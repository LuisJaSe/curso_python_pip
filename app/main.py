# Importar el modulo mod, debe estar en la misma carpeta ----------------------------
import mod
import read_csv
import graficas


# Llamar a la funcion poblacion() del modulo mod----------------------------------------------
def run():
  data = read_csv.read_csv("data.csv")
  country = input('Type Country => ')
  
  result = mod.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = mod.poblacion(country)

    graficas.generate_bar_chart(labels, values)
    
pass



# PARA PODER EJECUTAR ESTE ARCHIVO como escript tambien, SE DEBE EJECUTAR EL ARCHIVO main.py--------
if __name__ == "__main__":
  run()