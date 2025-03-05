from django.urls import path
from .views import PingView, AdminPc, AdminCity, AdminLaboratory

urlpatterns = [
    path('ping', PingView.as_view(), name='ping'),
    path('compute', AdminPc.as_view(), name='compute'),
    path('laboratory', AdminLaboratory.as_view(), name='laboratory'),
    path('city', AdminCity.as_view(), name='city'),
]
