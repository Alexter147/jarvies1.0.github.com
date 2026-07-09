# voice_input.py
# Encargado de escuchar el micrófono y convertir voz a texto.

import speech_recognition as sr
import config


class EscuchaVoz:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microfono = sr.Microphone()
        if config.UMBRAL_ENERGIA is not None:
            self.recognizer.energy_threshold = config.UMBRAL_ENERGIA
        self.recognizer.dynamic_energy_threshold = True

        # Calibración inicial de ruido ambiente
        with self.microfono as source:
            print("[voice_input] Calibrando ruido ambiente...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

    def escuchar_wake_word(self):
        """
        Escucha continuamente hasta detectar la wake word.
        Devuelve True cuando la detecta (bloqueante).
        """
        with self.microfono as source:
            while True:
                try:
                    audio = self.recognizer.listen(source, phrase_time_limit=3)
                    texto = self.recognizer.recognize_google(
                        audio, language=config.IDIOMA_RECONOCIMIENTO
                    ).lower()
                    if config.WAKE_WORD.lower() in texto:
                        return True
                except sr.UnknownValueError:
                    continue  # no se entendió nada, seguir escuchando
                except sr.RequestError as e:
                    print(f"[voice_input] Error de conexión con el servicio de voz: {e}")
                    continue

    def escuchar_comando(self, timeout=None):
        """
        Escucha un solo comando después de la wake word.
        Devuelve el texto reconocido o None si no entendió nada.
        """
        timeout = timeout or config.TIEMPO_ESPERA_COMANDO
        with self.microfono as source:
            try:
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=8)
                texto = self.recognizer.recognize_google(
                    audio, language=config.IDIOMA_RECONOCIMIENTO
                )
                return texto
            except sr.WaitTimeoutError:
                print("[voice_input] Tiempo de espera agotado, no se recibió comando.")
                return None
            except sr.UnknownValueError:
                print("[voice_input] No se entendió el comando.")
                return None
            except sr.RequestError as e:
                print(f"[voice_input] Error de conexión con el servicio de voz: {e}")
                return None
