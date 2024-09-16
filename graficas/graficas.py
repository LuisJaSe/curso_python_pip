# Importando la libreria de matplotlib
import matplotlib.pyplot as plt # type: ignore

# Ejemplo de grafica pastel utilziando matplotlib
def grafica_pastel():
    labels = ["A", "B", "C", "D", "E", "F"]
    values = [20, 30, 40, 50, 60, 200]
    
    fig, ax = plt.subplots() # Crear figura y eje
    ax.pie(values, labels=labels) # Generar grafica de torta
    ax.axis('equal') # Hacer que la grafica sea circular
    #pyplot.show() # Mostrar grafica
    plt.savefig("imagen_grafica.png")
    plt.close()
    
grafica_pastel()