# main.py
# Punto de entrada del asistente de voz.
# Flujo: escucha wake word -> escucha comando -> procesa (brain.py) -> responde (voz).

import random
import config
from voice_input import EscuchaVoz
from voice_output import VozAsistente
from brain import procesar_comando


def main():
    oido = EscuchaVoz()
    voz = VozAsistente()

    print(f"[main] Asistente listo. Di '{config.WAKE_WORD}' para activarlo.")

    while True:
        oido.escuchar_wake_word()
        frase = random.choice(config.FRASES_ACTIVACION)
        voz.hablar(frase)

        comando = oido.escuchar_comando()
        if comando is None:
            voz.hablar("No recibí ningún comando.")
            continue

        print(f"[main] Comando detectado: {comando}")
        respuesta = procesar_comando(comando)

        if respuesta == "__SALIR__":
            voz.hablar("Hasta luego.")
            break

        voz.hablar(respuesta)


if __name__ == "__main__":
    main()
