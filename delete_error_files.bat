@echo off
echo Deleting error files from str.txt...

REM Delete files that caused LNK1104 errors during build

echo Deleting ActorManager plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\ActorManager\Binaries\Win64\UnrealEditor-ActorManager.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\ActorManager\Binaries\Win64\UnrealEditor-ActorManager.dll" 2>nul

echo Deleting ExUMG plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\ExGameplayPlugin\Binaries\Win64\UnrealEditor-ExUMG.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\ExGameplayPlugin\Binaries\Win64\UnrealEditor-ExUMG.dll" 2>nul

echo Deleting DistributedDS plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\DistributedDS\Binaries\Win64\UnrealEditor-DistributedDS.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\DistributedDS\Binaries\Win64\UnrealEditor-DistributedDS.dll" 2>nul

echo Deleting ExEditorTools plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\ExGameplayPlugin\Binaries\Win64\UnrealEditor-ExEditorTools.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\ExGameplayPlugin\Binaries\Win64\UnrealEditor-ExEditorTools.dll" 2>nul

echo Deleting TKHotfix plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TKHotfix\Binaries\Win64\UnrealEditor-TKHotfix.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TKHotfix\Binaries\Win64\UnrealEditor-TKHotfix.dll" 2>nul

echo Deleting CharacterSync plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\CharacterSync\Binaries\Win64\UnrealEditor-CharacterSync.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\CharacterSync\Binaries\Win64\UnrealEditor-CharacterSync.dll" 2>nul

echo Deleting GCloud plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\GCloud\Binaries\Win64\UnrealEditor-GCloud.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\GCloud\Binaries\Win64\UnrealEditor-GCloud.dll" 2>nul

echo Deleting DNS_OneSDK plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\DNS_OneSDK\Binaries\Win64\UnrealEditor-DNS_OneSDK.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\DNS_OneSDK\Binaries\Win64\UnrealEditor-DNS_OneSDK.dll" 2>nul

echo Deleting CrashSight plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\CrashSight\Binaries\Win64\UnrealEditor-CrashSight.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\CrashSight\Binaries\Win64\UnrealEditor-CrashSight.dll" 2>nul

echo Deleting GEM_OneSDK plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\GEM_OneSDK\Binaries\Win64\UnrealEditor-GEM_OneSDK.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\GEM_OneSDK\Binaries\Win64\UnrealEditor-GEM_OneSDK.dll" 2>nul

echo Deleting TApm plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\TApm\Binaries\Win64\UnrealEditor-TApm.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\GCloudSDK\TApm\Binaries\Win64\UnrealEditor-TApm.dll" 2>nul

echo Deleting TKGCloud plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TKGCloud\Binaries\Win64\UnrealEditor-TKGCloud.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TKGCloud\Binaries\Win64\UnrealEditor-TKGCloud.dll" 2>nul

echo Deleting SpinePlugin plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\SpinePlugin\Binaries\Win64\UnrealEditor-SpinePlugin.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\SpinePlugin\Binaries\Win64\UnrealEditor-SpinePlugin.dll" 2>nul

echo Deleting SOCClientBase DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Binaries\Win64\UnrealEditor-SOCClientBase.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Binaries\Win64\UnrealEditor-SOCClientBase.dll" 2>nul

echo Deleting AssetPostprocessor plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\AssetPostprocessor\Binaries\Win64\UnrealEditor-AssetPostprocessor.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\AssetPostprocessor\Binaries\Win64\UnrealEditor-AssetPostprocessor.dll" 2>nul

echo Deleting CommonStartupLoadingScreen plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\GameplayKit\Binaries\Win64\UnrealEditor-CommonStartupLoadingScreen.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\GameplayKit\Binaries\Win64\UnrealEditor-CommonStartupLoadingScreen.dll" 2>nul

echo Deleting KawaiiPhysics plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\KawaiiPhysics\Binaries\Win64\UnrealEditor-KawaiiPhysics.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\KawaiiPhysics\Binaries\Win64\UnrealEditor-KawaiiPhysics.dll" 2>nul

echo Deleting EditorCameraPosition plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\EditorCameraPosition\Binaries\Win64\UnrealEditor-EditorCameraPosition.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\EditorCameraPosition\Binaries\Win64\UnrealEditor-EditorCameraPosition.dll" 2>nul

echo Deleting PSD2UMG plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\PSD2UMG\Binaries\Win64\UnrealEditor-PSD2UMG.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\PSD2UMG\Binaries\Win64\UnrealEditor-PSD2UMG.dll" 2>nul

