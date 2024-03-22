# Juego de Piedra papel tijera

# Complementos o dependiencias ---------------------------------------------------------
import random  #Importamos la libreria random

# Variables del juego ------------------------------------------------------------------
options = ('piedra', 'papel', 'tijera')  # Tupla de opciones
Opcion_usuario = input("Elige piedra, papel o tijera: ")
Opcion_usuario = Opcion_usuario.lower()

# Validacion de la opcion del usuario en la tupla de opciones----------------------------------------
#if not Opcion_usuario in options:
#print('Esa opcion no es valida')
while Opcion_usuario not in options:
  Opcion_usuario = input("Elige piedra, papel o tijera: ")
  Opcion_usuario = Opcion_usuario.lower()

# Opcion de la computadora ------------------------------------------------------------------------
Numero_aleatorio = random.randint(1, 3)
#print(Numero_aleatorio)

if Numero_aleatorio == 1:
  #Opcion_computadora = "piedra"
  Opcion_computadora = options[0]  #Usando la tupla
  print(f"La computadora eligió {Opcion_computadora}")

elif Numero_aleatorio == 2:
  #Opcion_computadora = "papel"
  Opcion_computadora = options[1]
  print(f"La computadora eligió {Opcion_computadora}")

elif Numero_aleatorio == 3:
  #Opcion_computadora = "tijera"
  Opcion_computadora = options[2]
  print(f"La computadora eligió {Opcion_computadora}")

else:
  print("La computadora no eligio ninguna opcion")

print('El usuario eligio: ', Opcion_usuario)

# Bloque o logica para ganar el juego ---------------------------------------------------------
# Contadores del juego o intentos
numero_de_juegos = 5
intentos = 0
ganados_usuario = 0
ganados_computadora = 0

while intentos <= numero_de_juegos:

  if Opcion_usuario == Opcion_computadora:
    print(f"Empate, ambos eligieron {Opcion_computadora}")

  elif Opcion_usuario == "piedra" and Opcion_computadora == "tijera":
    print("Ganaste,piedra le gana a tijera")
    ganados_usuario += 1

  elif Opcion_usuario == "piedra" and Opcion_computadora == "papel":
    print("Perdiste,papel le gana a piedra")
    ganados_computadora += 1

  elif Opcion_usuario == "tijera" and Opcion_computadora == "papel":
    print("Ganaste,tijera le gana a papel")
    ganados_usuario += 1

  elif Opcion_usuario == "tijera" and Opcion_computadora == "piedra":
    print("Perdiste,piedra le gana a tijera")
    ganados_computadora += 1

  elif Opcion_usuario == "papel" and Opcion_computadora == "piedra":
    print("Ganaste,papel le gana a piedra")
    ganados_usuario += 1

  elif Opcion_usuario == "papel" and Opcion_computadora == "tijera":
    print("Perdiste,tijera le gana a papel")
    ganados_computadora += 1

  else:
    print("El usuario eligio una opcion no valida")

  intentos += 1
  print(f"El usuario lleva {ganados_usuario} y la computadora {ganados_computadora}")



# Bloque o logica para ganar el juego -----------------------------------------------------
if ganados_usuario == ganados_computadora:
  print("El juego termino en empate")
  
elif ganados_usuario > ganados_computadora:
  print("El juego termino en victoria para el usuario")

else: print("El juego termino en victoria para la computadora")
