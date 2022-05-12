import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import sys


df = pd.DataFrame("navegacion.csv")
df = df.rename(columns={""})
df = df.dropna()
