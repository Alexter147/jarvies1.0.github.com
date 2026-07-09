# voice_output.py
# Encargado de convertir texto a voz (TTS).

import pyttsx3


class VozAsistente:
    def __init__(self, velocidad=175, volumen=1.0, voz_id=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", velocidad)
        self.engine.setProperty("volume", volumen)

        if voz_id:
            self.engine.setProperty("voice", voz_id)
        else:
            # Intenta seleccionar automáticamente una voz en español si existe
            for voz in self.engine.getProperty("voices"):
                if "spanish" in voz.name.lower() or "es" in voz.id.lower():
                    self.engine.setProperty("voice", voz.id)
                    break

    def hablar(self, texto: str):
        print(f"[Asistente]: {texto}")
        self.engine.say(texto)
        self.engine.runAndWait()

    def listar_voces_disponibles(self):
        """Utilidad para ver qué voces tienes instaladas en tu sistema."""
        voces = self.engine.getProperty("voices")
        for v in voces:
            print(f"ID: {v.id} | Nombre: {v.name} | Idiomas: {v.languages}")
