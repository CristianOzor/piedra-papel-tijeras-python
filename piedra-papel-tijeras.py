
nombre1 = input("¿Cómo se llama el jugador 1?\n")
nombre2 = input("¿Cómo se llama el jugador 2?\n")

jugador1 = input(f"¡Hola {nombre1}! ¿Qué eliges? ¿Piedra, papel o tijeras?:\n ").lower()
jugador2 = input(f"¡Hola {nombre2}! ¿Qué eliges? ¿Piedra, papel o tijeras?:\n ").lower()


condicion1 = (jugador1 == "piedra" and jugador2 =="tijeras")
condicion2 = (jugador1 == "papel" and jugador2 == "tijeras")
condicion3 = (jugador1 == "tijeras" and jugador2 == "papel")

if jugador1 == jugador2:
    print("¡Ha sido un empate!")

elif (condicion1 or condicion2 or condicion3):
    print(f"¡Ha ganado {nombre1}]!")

else:
    print(f"¡Ha ganado {nombre2}!")




#Otra forma de hacerlo
"""if jugador1 == jugador2:
    print("¡Ha sido un empate!")

elif (jugador1 == "piedra" and jugador2 =="tijeras") or (jugador1 == "papel" and jugador2 == "tijeras") or (jugador1 == "tijeras" and jugador2 == "papel"):
    print(f"¡Ha ganado {nombre1}]!")

else:
    print(f"¡Ha ganado {nombre2}!")"""
    