from django.urls import path
from . import views

urlpatterns = [
    path('', views.desc_list, name='post_list'),
    path("descrip/new",views.descrip_list,name="datos_nuevo"),       # Descripción del cultivo
    path("vars/new",views.vars_list,name="vars_nuevo"),              # Descripción de las variables
    path("pred/new",views.pred_list,name="predicciones"),            # Realizar predicciones
    path("datos/<int:pk>",views.dato_detail, name="dato_detail"),    # Agregar información
    path("datos/new",views.datos_new,name="datos_new"),              # Formulario para agregar información

]
