#!/usr/bin/env python3
"""
多仓库Git分支同步工具
功能：支持多个仓库的指定分支重置到特定时间点的commit，并强制推送到远程
配置方式：通过环境变量读取仓库配置
"""


import argparse
import json
import time
import datetime
import os
import subprocess
import sys

# 退出码定义
EXIT_SUCCESS = 0
EXIT_GENERAL_ERROR = 1
EXIT_PERMISSION_ERROR = 2
EXIT_ARGUMENT_ERROR = 3
EXIT_NOT_FOUND_ERROR = 4


def merge_and_resolve_conflicts(repo_path, resolve_strategy, branch_name):
    """
    合并远端分支到本地分支并解决冲突

    参数:
        repo_path: Git仓库路径
        resolve_strategy: 解决策略（ours/theirs）
        branch_name: 远端分支名

    返回:
        bool: 操作是否成功
    """
    print(f"开始合并远端分支 {branch_name} 到本地分支...")
    print(f"仓库路径: {repo_path}")
    print(f"解决策略: {resolve_strategy}")
    print(f"分支名: {branch_name}")

    # 切换到指定目录
    if not os.path.exists(repo_path):
        print(f"[ERROR] 目录不存在: {repo_path}")
        return False

    original_cwd = os.getcwd()
    try:
        os.chdir(repo_path)
        print(f"已切换到目录: {repo_path}")

        # 远端分支合入到本地分支
        merge_cmd = f'git merge --strategy-option={resolve_strategy} origin/{branch_name}'
        print(f"执行合并命令: {merge_cmd}")

        merge_result = subprocess.run(merge_cmd, shell=True, capture_output=True, text=True)

        if merge_result.returncode != 0:
            print(f"合并过程中出现冲突或错误:")
            print(f"stdout: {merge_result.stdout}")
            print(f"stderr: {merge_result.stderr}")

        # 合入完毕后需要睡眠一段时间
        print("等待60秒，确保git进程完全退出...")
        time.sleep(60)

        # 删除index.lock文件（如果存在）
        lock_file = ".git/index.lock"
        if os.path.exists(lock_file):
            try:
                os.remove(lock_file)
                print("已删除index.lock文件")
            except Exception as e:
                print(f"删除index.lock文件失败: {e}")
        else:
            print("index.lock文件不存在")

        # 遍历解决冲突文件
        print("开始解决冲突文件...")

        # 获取冲突文件列表
        conflict_cmd = 'git diff --name-only --diff-filter=U'
        conflict_result = subprocess.run(conflict_cmd, shell=True, capture_output=True, text=True)

        if conflict_result.returncode == 0 and conflict_result.stdout.strip():
            conflict_files = conflict_result.stdout.strip().split('\n')
            print(f"发现 {len(conflict_files)} 个冲突文件:")

            for conflict_file in conflict_files:
                if conflict_file.strip():
                    print(f"处理冲突文件: {conflict_file}")

                    # 使用参数覆盖冲突文件
                    checkout_cmd = f'git checkout --{resolve_strategy} -- "{conflict_file}"'
                    checkout_result = subprocess.run(checkout_cmd, shell=True, capture_output=True, text=True)

                    if checkout_result.returncode == 0:
                        print(f"✓ 已解决冲突: {conflict_file}")

                        # 单独添加每个已解决的文件
                        add_cmd = f'git add -f -- "{conflict_file}"'
                        add_result = subprocess.run(add_cmd, shell=True, capture_output=True, text=True)

                        if add_result.returncode == 0:
                            print(f"✓ 已添加文件: {conflict_file}")
                        else:
                            print(f"✗ 添加文件失败: {conflict_file}")
                            print(f"错误信息: {add_result.stderr}")
                    else:
                        print(f"✗ 解决冲突失败: {conflict_file}")
                        print(f"错误信息: {checkout_result.stderr}")
        else:
            print("未发现冲突文件")

        # 完成合并提交
        commit_message = f"merge from origin/{branch_name}, strategy_option: {resolve_strategy}"
        commit_cmd = f'git commit -m "{commit_message}"'
        print(f"执行提交命令: {commit_cmd}")

        commit_result = subprocess.run(commit_cmd, shell=True, capture_output=True, text=True)

        if commit_result.returncode == 0:
            print("✓ 合并提交成功")
        else:
            print(f"✗ 合并提交失败: {commit_result.stderr}")

        # 推送更改
        print("开始推送更改到远端...")
        push_result = subprocess.run('git push', shell=True, capture_output=True, text=True)

        if push_result.returncode == 0:
            print("✓ 推送成功")
            return True
        else:
            print(f"✗ 推送失败: {push_result.stderr}")
            return False

    except Exception as e:
        print(f"[ERROR] 执行过程中出现异常: {e}")
        return False
    finally:
        os.chdir(original_cwd)
        print(f"已切换回原目录: {original_cwd}")


