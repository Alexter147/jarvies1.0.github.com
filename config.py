# config.py
# Configuración central del asistente. Ajusta estos valores según tu preferencia.

# Palabra de activación (wake word). El asistente solo reacciona después de escucharla.
WAKE_WORD = "asistente"

# Idioma para reconocimiento de voz (formato Google Speech API)
IDIOMA_RECONOCIMIENTO = "es-PE"  # Español - Perú (ajústalo a tu región si prefieres)

# Idioma/voz para texto a voz (TTS)
IDIOMA_VOZ = "es"

# Tiempo máximo (segundos) que espera un comando después de detectar el wake word
TIEMPO_ESPERA_COMANDO = 6

# Umbral de energía del micrófono (ajustar según ruido ambiente; None = automático)
UMBRAL_ENERGIA = None

# Frases de confirmación al detectar wake word (se elige una al azar)
FRASES_ACTIVACION = [
    "Dime.",
    "Te escucho.",
    "¿En qué te ayudo?",
]
