import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np 

class codigografico:
    
    def __init__(self, archivo):
        self.archivo=archivo
        self.dt=pd.read_csv(archivo)
    
    def grafico(self, tipodegrafico, columnauno, columnados):
        
        def pearson():
            correlacion=np.corrcoef(self.dt[columnauno], self.dt[columnados])
            correlacion=round(correlacion[0], [1], 3)
            return correlacion
        
        print("el coeficiente de correlacion de pearson es {}".format(pearson()))
        fig, ax =plt.subplots()
        