def load_repositories_from_env():
    """从环境变量加载仓库配置"""

    # 从环境变量读取仓库配置
    repositories = list()
    if os.environ.get('SyncBinEngine', None):
        # BinaryEngine
        repositories.append({'name': os.environ.get('BinEnginePath', 'BinEnginePath'),
                             'path': os.environ.get('variables.BinEnginePath', ''),
                             'branch': os.environ.get('BinEnginePullParam', '')})
    if os.environ.get('SyncEngine', None):
        # SourceEngine
        repositories.append({'name': os.environ.get('SourceEngine', 'SourceEngine'),
                             'path': os.environ.get('variables.EnginePullParam', ''),
                             'branch': os.environ.get('EnginePullParam', '')})
    # TikiMainContent
    repositories.append({'name': os.environ.get('Engine', ''),
                         'path': os.environ.get('variables.ContentPath', ''),
                         'branch': os.environ.get('variables.EnginePullParam', '')})
    # TikiMainRoot
    repositories.append({'name': os.environ.get('TikiMainRoot', 'TikiMainRoot'),
                         'path': os.environ.get('variables.TikiStarPath', ''),
                         'branch': os.environ.get('variables.TikiStarPullParam', '')})
    # TikiFramework Content
    repositories.append({'name': os.environ.get('TikiFrameworkContent', 'TikiFrameworkContent'),
                         'path': os.environ.get('variables.TikiFrameworkPath', ''),
                         'branch': os.environ.get('variables.TikiFrameworkPullParam', '')})
    # Framework
    repositories.append({'name': os.environ.get('Framework', ''),
                         'path': os.environ.get('variables.FrameworkPath', ''),
                         'branch': os.environ.get('variables.FrameworkPullParam', '')})
    # TKCoreFramework
    repositories.append({'name': os.environ.get('TKCoreFramework', 'TKCoreFramework'),
                         'path': os.environ.get('variables.TKCoreFrameworkPath', ''),
                         'branch': os.environ.get('variables.TKCoreFrameworkPullParam', '')})
    # SharedSystems
    repositories.append({'name': os.environ.get('SharedSystems', 'SharedSystems'),
                         'path': os.environ.get('variables.SharedSystemsPath', ''),
                         'branch': os.environ.get('variables.SharedSystemsPullParam', '')})
    # TS_MVSS
    repositories.append({'name': os.environ.get('TS_MVSS', 'TS_MVSS'),
                         'path': os.environ.get('variables.MinViableSystemSetPath', ''),
                         'branch': os.environ.get('variables.MinViableSystemSetPullParam', '')})
    # Cpp_MVSS
    repositories.append({'name': os.environ.get('Cpp_MVSS', 'Cpp_MVSS'),
                         'path': os.environ.get('variables.MinViableSourceSetPath', ''),
                         'branch': os.environ.get('variables.MinViableSourceSetPullParam', '')})
    # Plg_MVSS
    repositories.append({'name': os.environ.get('Plg_MVSS', 'Plg_MVSS'),
                         'path': os.environ.get('variables.MinViablePluginSetPath', ''),
                         'branch': os.environ.get('variables.MinViablePluginSetPullParam', '')})
    # BP_MVSS
    repositories.append({'name': os.environ.get('BP_MVSS', 'BP_MVSS'),
                         'path': os.environ.get('variables.MinViableBlueprintSetPath', ''),
                         'branch': os.environ.get('variables.MinViableBlueprintSetPullParam', '')})
    # Cnt_MVSS
    repositories.append({'name': os.environ.get('Cnt_MVSS', 'Cnt_MVSS'),
                         'path': os.environ.get('variables.MinViableContentSetPath', ''),
                         'branch': os.environ.get('variables.MinViableContentSetPullParam', '')})
    # Puerts
    repositories.append({'name': os.environ.get('Puerts', 'Puerts'),
                         'path': os.environ.get('variables.PuertsPath', ''),
                         'branch': os.environ.get('variables.PuertsPullParam', '')})
    # ProtoJS
    repositories.append({'name': os.environ.get('ProtoJS', 'ProtoJS'),
                         'path': os.environ.get('variables.ProtoJSPath', ''),
                         'branch': os.environ.get('variables.ProtoJSPullParam', '')})
    # DDSFade
    repositories.append({'name': os.environ.get('DDSFade', 'DDSFade'),
                         'path': os.environ.get('variables.DistributedDSPath', ''),
                         'branch': os.environ.get('variables.DistributedDSPullParam', '')})
    # GCloudSDK
    repositories.append({'name': os.environ.get('GCloudSDK', 'GCloudSDK'),
                         'path': os.environ.get('variables.GCloudSDKPath', ''),
                         'branch': os.environ.get('variables.GCloudSDKPullParam', '')})
    # GameFeatures
    repositories.append({'name': os.environ.get('GameFeatures', 'GameFeatures'),
                         'path': os.environ.get('variables.GameFeaturesPath', ''),
                         'branch': os.environ.get('variables.GameFeaturesPullParam', '')})
    # TKPartyGame
    repositories.append({'name': os.environ.get('TKPartyGame', 'TKPartyGame'),
                         'path': os.environ.get('variables.TKPartyGamePath', ''),
                         'branch': os.environ.get('variables.TKPartyGamePullParam', '')})
    # TKPartyGame Content
    repositories.append({'name': os.environ.get('TKPartyGameContent', 'TKPartyGameContent'),
                         'path': os.environ.get('variables.TKPartyGame_ContentPath', ''),
                         'branch': os.environ.get('variables.TKPartyGame_ContentPullParam', '')})

    # TKPartyGameSystem
    repositories.append({'name': os.environ.get('TKPartyGameSystem', 'TKPartyGameSystem'),
                         'path': os.environ.get('variables.TKPartyGameSystemPath', ''),
                         'branch': os.environ.get('variables.TKPartyGameSystemPullParam', '')})
    # TKPartyGameSystem Content
    repositories.append({'name': os.environ.get('TKPartyGameSystemContent', 'TKPartyGameSystemContent'),
                         'path': os.environ.get('variables.TKPartyGameSystem_ContentPath', ''),
                         'branch': os.environ.get('variables.TKPartyGameSystem_ContentPullParam', '')})
    # # JSC Compiler, 强制同步不需要
    # repositories.append({'name': os.environ.get('JSCCompiler', 'JSCCompiler'),
    #                      'path': os.environ.get('variables.jsc_compilerPath', ''),
    #                      'branch': os.environ.get('variables.jsc_compilerPullParam', '')})
    if os.environ.get("SyncConfigData", 'false') == 'ture':
        # ConfigData
        repositories.append({'name': os.environ.get('ConfigData', 'ConfigData'),
                             'path': os.environ.get('variables.ConfigDataPath', ''),
                             'branch': os.environ.get('variables.ConfigDataPullParam', '')})

    # ProtocolFile
    if os.environ.get('SyncProtocolFile', 'false') == 'ture':
        repositories.append({'name': os.environ.get('ConfigData', 'ConfigData'),
                             'path': os.environ.get('variables.ProtocolFilePath', ''),
                             'branch': os.environ.get('variables.ProtocolFilePullParam', '')})
    return repositories

