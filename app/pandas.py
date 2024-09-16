# Importar el modulo mod, debe estar en la misma carpeta ----------------------------
import mod
import read_csv
import graficas
import pandas as pd


# Usando pandas ----------------------------------------------
def run_pandas():
  df = pd.read_csv('data.csv') # Leer datos
  df = df[df['Continent'] == 'South America'] # Filtrando los datos
  
  countries = df['Country/Territory'].values # Obtendiendo los datos
  percentages = df['World Population Percentage'].values # Obteniendo los datos
  
  graficas.generate_pie_chart(countries, percentages)


  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)

  result = mod.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = mod.get_population(country)
    graficas.generate_bar_chart(country['Country/Territory'], labels, values)
    
pass



# PARA PODER EJECUTAR ESTE ARCHIVO como escript tambien, SE DEBE EJECUTAR EL ARCHIVO main.py--------
if __name__ == "__main__":
  run_pandas()