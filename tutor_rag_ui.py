# tutor_rag_ui.py

import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# ================================
# CONFIGURACIÓN
# ================================

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Configura GEMINI_API_KEY en tu archivo .env")
    st.stop()

client = genai.Client(api_key=api_key)

# ================================
# BASE DE CONOCIMIENTO (RAG SIMPLE)
# ================================

BASE_CONOCIMIENTO = """
La normalización en bases de datos es el proceso de organizar los datos
para reducir redundancia y mejorar la integridad de la información.

Primera Forma Normal (1FN):
Una tabla está en 1FN si todos sus atributos contienen valores atómicos
y no existen grupos repetitivos.

Segunda Forma Normal (2FN):
Una tabla está en 2FN si está en 1FN y todos los atributos no clave
dependen completamente de la clave primaria.

Tercera Forma Normal (3FN):
Una tabla está en 3FN si está en 2FN y no existen dependencias transitivas.
"""

# ================================
# SYSTEM PROMPT (DISEÑO DE PROMPTS)
# ================================

SYSTEM_PROMPT = """
<ROL>
Eres un Tutor Académico experto en Bases de Datos.
</ROL>

<OBJETIVO>
Guiar al estudiante para que comprenda conceptos de bases de datos
usando preguntas socráticas sin dar la respuesta directa.
</OBJETIVO>

<REGLAS>
- Nunca des la respuesta directa.
- Usa preguntas que ayuden al estudiante a razonar.
- Usa únicamente el CONTEXTO proporcionado.
- Si la pregunta está fuera del contexto, indícalo.
</REGLAS>

<FORMATO_RESPUESTA>
Responde SIEMPRE en formato Markdown usando:

### Reflexión
explicación breve

### Preguntas guía
- pregunta 1
- pregunta 2
- pregunta 3
</FORMATO_RESPUESTA>

<FEW_SHOT>

Ejemplo 1:

Pregunta:
¿Qué es la primera forma normal?

Respuesta esperada:

### Reflexión
En una tabla puede ocurrir que un campo tenga varios valores.

### Preguntas guía
- ¿Qué pasaría si un campo contiene varios datos?
- ¿Cómo podrías separar esos valores?
- ¿Crees que cada celda debería tener un solo valor?


Ejemplo 2:

Pregunta:
¿Por qué se normalizan las bases de datos?

Respuesta esperada:

### Reflexión
Cuando la información se repite muchas veces pueden aparecer errores.

### Preguntas guía
- ¿Qué ocurriría si cambias un dato en solo una fila?
- ¿Qué problemas causa la redundancia?
- ¿Cómo podrías dividir la información en varias tablas?

</FEW_SHOT>
"""

# ================================
# UI
# ================================

st.set_page_config(page_title="Tutor RAG BD", page_icon="🤖")

st.title("🤖 Tutor Académico con RAG")
st.write("Asistente basado en material de Bases de Datos")

# ================================
# MEMORIA
# ================================

if "historial" not in st.session_state:
    st.session_state.historial = []

for msg in st.session_state.historial:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ================================
# INPUT CHAT
# ================================

if prompt := st.chat_input("Pregunta sobre Bases de Datos..."):

    st.chat_message("user").markdown(prompt)

    st.session_state.historial.append({
        "role": "user",
        "content": prompt
    })

    # ================================
    # PROMPT CON DELIMITADORES
    # ================================

    prompt_completo = f"""
<SYSTEM>
{SYSTEM_PROMPT}
</SYSTEM>

<CONTEXTO>
\"\"\" 
{BASE_CONOCIMIENTO}
\"\"\"
</CONTEXTO>

<PREGUNTA>
{prompt}
</PREGUNTA>
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_completo
    )

    respuesta = response.text

    with st.chat_message("assistant"):
        st.markdown(respuesta)

    st.session_state.historial.append({
        "role": "assistant",
        "content": respuesta
    })

# ================================
# HISTORIAL
# ================================

if st.button("Mostrar historial"):

    texto = ""

    for msg in st.session_state.historial:
        rol = "Usuario" if msg["role"] == "user" else "Asistente"
        texto += f"{rol}: {msg['content']}\n\n"

    st.text_area("Conversación", texto, height=300)
