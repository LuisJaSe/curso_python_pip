# Leer archivos csv -----------------------------------

import csv # Importar el modulo csv, sirve para leer archivos csv

# Funcion para leer archivos csv --------------------------------
def read_csv(ruta_archivo):
  with open(ruta_archivo, 'r') as csvfile: # 1. Abrir el archivo csv
    reader = csv.reader(csvfile, delimiter=',') # 2. Leer todo el archivo csv
    header = next(reader) # Leer la primera linea del archivo csv, titulos de las columnas.
    print(header) # Imprimir los titulos de las columnas
    data = [] # Lista para almacenar los diccionarios
    
    for row in reader:
      Iterable = zip(header, row) # Unir las listas los titulos con los datos de los regitros
      #print(list(Iterable)) # Imprimir los los titulos con los datos en forma de lista y tuplas
      country_dict = {key: value for key, value in Iterable} # Diccionario comprehension, transformar el registro en dicc
      #print(country_dict) # Imprimir el diccionario
      data.append(country_dict) # Agregar el diccionario a la lista data
    return data # Retornar la lista data
      #print('***' * 5)
      #print(row)
pass
    

if __name__ == '__main__': # Para ejecutar como script, lo que hay aqui adentro no se ejecuta cuando se importa como modulo
  data = read_csv("data.csv") # Ejecutar la funcion read_csv()
  print(data) # Imprimir el primer registro de la lista data
  #print(data[0]) # Imprimir el primer registro de la lista data
    
  