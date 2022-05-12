import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import sys


df = pd.DataFrame("navegacion.csv")
gf = pd.Dataframe("conversiones.csv")

df = df.dropna()

class Coche:
    def __init__(self, marca):
        self.marca = df(marca)

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
        


