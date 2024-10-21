from django.urls import path
from alumno import views

urlpatterns = [
    path('', views.Index_Vista, name='Index_vista'),
    path('alumno/<int:id>',views.Alumno_Vista, name='alumno_Vista')
]