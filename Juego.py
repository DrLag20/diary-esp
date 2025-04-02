from VoiceREC import speech
from random import choice
import random
import time

niveles = {

"facil": ["agenda", "ami", "souris"],
"intermedio": ["ordinateur", "algorithme", "développeur"],
"dificil": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
}

def play_game(level):
    palabras = niveles.get(level, [])
    if not palabras:
        print("No has seleccionado ningún nivel.")
        return
    
    puntuacion = 0

    for i in range(len(palabras)):
        palabra_random = choice(palabras)
        print(palabra_random)
        palabra_reconocida = speech()
        print(palabra_reconocida)
        if palabra_random == palabra_reconocida:
            print("Has pronunciado la palabra correctamente.")
            puntuacion + 1

        else:
            print("Mala pronunciaciación, intenta otra vez.")

    print("Juego terminado, tus puntos son:", puntuacion)
    Nivel_dificultad = input("Niveles")

    play_game(Nivel_dificultad)
