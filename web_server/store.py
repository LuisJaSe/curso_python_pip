# Importando libreria requests
import requests

# creando una funcion para consumir la API de categorias de platzi usando la libreria requests
def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) # status de la API
    print(r.text) # text o contenido de la API
    print(type(r.text)) # type de la API (texto)
    categories = r.json() # para transformarlo en lista
    for category in categories:
        print(category['name']) # solo se imprime la categoryclear
pass
        
#print("hola")


if __name__ == '__main__':
    get_categories()