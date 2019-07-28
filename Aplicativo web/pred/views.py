from django.shortcuts import render, get_object_or_404, redirect
from .models import Desc, Cult, Datos
from .forms import DataForm
import pickle
import numpy as np
from sklearn import ensemble

# Vista para la página principal
def desc_list(request):
    Descrip = "Descripción del cultivo"
    Vars = "Variables consideradas"
    Predict = "Predicción"
    return render(request,'pred/post_list.html',{"Vars":Vars,"Predict":Predict,"Descrip":Descrip})

# Se prueba crea una vista para la descripción
def descrip_list(request):
    posts = Desc.objects.order_by("Titulo")
    return render(request,'pred/desc_list.html',{"posts":posts})

# Se crea una vista para las variables
def vars_list(request):
    cults = Cult.objects.order_by("Titulo")
    return render(request,'pred/cult_detail.html',{"cults":cults})

# Se crea una vista para las predicciones
def pred_list(request):
    datos = Datos.objects.order_by("Titulo")
    return render(request,'pred/pred_list.html',{"datos":datos})

# Vista para los datos del modelo
def dato_detail(request,pk):
    dato = get_object_or_404(Datos,pk=pk)
    predict_model = pickle.load(open("Modelo final.sav","rb"))
    predict = np.round(predict_model.predict([[dato.P_accu,dato.T_avg_prev,dato.Rad_accu_prev1]]),3)
    return render(request,"pred/ML.html", {"dato": dato,"predict":predict})

# Formulario para ingresar información
def datos_new(request):
    if request.method=="POST":
        form = DataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect("dato_detail",pk=post.pk)
    else:
        form = DataForm(initial={"P_accu":0,"T_avg_prev":0,"Rad_accu_prev1":0})
    return render(request, "pred/data_edit.html",{"form":form})
