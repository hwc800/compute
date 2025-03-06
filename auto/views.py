import json

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status, generics
import pythonping
from django.db import transaction
from auto.models import PC, Laboratory, City
from auto.serializers import AllSerializer, LaboratorySerializer, CitySerializer


class PingView(APIView):
    def get(self, request, *args, **kwargs):
        host = self.request.GET.get('host')
        if not host:
            return HttpResponse({'error': 'Host is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = pythonping.ping(host, count=1)
            if response.success():
                return HttpResponse(json.dumps({'code': 200, 'status': 'success', 'message': f'{host} is reachable'}))
            else:
                return HttpResponse(json.dumps({'code': 200, 'status': 'failure', 'message': f'{host} is not reachable'}))
        except Exception as e:
            return HttpResponse(json.dumps({'code': 500, 'error': str(e)}))


class AdminPc(generics.RetrieveUpdateDestroyAPIView):

    def get(self, request, *args, **kwargs):
        compute_ip = self.request.GET.get('ComputeId', '')
        pc = PC.objects.filter(id=compute_ip)
        if not pc.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '主机不存在'}))
        serializer = AllSerializer(pc.first(), many=False)
        print(serializer.data)
        result = {'status': 200, 'data': serializer.data}
        return HttpResponse(json.dumps(result), content_type="text/html; charset=utf-8")

    def post(self, request, *args, **kwargs):
        pc_name = self.request.POST.get('ComputeName', '')
        pc_ip = self.request.POST.get('IP', '')
        laboratory_name = self.request.POST.get('LaboratoryName', '')
        city_name = self.request.POST.get('CityName', '')
        with transaction.atomic():
            city = City.objects.filter(name=city_name)
            if not city.exists():
                return HttpResponse(json.dumps({'status': 200, 'msg': '城市名不存在'}))
            city = city.first()
            laboratory = Laboratory.objects.filter(name=laboratory_name, city=city)
            if not laboratory.exists():
                return HttpResponse(json.dumps({'status': 200, 'msg': '实验室不存在'}))
            laboratory = laboratory.first()
            pc = PC.objects.filter(laboratory=laboratory, name=pc_name, host=pc_ip)
            if pc.exists():
                return HttpResponse(json.dumps({'status': 200, 'msg': '主机已存在'}))
            PC.objects.create(laboratory=laboratory, name=pc_name, host=pc_ip)
            return HttpResponse(json.dumps({'status': 200, 'msg': '新增成功'}))

    def patch(self, request, *args, **kwargs):
        pc_id = self.request.GET.get('ComputeID', '')
        rename = self.request.GET.get('Rename', '')

        if not pc_id:
            return HttpResponse(json.dumps({'status': 200, 'msg': '请确认参数'}))

        pc = PC.objects.filter(id=pc_id)
        if not pc.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '主机不存在'}))
        pc.update(name=rename)
        return HttpResponse(json.dumps({'status': 200, 'msg': '修改成功'}))

    def delete(self, request, *args, **kwargs):
        pc_id = self.request.GET.get('ComputeID', '')

        if not pc_id:
            return HttpResponse(json.dumps({'status': 200, 'msg': '请确认参数'}))
        pc = PC.objects.filter(id=pc_id)
        if not pc.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '主机不存在'}))
        pc.delete()
        return HttpResponse(json.dumps({'status': 200, 'msg': '删除成功'}))


class AdminLaboratory(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        laboratory_id = self.request.GET.get('LaboratoryId', '')
        laboratory = Laboratory.objects.filter(id=laboratory_id)
        if not laboratory.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '实验室不存在'}))

        serializer = LaboratorySerializer(laboratory.first(), many=False)
        print(serializer.data)
        result = {'status': 200, 'data': serializer.data}
        return HttpResponse(json.dumps(result), content_type="text/html; charset=utf-8")

    def post(self, request, *args, **kwargs):
        laboratory_name = self.request.GET.get('LaboratoryName', '')
        rename = self.request.GET.get('Rename', '')
        city_name = self.request.GET.get('CityName', '')

        if not laboratory_name or not city_name or rename:
            return HttpResponse(json.dumps({'status': 200, 'msg': '请确认参数'}))
        city = City.objects.filter(name=city_name)
        if not city.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '城市名错误'}))
        city = city.first()
        laboratory = Laboratory.objects.filter(name=laboratory_name, city=city)
        if laboratory.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '实验室已存在'}))
        Laboratory.objects.create(name=laboratory_name, city=city)
        return HttpResponse(json.dumps({'status': 200, 'msg': '实验室已新增成功'}))

    def patch(self, request, *args, **kwargs):
        laboratory_name = self.request.GET.get('LaboratoryName', '')
        rename = self.request.GET.get('Rename', '')
        city_name = self.request.GET.get('CityName', '')

        if not laboratory_name or not city_name or rename:
            return HttpResponse(json.dumps({'status': 200, 'msg': '请确认参数'}))
        city = City.objects.filter(name=city_name)
        if not city.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '城市名错误'}))
        city = city.first()
        laboratory = Laboratory.objects.filter(name=laboratory_name, city=city)
        if not laboratory.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '实验室不存在'}))
        laboratory.update(name=rename)
        return HttpResponse(json.dumps({'status': 200, 'msg': '修改成功'}))

    def delete(self, request, *args, **kwargs):
        laboratory_name = self.request.GET.get('LaboratoryName', '')
        city_name = self.request.GET.get('CityName', '')

        if not laboratory_name or not city_name:
            return HttpResponse(json.dumps({'status': 200, 'msg': '请确认参数'}))
        city = City.objects.filter(name=city_name)
        if not city.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '城市名错误'}))
        city = city.first()
        laboratory = Laboratory.objects.filter(name=laboratory_name, city=city)
        if not laboratory.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '实验室不存在'}))
        laboratory.delete()
        return HttpResponse(json.dumps({'status': 200, 'msg': '删除成功'}))


class AdminCity(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        city_name = self.request.GET.get('CityName', '')
        city = City.objects.filter(name=city_name)
        if not city.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '城市不存在'}))
        serializer = CitySerializer(city.first(), many=False)
        print(serializer.data)
        result = {'status': 200, 'data': serializer.data}
        return HttpResponse(json.dumps(result), content_type="text/html; charset=utf-8")

    def post(self, request, *args, **kwargs):
        city_name = self.request.GET.get('CityName', '')

        if not city_name:
            return HttpResponse(json.dumps({'status': 200, 'msg': '请确认参数'}))
        city = City.objects.filter(name=city_name)

        if city.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '城市已存在'}))
        City.objects.create(name=city_name)
        return HttpResponse(json.dumps({'status': 200, 'msg': '城市已新增成功'}))

    def patch(self, request, *args, **kwargs):
        city_name = self.request.GET.get('CityName', '')

        if not city_name:
            return HttpResponse(json.dumps({'status': 200, 'msg': '请确认参数'}))
        city = City.objects.filter(name=city_name)
        if not city.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '城市不存在'}))
        city = city.first()
        city.update(name=city_name)
        return HttpResponse(json.dumps({'status': 200, 'msg': '修改成功'}))

    def delete(self, request, *args, **kwargs):
        city_name = self.request.GET.get('CityName', '')

        if not city_name:
            return HttpResponse(json.dumps({'status': 200, 'msg': '请确认参数'}))
        city = City.objects.filter(name=city_name)
        if not city.exists():
            return HttpResponse(json.dumps({'status': 200, 'msg': '城市不存在'}))
        city.delete()
        return HttpResponse(json.dumps({'status': 200, 'msg': '删除成功'}))

