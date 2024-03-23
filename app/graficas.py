# Graficas en python
# primero es instalar matplotlib en los packages
# luego se importa matplotlib

import matplotlib.pyplot as plt

def generate_bar_chart(labels,values):
  fig, ax = plt.subplots() # Crear figura y eje
  ax.bar(labels, values) # Generar grafica de barras
  #plt.show() # Mostrar grafica
  plt.savefig("imagen_grafica_bar.png")
  plt.close()
pass

def generate_pie_chart(labels,values):
  fig, ax = plt.subplots() # Crear figura y eje
  ax.pie(values, labels=labels) # Generar grafica de torta
  ax.axis('equal') # Hacer que la grafica sea circular
  #plt.show() # Mostrar grafica
  plt.savefig("imagen_grafica_pie.png")
  plt.close()
pass



if __name__ == '__main__':
  labels = ['a', 'b', 'c'] # Etiquetas
  values = [100, 200, 150] # Valores
  
  generate_bar_chart(labels,values) # Ejecutar la funcion generate_bar_chart()
  generate_pie_chart(labels,values) # Ejecutar la funcion generate_pie_chart()
  