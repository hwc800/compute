
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import generics, serializers
from auto.models import PC, Laboratory, City


class AllSerializer(FlexFieldsModelSerializer):

    compute_name = serializers.SerializerMethodField(default='', read_only=True, help_text='compute name')
    host = serializers.CharField(default='', read_only=True, help_text='compute host')
    laboratory_name = serializers.SerializerMethodField(default='', read_only=True, help_text='laboratory name')
    city_name = serializers.SerializerMethodField(default='', read_only=True, help_text='city name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_compute_name(self, compute):

        return compute.name

    def get_host(self, compute):
        return compute.host

    def get_laboratory_name(self, compute):
        return compute.laboratory.name

    def get_city_name(self, compute):
        return compute.laboratory.city.name

    def to_representation(self, instance):

        return super().to_representation(instance)

    class Meta:
        model = PC
        fields = ['compute_name', 'host', 'city_name', 'laboratory_name']


class CitySerializer(FlexFieldsModelSerializer):
    city_name = serializers.SerializerMethodField(default='', read_only=True, help_text='city name')
    compute_count = serializers.SerializerMethodField(default='', read_only=True, help_text='city name')

    def get_city_name(self, city):
        return city.name

    def get_compute_count(self, city):
        return city.compute_count

    class Meta:
        model = City
        fields = ['city_name', 'compute_count']


class LaboratorySerializer(FlexFieldsModelSerializer):
    laboratory_name = serializers.SerializerMethodField(default='', read_only=True, help_text='laboratory name')
    compute_count = serializers.SerializerMethodField(default='', read_only=True, help_text='laboratory name')
    city_name = serializers.SerializerMethodField(default='', read_only=True, help_text='laboratory name')

    def get_laboratory_name(self, laboratory):
        return laboratory.name

    def get_city_name(self, laboratory):
        return laboratory.city.name

    def get_compute_count(self, laboratory):
        return laboratory.compute_count

    class Meta:
        model = Laboratory
        fields = ['laboratory_name', 'compute_count', 'city_name']
