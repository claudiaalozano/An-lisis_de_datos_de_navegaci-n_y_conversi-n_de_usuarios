import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import sys
from Clase.analisis import *


if __name__ == "__main__":
  from Clase.analisis import *
  recurrente = usuarios_recurrentes()
  tipo_conversion = call_form()
  visita = numero_visitas()
  popular = coche_mas_visitado()
  print(recurrente, tipo_conversion, visita, popular)
  