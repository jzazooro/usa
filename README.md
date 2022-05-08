# usa

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/usa.git)

He realizado un ejericio de estructuras y manejo de datos, en el que partiendo de un dataset, tenemos que hallar las graficas que describan las implicaciones estadisticas de él mismo.

### Codigograficos:

```
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
        if tipodegrafico=="dispersion":
            plt.scatter(self.dt[columnauno]. self.dt[columnados])
        else:
            self.dt.groupby(columnauno)[columnados].sum().plot(kind=tipodegrafico, ax=ax)
        ax.set_title('grafico' + tipodegrafico, loc='center', fontdict={'fontsize':14, 'fontweight': 'bold', 'color':'tab:green'})
        ax.set_ylabel('')
        plt.savefig('graficos/grafico' + ' - ' + tipodegrafico + columnauno + columnados + '.png', bbox_inches='tight')
```

### Main:

```
from clases.codigograficos import codigografico 

if __name__ == "__main__":
    
    grafica=codigografico("dataset housing/USA_Housing.csv")
    
    grafica.grafico("dispersion", "Area Population", "Price")

    grafica.grafico("dispersion", "Avg. Area Income", "Avg.Area Number of Rooms")

    grafica.grafico("dispersion", "Avg. Area Income", "Price")
```
