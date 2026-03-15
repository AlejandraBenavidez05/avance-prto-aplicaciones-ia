# Descripción del Avance 1 del Proyecto

En este primer avance del proyecto se desarrolló un prototipo de asistente inteligente enfocado en el apoyo académico en el área de Bases de Datos. El sistema fue implementado como una aplicación local utilizando Python y la biblioteca Streamlit, lo que permite interactuar con el asistente mediante una interfaz tipo chat directamente desde el navegador, preservando la privacidad de los datos.

El asistente se diseñó siguiendo principios de **Prompt Engineering**, donde se estructuraron instrucciones del sistema (System Prompt) que definen claramente el rol, el objetivo y las reglas de comportamiento del modelo. En este caso, el asistente actúa como un **tutor académico socrático**, guiando al estudiante mediante preguntas reflexivas para que construya su propio conocimiento en temas como SQL, normalización y conceptos fundamentales de bases de datos, evitando proporcionar respuestas directas.

Adicionalmente, se implementó la técnica de **Few-Shot Prompting**, incluyendo ejemplos de interacción dentro del prompt para orientar al modelo hacia un formato específico de respuesta en Markdown. Estos ejemplos permiten al modelo comprender el estilo pedagógico esperado, basado en reflexiones breves seguidas de preguntas guía que fomentan el razonamiento del estudiante.

El sistema también incorpora **estrategias de delimitadores**, utilizando etiquetas estructuradas (como `<SYSTEM>`, `<CONTEXTO>` y `<PREGUNTA>`) junto con delimitadores de texto para separar claramente las instrucciones del modelo, el contexto de conocimiento y la consulta del usuario. Esta organización facilita el control del comportamiento del modelo y simula un enfoque inicial de **Retrieval-Augmented Generation (RAG)**, donde el asistente responde basándose únicamente en una base de conocimiento específica incluida en el sistema.

Finalmente, se implementó una memoria de conversación que permite mantener el historial del chat durante la sesión, mejorando la continuidad de la interacción. Este avance establece la base para futuras mejoras del sistema, como la integración de documentos externos, bases vectoriales y agentes inteligentes para realizar consultas más complejas sobre la base de conocimientos.


## Requisitos de Instalación Antes de ejecutar el script:

1. *Python: Asegúrese de tener Python3 instalado en su sistema.

Puede descargarlo desde [python.org](https://www.python.org/).Puede verificar la versión de Python instalada en el sistema utilizando el siguiente comando en la línea de comandos o terminal, dependiendo de tu sistema operativo:

*Para Windows:* 
    
```bash
python --version
python -V 
```
  
*Para Linux o macOS:*
     
```bash
python3 --version
python3 -V 
```

Estos comandos deberían mostrar la versión de Python instalada en tu sistema.
Asegúrate de tener Python instalado y configurado en tu PATH para que estos comandos funcionen correctamente. 

2. *Variables de Entorno de google AI Studio que se deben configurar:*  Antes de ejecutar los scripts .py asegúrese de configurar su archivo .env con su token de google AI Studio: 

      - `GEMINI_API_KEY`: Token/clave del API de Gemini.

 Esta variable es esencial para la integración con el API google gemini AI. Es importante configurarla correctamente para asegurar el funcionamiento adecuado del scripts. Si no dispone de un token de usuario en esta herramienta, puede consultar haciendo click en el botón de  [crea o visualiaza una clave de API de Gemini](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419) 

## Ejecución de los scripts

Para ejecutar los scripts, debe seguir estos pasos:

1. *Clonar Repositorio:*     
a. Comience clonando el repositorio en su máquina local mediante el siguiente comando:
```bash  
git clone https://github.com/AlejandraBenavidez05/taller-base-de-datos.git
```
   

b. Ubiquese en el directorio gemini-api-activity/

2. *Crear entorno Virtual (recomendado):*
Se recomienda utilizar un entorno virtual para evitar conflictos con las dependencias de otros proyectos.   
 
a. Puede crear un entorno virtual en el directorio del proyecto con el siguiente comando:

```bash
python3 -m venv venv 
```
```bash
python -m venv venv 
``` 
```bash
py -m venv venv 
```

      
b. Para activar el entorno virtual ejecute el comando adecuado según su sistema operativo.

  - En Windows (cmd): `venv\Scripts\activate`

  - En Windows (PowerShell): `venv\Scripts\activate`

  - En macOS y Linux: `source ./venv/bin/activate`

3. *Instalación de Dependencias:*

 Instale las dependencias del proyecto utilizando el siguiente comando:
 ```bash
pip install -r requirements.txt
```
Esto instalará todas las bibliotecas necesarias para ejecutar el script. 

4. *Ejecución del script de python:* 

Para ejecutar los scripts, utilice el siguiente comando:
```bash
streamlit run tutor_rag_ui.py
```