echo Deleting KawaiiPhysicsEd plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\KawaiiPhysics\Binaries\Win64\UnrealEditor-KawaiiPhysicsEd.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\KawaiiPhysics\Binaries\Win64\UnrealEditor-KawaiiPhysicsEd.dll" 2>nul

echo Deleting JsonLibrary plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\OasisSDK\Binaries\Win64\UnrealEditor-JsonLibrary.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\OasisSDK\Binaries\Win64\UnrealEditor-JsonLibrary.dll" 2>nul

echo Deleting LowEntryExtendedStandardLibrary plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\LowEntryExtStdLib\Binaries\Win64\UnrealEditor-LowEntryExtendedStandardLibrary.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\LowEntryExtStdLib\Binaries\Win64\UnrealEditor-LowEntryExtendedStandardLibrary.dll" 2>nul

echo Deleting OasisLogin plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\OasisSDK\Binaries\Win64\UnrealEditor-OasisLogin.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\OasisSDK\Binaries\Win64\UnrealEditor-OasisLogin.dll" 2>nul

echo Deleting OasisWebBrowser plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\OasisSDK\Binaries\Win64\UnrealEditor-OasisWebBrowser.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\OasisSDK\Binaries\Win64\UnrealEditor-OasisWebBrowser.dll" 2>nul

echo Deleting SelectedDialogBox plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\SelectedDialogBox\Binaries\Win64\UnrealEditor-SelectedDialogBox.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\SelectedDialogBox\Binaries\Win64\UnrealEditor-SelectedDialogBox.dll" 2>nul

echo Deleting OasisWebBrowserWidget plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\OasisSDK\Binaries\Win64\UnrealEditor-OasisWebBrowserWidget.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\OasisSDK\Binaries\Win64\UnrealEditor-OasisWebBrowserWidget.dll" 2>nul

echo Deleting ContentFilter plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TATools\Binaries\Win64\UnrealEditor-ContentFilter.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TATools\Binaries\Win64\UnrealEditor-ContentFilter.dll" 2>nul

echo Deleting TSPythonScript plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TSPythonScript\Binaries\Win64\UnrealEditor-TSPythonScript.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TSPythonScript\Binaries\Win64\UnrealEditor-TSPythonScript.dll" 2>nul

echo Deleting WwiseUtils plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseUtils.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseUtils.dll" 2>nul

echo Deleting WwiseConcurrency plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseConcurrency.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseConcurrency.dll" 2>nul

echo Deleting TKCrashSight plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TKCrashSight\Binaries\Win64\UnrealEditor-TKCrashSight.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TKCrashSight\Binaries\Win64\UnrealEditor-TKCrashSight.dll" 2>nul

echo Deleting ZipUtility plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\ZipUtility\Binaries\Win64\UnrealEditor-ZipUtility.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\ZipUtility\Binaries\Win64\UnrealEditor-ZipUtility.dll" 2>nul

echo Deleting SpatialSound plugin DLL: E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\SpatialSound\Binaries\Win64\UnrealEditor-SpatialSound.dll
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\SpatialSound\Binaries\Win64\UnrealEditor-SpatialSound.dll" 2>nul

echo Deleting TKPerfSight plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TKPerfSight\Binaries\Win64\UnrealEditor-TKPerfSight.dll" 2>nul

echo Deleting WwiseSoundEngine plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseSoundEngine.dll" 2>nul

echo Deleting TATools plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\TATools\Binaries\Win64\UnrealEditor-TATools.dll" 2>nul

echo Deleting WwiseEngineUtils plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseEngineUtils.dll" 2>nul

echo Deleting WwiseObjectUtils plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseObjectUtils.dll" 2>nul

echo Deleting WwiseProcessing plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseProcessing.dll" 2>nul

echo Deleting WwiseFileHandler plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseFileHandler.dll" 2>nul

echo Deleting WwiseResourceLoader plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseResourceLoader.dll" 2>nul

echo Deleting WwiseProjectDatabase plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseProjectDatabase.dll" 2>nul

echo Deleting Wwise plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-Wwise.dll" 2>nul

echo Deleting WwiseResourceCooker plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-WwiseResourceCooker.dll" 2>nul

echo Deleting AkAudio plugin DLL...
del /f /q "E:\TKMAIN_DSBUILD\TK_TMR\TikiStar\Plugins\MinViablePluginSet\Wwise\Binaries\Win64\UnrealEditor-AkAudio.dll" 2>nul

echo.
echo File deletion completed.
echo.
echo Note: These files were causing LNK1104 errors during the build process.
echo Deleting them may help resolve the compilation issues.
pause