import random  # Importamos la librería random

# Variables del juego
options = ('piedra', 'papel', 'tijera')  # Tupla de opciones
numero_de_juegos = 5
ganados_usuario = 0
ganados_computadora = 0

# Bucle principal del juego
for intentos in range(numero_de_juegos):
    
    # Opción del usuario
    Opcion_usuario = input("Elige piedra, papel o tijera: ").lower()
    
    # Validación de la opción del usuario
    while Opcion_usuario not in options:
        Opcion_usuario = input("Elige una opción válida (piedra, papel o tijera): ").lower()
    
    # Opción de la computadora
    Opcion_computadora = random.choice(options)
    print(f"La computadora eligió: {Opcion_computadora}")
    print(f"El usuario eligió: {Opcion_usuario}")

    # Lógica para decidir el ganador de la ronda
    if Opcion_usuario == Opcion_computadora:
        print(f"Empate, ambos eligieron {Opcion_computadora}")
    
    elif (Opcion_usuario == "piedra" and Opcion_computadora == "tijera") or \
         (Opcion_usuario == "tijera" and Opcion_computadora == "papel") or \
         (Opcion_usuario == "papel" and Opcion_computadora == "piedra"):
        print(f"Ganaste, {Opcion_usuario} le gana a {Opcion_computadora}")
        ganados_usuario += 1
    
    else:
        print(f"Perdiste, {Opcion_computadora} le gana a {Opcion_usuario}")
        ganados_computadora += 1
    
    print(f"Puntuación - Usuario: {ganados_usuario} | Computadora: {ganados_computadora}\n")

# Resultado final del juego
if ganados_usuario > ganados_computadora:
    print("El juego terminó en victoria para el usuario")
elif ganados_computadora > ganados_usuario:
    print("El juego terminó en victoria para la computadora")
else:
    print("El juego terminó en empate")
