# Funcion para calcular la poblacion de un pais
def poblacion(pais):
  poblacion_dict = {
    '2022': int(pais['2022 Population']),
    '2020': int(pais['2020 Population']),
    '2015': int(pais['2015 Population']),
    '2010': int(pais['2010 Population']),
    '2000': int(pais['2000 Population']),
    '1990': int(pais['1990 Population']),
    '1980': int(pais['1980 Population']),
    '1970': int(pais['1970 Population'])
  }
  #return keys, values
  label = poblacion_dict.keys()
  values = poblacion_dict.values()
  return label, values
pass



# Funcion dentro de modulos para luego ser utilizada en otros modulos
def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result
pass