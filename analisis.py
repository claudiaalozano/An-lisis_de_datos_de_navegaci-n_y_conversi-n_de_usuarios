import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import sys


df = pd.DataFrame("navegacion.csv")

df = df.dropna()

class Coche:
    def __init__(self, marca):
        self.marca = df(marca)

    def call_form(self):
        

