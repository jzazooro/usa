from clases.codigograficos import codigografico 

if __name__ == "__main__":
    
    grafica=codigografico("dataset housing/USA_Housing.csv")
    
    grafica.grafico("dispersion", "Area Population", "Price")

    grafica.grafico("dispersion", "Avg. Area Income", "Avg.Area Number of Rooms")

    grafica.grafico("dispersion", "Avg. Area Income", "Price")