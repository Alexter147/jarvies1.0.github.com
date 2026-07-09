# Asistente de Voz — Base

Estructura base de un asistente de IA que se activa por comando de voz (wake word).

## Estructura del proyecto

```
asistente_ia/
├── main.py           # Punto de entrada, orquesta el flujo
├── config.py          # Configuración (wake word, idioma, tiempos)
├── voice_input.py      # Captura de micrófono + reconocimiento de voz
├── voice_output.py     # Texto a voz (TTS)
├── brain.py            # Lógica de respuesta (aquí se conectará la IA con tono/personalidad)
└── requirements.txt
```

## Instalación

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Nota: `PyAudio` a veces requiere dependencias del sistema:
- **Windows**: normalmente instala sin problema.
- **macOS**: `brew install portaudio` antes de `pip install pyaudio`.
- **Linux**: `sudo apt-get install python3-pyaudio portaudio19-dev`.

## Uso

```bash
python main.py
```

1. El asistente queda escuchando en segundo plano.
2. Di la palabra de activación (por defecto `"asistente"`, configurable en `config.py`).
3. El asistente responde con una frase corta y espera tu comando.
4. Da tu comando por voz; el asistente lo procesa en `brain.py` y responde por voz.
5. Di "adiós" o "apágate" para terminar el programa.

## Próximo paso

`brain.py` tiene un punto de extensión marcado donde se conectará el modelo de IA
(por ejemplo la API de Claude) usando un **system prompt** que defina el tono de voz
y la forma de responder que tú definas. Cuando me pases esas indicaciones,
actualizamos ese archivo para darle personalidad real al asistente.
