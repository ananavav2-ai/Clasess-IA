import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(
    page_title="IA en la Psicología Educativa",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ESTILOS
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:1rem;
}

/* Contenedor principal */
.content-container{
    max-width:1000px;
    margin:auto;
}

/* Texto */
.title-text{
    font-family:'Helvetica Neue',sans-serif;
    font-weight:700;
    color:#1a1a1a;
}

.body-text{
    font-family:'Georgia',serif;
    font-size:1.15rem;
    line-height:1.7;
    color:#333;
}

/* Botones */
.stButton>button{
    border-radius:40px;
    padding:8px 20px;
    border:1px solid #e0e0e0;
    background:white;
}

.stButton>button:hover{
    border-color:black;
}

</style>
""", unsafe_allow_html=True)


# NAVEGACIÓN
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1


# CONTENIDO (más información agregada)
sections = [

{
"titulo":"La Inteligencia Artificial en el Aula",
"sub":"¿Aliada o desafío para la psicología educativa?",
"contenido":"""
La inteligencia artificial está transformando rápidamente el campo educativo. 
Lo que hace algunos años parecía una herramienta futurista, hoy forma parte de 
muchas plataformas educativas utilizadas en escuelas y universidades.

Desde la psicología educativa, la IA abre nuevas posibilidades para comprender 
cómo aprenden los estudiantes, cómo se motivan y cuáles son las dificultades 
que enfrentan durante su proceso de aprendizaje.

Además, permite analizar grandes cantidades de datos sobre el rendimiento 
académico y los estilos de aprendizaje, lo que puede ayudar a diseñar 
estrategias educativas más eficaces y centradas en el estudiante.
""",
"img":"https://img.freepik.com/free-vector/human-brain-with-digital-circuit-lines-background_1017-30358.jpg"
},

{
"titulo":"¿Qué es realmente la Inteligencia Artificial?",
"contenido":"""
La inteligencia artificial es un conjunto de tecnologías capaces de procesar 
información, identificar patrones y tomar decisiones basadas en datos.

A diferencia de lo que muchas personas imaginan, la IA no es un robot con 
conciencia o emociones. En realidad, se trata de sistemas computacionales 
diseñados para simular ciertas capacidades humanas como el aprendizaje, 
la resolución de problemas y la toma de decisiones.

En educación, estas tecnologías pueden analizar el comportamiento de los 
estudiantes dentro de plataformas digitales para detectar dificultades, 
adaptar ejercicios y ofrecer recomendaciones personalizadas.
""",
"img":"https://img.freepik.com/free-photo/representation-user-experience-interface-design_23-2150165981.jpg"
},

{
"titulo":"Aprendizaje Personalizado",
"contenido":"""
Uno de los mayores aportes de la inteligencia artificial en la educación es 
la posibilidad de ofrecer aprendizaje personalizado.

Tradicionalmente, todos los estudiantes seguían el mismo ritmo dentro del aula. 
Sin embargo, cada estudiante aprende de manera distinta. Algunos necesitan 
más tiempo para comprender ciertos conceptos, mientras que otros avanzan 
más rápido.

Los sistemas educativos basados en IA pueden identificar estas diferencias 
y adaptar los contenidos según las necesidades de cada estudiante. Esto 
permite ofrecer ejercicios adicionales, explicaciones alternativas o 
actividades de refuerzo cuando un alumno presenta dificultades.
""",
"img":"https://img.freepik.com/free-vector/personalized-learning-concept-illustration_114360-7053.jpg"
},

{
"titulo":"Inclusión y apoyo al docente",
"contenido":"""
La inteligencia artificial también puede contribuir a mejorar la inclusión 
educativa. Algunos sistemas permiten adaptar materiales para estudiantes 
con necesidades educativas especiales, como dificultades de lectura, 
problemas de atención o discapacidades visuales.

Además, la IA puede apoyar a los docentes analizando datos sobre el progreso 
de los estudiantes. Esto permite identificar patrones de aprendizaje, detectar 
dificultades tempranas y tomar decisiones pedagógicas más informadas.

En este sentido, la tecnología no reemplaza al docente, sino que funciona 
como una herramienta que amplía sus capacidades dentro del aula.
""",
"img":"https://img.freepik.com/free-vector/teacher-concept-illustration_114360-1638.jpg"
},

{
"titulo":"Señales de alerta: ética y privacidad",
"contenido":"""
A pesar de sus beneficios, el uso de inteligencia artificial en educación 
también plantea desafíos importantes.

Uno de los principales problemas es la privacidad de los datos. Las 
plataformas educativas recopilan información sobre el comportamiento 
de los estudiantes, su rendimiento y sus hábitos de estudio.

Por ello es fundamental garantizar que estos datos estén protegidos 
y que se utilicen de manera responsable.

Otro riesgo es la presencia de sesgos en los algoritmos. Si los sistemas 
se entrenan con datos incompletos o sesgados, podrían generar decisiones 
injustas o discriminatorias.
""",
"img":"https://img.freepik.com/free-vector/data-protection-concept-illustration_114360-1011.jpg"
},

{
"titulo":"El valor del factor humano",
"contenido":"""
Aunque la inteligencia artificial puede ofrecer múltiples herramientas 
educativas, es importante recordar que la educación es un proceso profundamente 
humano.

El vínculo emocional entre docentes y estudiantes, la empatía, la motivación 
y el acompañamiento psicológico no pueden ser reemplazados por una máquina.

Por esta razón, el verdadero desafío consiste en utilizar la tecnología 
como una herramienta que fortalezca el proceso educativo sin sustituir 
la interacción humana que es esencial para el aprendizaje.
""",
"img":"https://img.freepik.com/free-vector/high-five-concept-illustration_114360-1929.jpg"
},

{
"titulo":"El futuro de la educación",
"contenido":"""
El futuro de la educación probablemente combinará herramientas tecnológicas 
avanzadas con enfoques pedagógicos centrados en el desarrollo humano.

La inteligencia artificial puede ayudar a crear entornos educativos más 
flexibles, personalizados e inclusivos. Sin embargo, su implementación 
debe realizarse con responsabilidad, considerando aspectos éticos, sociales 
y psicológicos.

El objetivo final no es reemplazar a los docentes, sino construir sistemas 
educativos donde la tecnología esté al servicio del desarrollo humano y del 
aprendizaje significativo.
""",
"img":"https://img.freepik.com/free-vector/future-concept-illustration_114360-5394.jpg"
}

]

current = sections[st.session_state.step]


# BOTONES ARRIBA DERECHA
nav1, nav2, nav3 = st.columns([6,1,1])

with nav2:
    if st.session_state.step > 0:
        st.button("←", on_click=prev_step)

with nav3:
    if st.session_state.step < len(sections)-1:
        st.button("→", on_click=next_step)
    else:
        if st.button("✓"):
            st.balloons()


# CONTENIDO
st.markdown('<div class="content-container">', unsafe_allow_html=True)

st.markdown(f"<h1 class='title-text'>{current['titulo']}</h1>", unsafe_allow_html=True)

if "sub" in current:
    st.markdown(f"### {current['sub']}")

if "img" in current:
    st.image(current["img"], width=450)

st.markdown(f"<p class='body-text'>{current['contenido']}</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# REFERENCIAS
if st.session_state.step == len(sections)-1:
    with st.expander("Referencias"):
        st.write("""
        Azevedo (2024)  
        Chiu (2023)  
        García-Peñalvo (2024)
        """)