def validate_repository(repo_path):
    """验证仓库路径是否有效"""
    if not os.path.exists(repo_path):
        print(f"仓库路径不存在: {repo_path}")
        return False
    
    git_dir = os.path.join(repo_path, ".git")
    if not os.path.exists(git_dir):
        print(f"路径不是Git仓库: {repo_path}")
        return False
    
    return True

def run_command(cmd, capture_output=True, cwd=None):
    """执行shell命令并返回结果"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=capture_output, text=True, cwd=cwd)
        return result
    except Exception as e:
        print(f"执行命令失败: {cmd}")
        print(f"错误信息: {e}")
        return None

def get_dest_commit_id(branch, sync_time=None, repo_path="."):
    """获取目标commit ID"""
    if not sync_time:
        # 同步到最新
        cmd = f'git rev-parse origin/{branch}'
        result = run_command(cmd, cwd=repo_path)
        if result and result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"获取分支 {branch} 最新commit失败: {result.stderr if result else '未知错误'}")
            return None
    else:
        # 同步到指定时间前的最后一个commit
        cmd = f'git log --before=\"{sync_time}\" -1 --format=\"%H\" origin/{branch}'
        result = run_command(cmd, cwd=repo_path)
        if result and result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            print(f"在分支 {branch} 中找不到 {sync_time} 之前的commit")
            return None

def reset_branch(branch, sync_time=None, repo_path="."):
    """重置分支到指定commit"""
    print(f"开始重置分支 {branch}...")

    # 获取目标commit ID
    dest_commit_id = get_dest_commit_id(branch, sync_time, repo_path)
    if not dest_commit_id:
        return False

    print(f"目标commit ID: {dest_commit_id[:7]}")

    # reset hard到指定commit
    reset_cmd = f'git reset --hard {dest_commit_id}'
    reset_result = run_command(reset_cmd, capture_output=False, cwd=repo_path)
    if not reset_result or reset_result.returncode != 0:
        print(f"重置分支失败: {reset_result.stderr if reset_result else '未知错误'}")
        return False

    print("重置分支成功")

    # 强制推送到远端
    push_cmd = 'git push --force'
    push_result = run_command(push_cmd, capture_output=False, cwd=repo_path)
    if not push_result or push_result.returncode != 0:
        print(f"强制推送失败: {push_result.stderr if push_result else '未知错误'}")
        return False

    print("强制推送成功")

    # 清理工作目录
    clean_cmd = 'git clean -f -d'
    clean_result = run_command(clean_cmd, capture_output=False, cwd=repo_path)
    if not clean_result or clean_result.returncode != 0:
        print(f"清理工作目录失败: {clean_result.stderr if clean_result else '未知错误'}")
        return False

    print("清理工作目录成功")

    # 获取当前的最新commit ID
    cur_commit_cmd = 'git rev-parse HEAD'
    cur_commit_result = run_command(cur_commit_cmd, cwd=repo_path)
    if not cur_commit_result or cur_commit_result.returncode != 0:
        print(f"获取当前commit失败: {cur_commit_result.stderr if cur_commit_result else '未知错误'}")
        return False

    cur_commit_id = cur_commit_result.stdout.strip()

    # 比对是否与目标commit ID一致
    if cur_commit_id == dest_commit_id:
        print(f"重置 {branch} 成功! CommitID: {cur_commit_id[:7]}")
        return True
    else:
        print(f"重置 {branch} 失败! CommitID不匹配: {cur_commit_id[:7]} != {dest_commit_id[:7]}")
        return False



def sync_repositories(repositories, sync_time=None):
    """同步所有仓库"""
    if not repositories:
        print("没有定义任何仓库")
        return False

    print(f"开始同步 {len(repositories)} 个仓库...")

    # 记录详细的同步结果
    sync_results = []
    success_count = 0
    failed_count = 0

    for repo in repositories:
        repo_name = repo.get("name", "未命名仓库")
        # 拼接绝对路径
        repo_path = os.path.join(os.environ.get("Workspace", ""), repo.get("path", ""))
        branch = repo.get("branch", "master")

        print(f"\n{'='*50}")
        print(f"同步仓库: {repo_name}")
        print(f"路径: {repo_path}")
        print(f"分支: {branch}")

        # 验证仓库
        if not validate_repository(repo_path):
            print(f"[ERROR] 仓库验证失败，跳过: {repo_name}")
            sync_results.append({
                "name": repo_name,
                "path": repo_path,
                "branch": branch,
                "success": False,
                "error": "仓库验证失败"
            })
            failed_count += 1
            continue

        # 保存当前工作目录
        original_cwd = os.getcwd()

        try:
            # 切换到仓库目录
            os.chdir(repo_path)
            print(f"已切换到仓库目录: {repo_path}")

            # 在同步前为当前状态打tag
            print("在同步前为当前状态打tag...")
            tag_success = tag_latest_commit(branch)
        except Exception as e:
            print(f"处理仓库 {repo_name} 时发生错误: {e}")
            sync_results.append({
                "name": repo_name,
                "path": repo_path,
                "branch": branch,
                "success": False,
                "error": f"处理过程中发生错误: {e}"
            })
            failed_count += 1
            continue
        finally:
            # 恢复原始工作目录
            os.chdir(original_cwd)

        if tag_success:
            print(f"{repo_name}同步前tag创建成功")
        else:
            print(f"{repo_name}同步前tag创建失败")

        # 执行同步（reset_branch函数内部会处理目录切换）
        success = reset_branch(branch, sync_time, repo_path)

        if success:
            print(f"[SUCCESS] {repo_name} 同步成功")
            sync_results.append({
                "name": repo_name,
                "path": repo_path,
                "branch": branch,
                "success": True,
                "error": None
            })
            success_count += 1
        else:
            print(f"[ERROR] {repo_name} 同步失败")
            sync_results.append({
                "name": repo_name,
                "path": repo_path,
                "branch": branch,
                "success": False,
                "error": "同步过程中出现错误"
            })
            failed_count += 1

    # 详细显示同步结果
    print(f"\n{'='*60}")
    print("=== 同步完成详情 ===")
    print(f"总计仓库数: {len(repositories)}")
    print(f"成功: {success_count}")
    print(f"失败: {failed_count}")

    # 显示成功仓库列表
    if success_count > 0:
        print(f"\n[SUCCESS] 成功同步的仓库 ({success_count}个):")
        for result in sync_results:
            if result["success"]:
                print(f"  - {result['name']} (分支: {result['branch']})")

    # 显示失败仓库列表及错误信息
    if failed_count > 0:
        print(f"\n[ERROR] 同步失败的仓库 ({failed_count}个):")
        for result in sync_results:
            if not result["success"]:
                print(f"  - {result['name']} (分支: {result['branch']})")
                if result["error"]:
                    print(f"    错误: {result['error']}")

    print(f"\n{'='*60}")

    return failed_count == 0


def check_git_permission():
    """
    检查git操作权限

    Returns:
        tuple: (has_read_permission, has_write_permission)
    """
    try:
        # 检查是否有读取权限（列出远程分支）
        read_cmd = 'git ls-remote --heads origin'
        read_result = subprocess.run(read_cmd, shell=True, capture_output=True, text=True)
        has_read_permission = read_result.returncode == 0

        # 检查是否有写入权限（尝试创建一个临时tag来测试）
        write_cmd = 'git tag --list test_permission_check_12345'
        write_result = subprocess.run(write_cmd, shell=True, capture_output=True, text=True)

        # 如果能够执行tag相关命令，说明有基本权限
        has_write_permission = write_result.returncode == 0

        return has_read_permission, has_write_permission

    except Exception as e:
        print(f"权限检查失败：{e}")
        return False, False


def check_delete_permission():
    """
    检查删除tag的权限

    Returns:
        bool: 是否有删除权限
    """
    print("检查删除权限...")

    has_read, has_write = check_git_permission()

    if not has_read:
        print("  没有读取权限，无法访问远程仓库")
        return False

    if not has_write:
        print("  没有写入权限，无法执行删除操作")
        return False

    print("  权限检查通过")
    return True


def get_latest_commit(branch_name):
    """
    获取指定分支最新的commit id

    Args:
        branch_name: 分支名称

    Returns:
        str: 最新的commit id，如果失败返回None
    """
    try:
        # 获取最新的commit
        cmd = f'git log {branch_name} -1 --pretty=format:"%H"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"错误：获取最新commit失败 - {result.stderr}")
            return None

        commit_id = result.stdout.strip()

        if not commit_id:
            print(f"分支 '{branch_name}' 没有找到任何commit")
            return None

        print(f"在分支 '{branch_name}' 中找到最新commit: {commit_id[:7]}")
        return commit_id

    except Exception as e:
        print(f"获取最新commit时发生错误：{e}")
        return None


def create_tag_for_commit(commit_id, tag_prefix=""):
    """
    为指定的commit创建tag

    Args:
        commit_id: commit id
        tag_prefix: tag前缀（如果为空则使用分支名_日期格式）

    Returns:
        bool: 是否成功创建tag
    """
    try:
        # 获取当前分支名称
        branch_cmd = 'git rev-parse --abbrev-ref HEAD'
        branch_result = subprocess.run(branch_cmd, shell=True, capture_output=True, text=True)

        if branch_result.returncode != 0:
            print(f"获取当前分支失败：{branch_result.stderr}")
            return False

        branch_name = branch_result.stdout.strip()

        # 生成tag名称（使用分支名_当前日期格式）
        current_date = datetime.datetime.now().strftime("%Y%m%d")

        if tag_prefix:
            tag_name = f"{tag_prefix}{current_date}"
        else:
            tag_name = f"{branch_name}_{current_date}"

        # 检查tag是否已存在
        check_cmd = f'git tag -l "{tag_name}"'
        check_result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)

        if check_result.stdout.strip():
            print(f"Tag '{tag_name}' 已存在，跳过")
            return True

        # 创建tag
        cmd = f'git tag {tag_name} {commit_id}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"成功为commit {commit_id[:7]} 创建tag: {tag_name}")
            return True
        else:
            print(f"创建tag失败：{result.stderr}")
            return False

    except Exception as e:
        print(f"创建tag时发生错误：{e}")
        return False


def delete_local_tag(tag_name):
    """
    删除本地tag

    Args:
        tag_name: tag名称

    Returns:
        bool: 是否成功删除
    """
    try:
        # 检查tag是否存在
        check_cmd = f'git tag -l "{tag_name}"'
        check_result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True)

        if not check_result.stdout.strip():
            print(f"Tag '{tag_name}' 不存在，无需删除")
            return True

        # 删除本地tag
        cmd = f'git tag -d {tag_name}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"成功删除本地tag: {tag_name}")
            return True
        else:
            error_msg = result.stderr
            if "authority" in error_msg.lower() or "permission" in error_msg.lower():
                print(f"  权限不足，无法删除本地tag: {tag_name}")
                print("   请检查您是否有足够的权限执行此操作")
            else:
                print(f"删除本地tag失败：{error_msg}")
            return False

    except Exception as e:
        print(f"删除本地tag时发生错误：{e}")
        return False


def delete_remote_tag(tag_name):
    """
    删除远程tag

    Args:
        tag_name: tag名称

    Returns:
        bool: 是否成功删除
    """
    try:
        # 先检查权限
        if not check_delete_permission():
            return False

        # 删除远程tag
        cmd = f'git push origin --delete {tag_name}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"成功删除远程tag: {tag_name}")
            return True
        else:
            error_msg = result.stderr
            if "authority" in error_msg.lower() or "permission" in error_msg.lower():
                print(f"  权限不足，无法删除远程tag: {tag_name}")
                print("   您没有删除此项目的tag的权限")
                print("   请联系项目管理员获取权限")
            else:
                print(f"删除远程tag失败：{error_msg}")
            return False

    except Exception as e:
        print(f"删除远程tag时发生错误：{e}")
        return False


def delete_tag(tag_name, delete_remote=True):
    """
    删除tag（本地和远程）

    Args:
        tag_name: tag名称
        delete_remote: 是否删除远程tag

    Returns:
        bool: 是否成功删除
    """
    print(f"开始删除tag: {tag_name}")

    # 删除本地tag
    if not delete_local_tag(tag_name):
        return False

    # 删除远程tag
    if delete_remote:
        if not delete_remote_tag(tag_name):
            print(f"警告：本地tag已删除，但远程tag删除失败")
            return False

    print(f"成功删除tag: {tag_name}")
    return True


def list_tags(pattern="*"):
    """
    列出所有tag

    Args:
        pattern: tag匹配模式

    Returns:
        list: tag列表
    """
    try:
        cmd = f'git tag -l "{pattern}"'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            tags = [tag.strip() for tag in result.stdout.split('\n') if tag.strip()]
            return tags
        else:
            print(f"获取tag列表失败：{result.stderr}")
            return []

    except Exception as e:
        print(f"获取tag列表时发生错误：{e}")
        return []


def tag_latest_commit(branch_name, tag_prefix=""):
    """
    为指定分支的最新commit打tag

    Args:
        branch_name: 分支名称
        tag_prefix: tag前缀（如果为空则使用分支名_日期格式）

    Returns:
        bool: 是否成功
    """
    print(f"开始为分支 '{branch_name}' 的最新commit打tag...")

    # 获取最新的commit
    commit_id = get_latest_commit(branch_name)

    if not commit_id:
        print("没有找到需要打tag的commit")
        return False

    # 为commit打tag
    if create_tag_for_commit(commit_id, tag_prefix):
        print(f"\n成功为分支 '{branch_name}' 的最新commit打tag")

        # 推送tag到远程仓库
        try:
            push_cmd = "git push origin --tags"
            push_result = subprocess.run(push_cmd, shell=True, capture_output=True, text=True)
            if push_result.returncode == 0:
                print("推送tag到远程仓库成功")
            else:
                error_msg = push_result.stderr
                if "authority" in error_msg.lower() or "permission" in error_msg.lower():
                    print("  权限不足，无法推送tag到远程仓库")
                    print("   您没有推送tag到此项目的权限")
                else:
                    print(f"推送tag失败：{error_msg}")
        except Exception as e:
            print(f"推送tag时发生错误：{e}")

        return True
    else:
        print(f"\n为分支 '{branch_name}' 的最新commit打tag失败")
        return False


def show_permission_status():
    """显示当前权限状态"""
    print("检查当前git权限状态...")
    has_read, has_write = check_git_permission()

    print(f"读取权限: {'  有' if has_read else '  无'}")
    print(f"写入权限: {'  有' if has_write else '  无'}")

    if not has_read:
        print("\n🔍 可能的原因：")
        print("  • 没有访问远程仓库的权限")
        print("  • 网络连接问题")
        print("  • 认证信息错误")

    if not has_write:
        print("\n🔍 可能的原因：")
        print("  • 没有推送权限")
        print("  • 项目权限设置限制")
        print("  • 需要管理员权限")



def main():
    """主函数"""
    # 同步所有仓库到指定分支的最新commit
    # python ForceCodeSync.py - -branch test
    parser = argparse.ArgumentParser(description='多仓库Git分支同步工具')
    parser.add_argument('--branch', help='指定分支名称（覆盖配置中的分支设置）', default=None)

    args = parser.parse_args()

    # 从环境变量SyncTime读取同步时间
    sync_time = os.environ.get('SyncTime')
    if sync_time:
        print(f"从环境变量读取同步时间: {sync_time}")

    # 从环境变量加载仓库配置
    # repositories = load_repositories_from_env()
    repositories = [{'name': 'mycode',
                     'path': '.',
                     'branch': 'test'}]
    # 如果指定了分支参数，覆盖所有仓库的分支设置
    if args.branch:
        for repo in repositories:
            repo["branch"] = args.branch
        print(f"使用指定分支: {args.branch}")
    
    # 执行同步
    success = sync_repositories(repositories, sync_time)
    if not success:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()