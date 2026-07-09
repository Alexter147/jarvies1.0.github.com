# brain.py
# Este es el "cerebro" del asistente: decide qué responder ante cada comando.
#
# Incluye la personalidad de Jarvies (inspirada en JARVIS de Iron Man) como
# system prompt, lista para conectar con un modelo real. Mientras tanto,
# las respuestas de ejemplo ya siguen ese mismo tono.

PERSONALIDAD = """
Eres Jarvies, un asistente de inteligencia artificial inspirado en JARVIS de Iron Man.

Reglas de personalidad y estilo:
- Eres respetuoso y formal, pero cercano. Te diriges al usuario como "señor" con
  moderación (no en cada frase, para no sonar repetitivo).
- Eres rápido, directo y eficiente. Evita rodeos, relleno o disculpas innecesarias.
- Respondes con precisión técnica cuando corresponde, pero en lenguaje claro.
- Cometes el mínimo error posible: si no tienes un dato con certeza, lo dices
  explícitamente en lugar de inventarlo.
- Mantienes un tono sereno y con ligera elegancia británica, nunca informal ni efusivo.
- Confirmas brevemente las acciones antes o después de realizarlas.
- No usas emojis ni exclamaciones exageradas.
- Tus respuestas se leen en voz alta: sé breve y ve al grano.
"""


def procesar_comando(texto: str) -> str:
    """
    Recibe el texto reconocido del usuario y devuelve la respuesta del asistente.
    Punto de extensión principal: aquí luego conectaremos la llamada al modelo AI,
    pasando PERSONALIDAD como system prompt.
    """
    texto_normalizado = texto.lower().strip()

    if not texto_normalizado:
        return "No le escuché bien, ¿puede repetirlo, señor?"

    if "hola" in texto_normalizado:
        return "Buenas, señor. ¿En qué puedo asistirle?"

    if "hora" in texto_normalizado:
        from datetime import datetime
        ahora = datetime.now().strftime("%H:%M")
        return f"Son las {ahora}, señor."

    if any(p in texto_normalizado for p in ["adiós", "adios", "apágate", "apagate"]):
        return "__SALIR__"  # señal especial para terminar el programa

    # --- AQUÍ SE CONECTARÁ LA LLAMADA A LA IA (Claude API u otro modelo) ---
    # Ejemplo futuro:
    # respuesta = llamar_modelo_ia(texto_normalizado, system_prompt=PERSONALIDAD)
    # return respuesta

    return f"Procesado, señor. Recibí: '{texto}'. Aún no tengo un modelo de lenguaje conectado para responder esto con precisión."
