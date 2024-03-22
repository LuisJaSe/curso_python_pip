import random

options = ("piedra", "papel", "tijera")

try:
  Opcion_usuario = input("Elige piedra, papel o tijera: ")
  Opcion_usuario = Opcion_usuario.lower()
except ValueError:
  print("No has introducido una opción válida.")
  #continue

Numero_aleatorio = random.randint(0, len(options) - 1)
Opcion_computadora = options[Numero_aleatorio]
print(f"La computadora eligió {Opcion_computadora}")

ganancias = {
    "piedra": "tijera",
    "papel": "piedra",
    "tijera": "papel"
}

numero_de_juegos = 5
intentos = 0
ganados_usuario = 0
ganados_computadora = 0

while intentos <= numero_de_juegos:
  if Opcion_usuario == Opcion_computadora:
    print(f"Empate, ambos eligieron {Opcion_computadora}")
  else:
    if ganancias[Opcion_usuario] == Opcion_computadora:
      print(f"Ganaste, {Opcion_usuario} le gana a {Opcion_computadora}")
      ganados_usuario += 1
    else:
      print(f"Perdiste, {Opcion_computadora} le gana a {Opcion_usuario}")
      ganados_computadora += 1

  intentos += 1
  print(f"Llevas {ganados_usuario} victorias y la computadora {ganados_computadora}")

if ganados_usuario == ganados_computadora:
  print("El juego terminó en empate.")
