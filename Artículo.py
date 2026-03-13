import streamlit as st
import pandas as pd

# 1. Configuración de la página y Estilo Minimalista
st.set_page_config(page_title="IA en la Psicología Educativa", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* Ocultar elementos innecesarios para diseño limpio */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Contenedor principal que simula el viewport completo */
    .viewport-container {
        height: 80vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 2rem;
    }
    
    /* Tipografías */
    .title-text { font-family: 'Helvetica Neue', sans-serif; font-weight: 700; color: #1a1a1a; }
    .body-text { font-family: 'Georgia', serif; font-size: 1.2rem; line-height: 1.6; color: #333; max-width: 800px; margin: auto; }
    
    /* Botones de navegación */
    .stButton>button {
        border-radius: 50px;
        padding: 10px 25px;
        border: 1px solid #e0e0e0;
        background-color: white;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        border-color: #000;
        background-color: #f9f9f9;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Gestión de navegación (State)
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step(): st.session_state.step += 1
def prev_step(): st.session_state.step -= 1

# 3. Definición de las Secciones del Artículo [cite: 44]
sections = [
    {
        "titulo": "La Inteligencia Artificial en el Aula",
        "sub": "¿Aliada o Desafío para la Psicología Educativa? [cite: 48]",
        "contenido": "La educación está viviendo una metamorfosis. Lo que antes parecía ciencia ficción es hoy una realidad cotidiana. [cite: 49]",
        "img": "https://img.freepik.com/free-vector/human-brain-with-digital-circuit-lines-background_1017-30358.jpg"
    },
    {
        "titulo": "¿Qué es realmente la IA?",
        "contenido": "No es un robot con sentimientos, sino un sistema capaz de procesar cantidades enormes de información para resolver problemas, de forma similar a como lo haría un humano. [cite: 52]",
        "img": "https://img.freepik.com/free-photo/representation-user-experience-interface-design_23-2150165981.jpg"
    },
    {
        "titulo": "Cambios en la Escuela: Personalización",
        "contenido": "Aprendizaje Personalizado: Ya no todos los niños tienen que ir al mismo ritmo. La IA detecta si un estudiante se atasca y ofrece refuerzo específico. [cite: 58, 59]",
        "img": "https://img.freepik.com/free-vector/personalized-learning-concept-illustration_114360-7053.jpg"
    },
    {
        "titulo": "Cambios en la Escuela: Inclusión y Docencia",
        "contenido": "Inclusión Real: Adaptación de materiales para necesidades especiales. [cite: 60] El Maestro 'Aumentado': El docente usa datos para entender el apoyo emocional que necesita cada alumno. [cite: 61]",
        "img": "https://img.freepik.com/free-vector/teacher-concept-illustration_114360-1638.jpg"
    },
    {
        "titulo": "Señales de Alerta: Ética y Privacidad",
        "contenido": "Privacidad de Datos y Sesgos: Es vital asegurar que la información personal esté protegida y que los algoritmos no discriminen. [cite: 64, 66]",
        "img": "https://img.freepik.com/free-vector/data-protection-concept-illustration_114360-1011.jpg"
    },
    {
        "titulo": "Integridad y el Toque Humano",
        "contenido": "El desafío es usar la IA para potenciar la creatividad, no para reemplazar el pensamiento crítico. La IA nunca podrá sustituir el vínculo emocional maestro-alumno. [cite: 67, 69]",
        "img": "https://img.freepik.com/free-vector/high-five-concept-illustration_114360-1929.jpg"
    },
    {
        "titulo": "El Futuro",
        "contenido": "“El futuro del aprendizaje no es solo digital, es ético y humano.” [cite: 40] El objetivo es una tecnología que sirva al ser humano y no al revés. [cite: 72]",
        "img": "https://img.freepik.com/free-vector/future-concept-illustration_114360-5394.jpg"
    }
]

# 4. Renderizado de la Pantalla Actual
current = sections[st.session_state.step]

# Layout de la sección
st.markdown('<div class="viewport-container">', unsafe_allow_html=True)
if "img" in current:
    st.image(current["img"], width=400)
st.markdown(f'<h1 class="title-text">{current["titulo"]}</h1>', unsafe_allow_html=True)
if "sub" in current:
    st.markdown(f'### {current["sub"]}')
st.markdown(f'<p class="body-text">{current["contenido"]}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. Controles de Navegación [cite: 45]
col_prev, col_space, col_next = st.columns([1, 4, 1])

with col_prev:
    if st.session_state.step > 0:
        st.button("← Anterior", on_click=prev_step)

with col_next:
    if st.session_state.step < len(sections) - 1:
        st.button("Siguiente →", on_click=next_step)
    else:
        if st.button("Finalizar"):
            st.balloons()
            st.success("¡Gracias por leer!")

# 6. Mostrar referencias si es el final
if st.session_state.step == len(sections) - 1:
    with st.expander("Ver Referencias Bibliográficas [cite: 73]"):
        st.write("Azevedo (2024), Chiu (2023), García-Peñalvo (2024), entre otros. [cite: 74, 75, 77]")
