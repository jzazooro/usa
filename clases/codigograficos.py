import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

class codigografico:
    
    def __init__(self, archivo):
        self.archivo=archivo
        self.dt=pd.read_csv(archivo)
    
    