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

    



