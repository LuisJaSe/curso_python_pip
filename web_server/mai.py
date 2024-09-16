# se importa el modulo que habiuamos creado en store
import store

# importar fastapi
#from fastapi import FastAPI


# Se crea una funcion para ejecutar la funcion del modulo del store
def run():
    store.get_categories()

# Se utiliza este bloque para ejecutar la funcion del modulo del store como script
if __name__ == '__main__':
    run()