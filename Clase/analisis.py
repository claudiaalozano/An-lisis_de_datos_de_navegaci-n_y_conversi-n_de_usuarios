
import pandas as pd
import numpy as np
from replit import db
import matplotlib.pyplot as plt
import csv
import os
import sys

df = pd.DataFrame("navegacion.csv")
gf = pd.Dataframe("conversiones.csv")

df = df.dropna()

def call_form(self):
    #como es un contador, creo dos variables para cada uno
    call = 0
    form = 0
    i = 0
    for i in gf["lead_type"]:
        if i == "call":
            call = call +1
        elif i == "form":
            form = form + 1
    print("Call = " , call, "\n" , "Form = ", form)

    
def usuarios_recurrentes (self):
    usuarios_recurrentes = 0
    #creo otro bucle para ver cuantos tengo
    for i in df["user_recurrent"]:
        if i == "True":
            usuarios_recurrentes = usuarios_recurrentes + 1
        
    total = df.count()["user_recurrent"]
    porcentaje = (usuarios_recurrentes * 100 )/ total
    print("El porcentaje de usuarios recurrentes es: ", porcentaje)
        

def numero_visitas(self):
    numero = df.count()["ts"]
    print("El numero de visitas del cliente es: ", numero)
        
    c1 = df["ts"]
    gf["Fechas"] = gf["date"] + " " + gf["hour"]
        

    contador = 0 
    for i in c1:
        if i in gf["Fechas"]:
            contador = contador + 1
    porcentaje = (contador * 100 )/ numero
    print("El porcentaje de visitas es: " , porcentaje)

      
def coche_mas_visitado(self):
    lista = [] 
        
    for i in df["url_landing"]:

        coche = lista.append(i.split("/"))[-1]
        lista[coche] = lista + 1
    print(lista)

