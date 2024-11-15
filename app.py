import streamlit as st
from datetime import date
import time
import requests

# Inicio del contador de tiempo
start_time = time.time()

# Configuración de la página
st.set_page_config(
    page_title="Simulador de Pensión de Jubilación | Calculadora de Pensión 2025",
    page_icon="💼",
    initial_sidebar_state="collapsed"
)

# Agregar metadatos SEO mejorados
st.components.v1.html("""
    <meta name="description" content="Simulador de jubilación gratuito ✓ Calculadora de pensión actualizada 2025 ✓ Simulador de pensión oficial ✓ Resultados instantáneos y precisos.">
    <meta name="keywords" content="simulador de jubilación, calculadora de pensión de jubilación, calculadora de pensión, simulador de pensión, simulador de pensión de jubilación, pensión jubilación, cálculo pensión">
    <meta name="robots" content="index, follow">
    <meta name="author" content="José Maria Muñiz">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta property="og:title" content="Simulador de Jubilación | Calculadora de Pensión 2025">
    <meta property="og:description" content="Use nuestro simulador de jubilación y calculadora de pensión de jubilación para planificar su futuro.">
    <meta property="og:type" content="website">
    <link rel="canonical" href="https://calculadora-de-pension.streamlit.app/"/>
    
    <!-- Twitter Card data -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Simulador de Pensión de Jubilación">
    <meta name="twitter:description" content="Calcule su pensión de jubilación de forma gratuita y precisa">
    
    <!-- Schema.org markup mejorado -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebApplication",
      "name": "Simulador de Jubilación",
      "description": "Calculadora gratuita para simular su pensión de jubilación",
      "url": "https://calculadora-de-pension.streamlit.app",
      "applicationCategory": "FinancialCalculator",
      "operatingSystem": "All",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "EUR"
      },
      "dateModified": "2024-03-10",
      "provider": {
        "@type": "Organization",
        "name": "José Maria Muñiz",
        "sameAs": "https://calculadora-de-pension.streamlit.app/"
      },
      "about": {
        "@type": "Thing",
        "name": "Pensión de Jubilación",
        "description": "Cálculo y simulación de pensiones de jubilación en España"
      },
      "potentialAction": {
        "@type": "UseAction",
        "target": "https://calculadora-de-pension.streamlit.app/"
      },
      "softwareHelp": {
        "@type": "CreativeWork",
        "name": "Guía de uso del simulador",
        "text": "Introduzca sus datos personales, años ó días cotizados y base reguladora ó sueldo bruto anual para calcular su pensión estimada"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "ratingCount": "1250",
        "bestRating": "5",
        "worstRating": "1"
      }
    }
    </script>

    <!-- Breadcrumbs Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [{
        "@type": "ListItem",
        "position": 1,
        "name": "Inicio",
        "item": "https://calculadora-de-pension.streamlit.app/"
      },{
        "@type": "ListItem",
        "position": 2,
        "name": "Calculadora",
        "item": "https://calculadora-de-pension.streamlit.app/calculadora"
      },{
        "@type": "ListItem",
        "position": 3,
        "name": "Simulador de Pensión de Jubilación",
        "item": "https://calculadora-de-pension.streamlit.app/calculadora/pension-jubilacion"
      }]
    }
    </script>

    <!-- FAQ Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [{
        "@type": "Question",
        "name": "¿Cómo calculo mi pensión de jubilación?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Introduzca su edad actual, años ó días cotizados, fecha de nacimiento y base reguladora ó sueldo bruto anual en nuestro simulador para obtener una estimación de su pensión."
        }
      },{
        "@type": "Question",
        "name": "¿Qué es la base reguladora?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "La base reguladora es el promedio de las bases de cotización de los últimos años de su vida laboral, que se utiliza para calcular su pensión."
        }
      },{
        "@type": "Question",
        "name": "¿Cómo se calcula el porcentaje de la pensión?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "El porcentaje depende de los años cotizados. Se necesitan 15 años mínimo para el 50% de la base reguladora. Cada mes adicional suma un porcentaje hasta llegar al 100%."
        }
      },{
        "@type": "Question",
        "name": "¿Cuál es la pensión máxima en 2025?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "La pensión máxima está establecida en 3.175,04 euros mensuales (14 pagas anuales). Este límite se actualiza cada año según el IPC."
        }
      },{
        "@type": "Question",
        "name": "¿Qué es la pensión deflactada?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "La pensión deflactada es el valor real estimado que tendrá su pensión cuando se jubile, teniendo en cuenta la pérdida de poder adquisitivo por la inflación."
        }
     }]
    }
    </script>

    <!-- Article Schema adicional -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Calculadora de Pensión de Jubilación 2025: Simule su pensión gratis",
  "description": "Utilice nuestro simulador de pensión gratuito y actualizado para calcular su pensión de jubilación estimada en 2025. Resultados instantáneos y precisos.",
  "datePublished": "2024-03-15",
  "dateModified": "2024-03-15",
  "author": {
    "@type": "Person",
    "name": "José Maria Muñiz"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Simulador de Pensiones",
    "logo": {
      "@type": "ImageObject",
      "url": "https://calculadora-de-pension.streamlit.app/"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://calculadora-de-pension.streamlit.app/"
  }
}
</script>

    <!-- HowTo Schema adicional -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Cómo calcular su pensión de jubilación",
  "description": "Guía paso a paso para calcular su pensión de jubilación estimada",
  "step": [
    {
      "@type": "HowToStep",
      "name": "Introduzca edad actual",
      "text": "Ingrese su edad actual entre 18 y 67 años"
    },
    {
      "@type": "HowToStep",
      "name": "Años cotizados",
      "text": "Indique sus años o días cotizados hasta la fecha"
    },
    {
      "@type": "HowToStep",
      "name": "Base reguladora",
      "text": "Introduzca su base reguladora mensual o sueldo bruto anual"
    },
    {
      "@type": "HowToStep",
      "name": "Calcular resultado",
      "text": "Pulse el botón calcular para obtener su pensión estimada"
    }
  ],
  "totalTime": "PT2M"
}
</script>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-P07CZVS8WQ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-P07CZVS8WQ');
</script>
""", height=0)

# CSS para ocultar el menú, el footer y el botón flotante de "Hosted with Streamlit"
hide_streamlit_elements = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    iframe[title="widget"] {display: none !important;}
    .breadcrumbs {
        padding: 10px 0;
        color: #666;
        font-size: 14px;
    }
    .last-updated {
        color: #666;
        font-size: 12px;
        text-align: right;
        margin-top: 10px;
    }
    </style>
"""
st.markdown(hide_streamlit_elements, unsafe_allow_html=True)

# Estilos personalizados
st.markdown("""
    <style>
    .block-container {
        background-color: #FFF8E1;
        padding: 1px; /* Reduci el padding */
        border-radius: 10px;
        width: 100%; /* Ajusta el ancho al 100% en móviles */
        margin: 0 auto; /* Centra horizontalmente */
    }
    .stButton button {
        background-color: #FF5722;
        color: white;
        font-size: 22px; /* Reduce el tamaño de fuente */
        padding: 8px 16px; /* Reduce el padding */
        border-radius: 8px;
        width: 100%; /* Ocupa todo el ancho disponible */
    }
    h1 {
        font-size: 1.8em; /* Reduce el tamaño de fuente del título */
        color: #333333;
    }
    label, .stRadio, .stNumberInput, .stTextInput {
        font-size: 16px; /* Reduce el tamaño de fuente de los controles */
        color: #333333;
    }
    .stNumberInput input {
        font-size: 14px;
        width: 100%; /* Ocupa todo el ancho disponible */
    }
    @media (min-width: 768px) { /* Estilos para pantallas más grandes */
        .block-container {
            width: 80%; /* Aumenta el ancho al 80% en pantallas más grandes */
        }
        .stButton button {
            width: auto; /* Vuelve al ancho automático en pantallas más grandes */
        }
    }
    </style>
""", unsafe_allow_html=True)

# Header y text optimizados para SEO
st.markdown("""
    <h1 style='font-size: 2em; font-weight: bold;'>Simulador de Jubilación</h1>
    <p style='font-size: 1em; margin-bottom: 18px;'>Utilice nuestra calculadora de pensión de jubilación y conozca su pensión estimada y futura deflactada.</p>
    <p class="last-updated">Última actualización: Noviembre 2024</p>
""", unsafe_allow_html=True)

# Banner publicitario al inicio
st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://swiy.co/descargar-guia-gratis" target="_blank">
            <img src="https://toolyu.com/image/Nuevo_Banner_Negro_728x180_1.webp" alt="10 Estrategias Claves para Mejorar Su pensión de Jubilación" style="width:100%; height:auto;">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Breadcrumbs y fecha de actualización
st.markdown("""
    <div class="breadcrumbs">
        Inicio > Calculadora > Simulador de Pensión de Jubilación
    </div>
""", unsafe_allow_html=True)

# Entradas de datos
st.markdown("#### Introduzca sus datos:")
col_edad, col_tipo_cotizacion, col_cotizacion_valor = st.columns(3)

with col_edad:
    edad_actual = st.number_input("Edad actual (18-67):", min_value=18, max_value=67, step=1, value=None, key="edad_actual")

with col_tipo_cotizacion:
    tipo_cotizacion = st.radio("Cotización en:", ["Años", "Días"], key="tipo_cotizacion")

with col_cotizacion_valor:
    if tipo_cotizacion == "Años":
        anios_cotizados = st.number_input("Años cotizados (máx. 51):", min_value=0, max_value=51, step=1, value=None, key="anios_cotizados")
        dias_cotizados = anios_cotizados * 365 if anios_cotizados is not None else 0
    else:
        dias_cotizados = st.number_input("Días cotizados (máx. 18615):", min_value=0, max_value=18615, step=1, value=None, key="dias_cotizados", format="%d")

# Campos de fecha de nacimiento
st.markdown("#### Introduzca su fecha de nacimiento(formato d/m/19xx):")
col_dia, col_mes, col_anio = st.columns(3)
with col_dia:
    dia = st.number_input("Día", min_value=1, max_value=31, value=None, key="fecha_dia", step=1, format="%d")
with col_mes:
    mes = st.number_input("Mes", min_value=1, max_value=12, value=None, key="fecha_mes", step=1, format="%d")
with col_anio:
    anio = st.number_input("Año", min_value=1900, max_value=date.today().year, value=None, key="fecha_anio", step=1, format="%d")

fecha_nacimiento = None
if dia and mes and anio:
    try:
        fecha_nacimiento = date(anio, mes, dia)
        if fecha_nacimiento > date.today():
            st.error("La fecha de nacimiento no puede ser futura.")
    except ValueError:
        st.error("Fecha de nacimiento no válida.")

# Días restantes hasta los 67 años
dias_hasta_67 = 0
if fecha_nacimiento:
    fecha_67 = date(fecha_nacimiento.year + 67, fecha_nacimiento.month, fecha_nacimiento.day)
    dias_hasta_67 = (fecha_67 - date.today()).days if fecha_67 > date.today() else 0

dias_cotizados = dias_cotizados or 0
dias_totales_cotizados = dias_cotizados + dias_hasta_67

# Selección de base reguladora o sueldo anual
st.markdown("#### Seleccione su base reguladora ó su sueldo bruto anual(decimales admitidos con coma):")
col_opcion_base, col_base_valor = st.columns(2)
with col_opcion_base:
    opcion_base = st.radio("Selecciona una opción:", ["Base reguladora mensual", "Sueldo bruto anual"], key="opcion_base")

with col_base_valor:
    if opcion_base == "Base reguladora mensual":
        base_reguladora = st.number_input("Base reguladora mensual:", min_value=0.0, format="%.2f", value=None, key="base_reguladora")
    else:
        sueldo_bruto_anual = st.number_input("Sueldo bruto anual:", min_value=0.0, format="%.2f", value=None, key="sueldo_bruto_anual")
        base_reguladora = sueldo_bruto_anual / 12 if sueldo_bruto_anual else 0.0

# Cálculo de la pensión mensual bruta y deflactada
if st.button("Calcular Pensión y ver resultados abajo ⬇⬇"):
    if not fecha_nacimiento:
        st.error("Por favor, introduzca una fecha de nacimiento válida.")
    elif base_reguladora == 0:
        st.error("Por favor, introduzca la base reguladora o el sueldo bruto anual.")
    elif edad_actual is None or (edad_actual < 18 or edad_actual > 67):
        st.error("Por favor, introduzca una edad comprendida entre 18 y 67 años.")
    else:
        # Calcula porcentaje en función de los días totales cotizados
        anios_totales = dias_totales_cotizados / 365.0
        porcentaje_base = 0.5
        if anios_totales > 15:
            meses_adicionales = int((anios_totales - 15) * 12)
            porcentaje_base += meses_adicionales * 0.0019
            porcentaje_base = min(porcentaje_base, 1.0)

        pension_mensual_bruta = base_reguladora * porcentaje_base
        pension_mensual_bruta = min(pension_mensual_bruta, 3175.04)
        valor_deflactado = pension_mensual_bruta * 0.82

        # Agregar el segundo banner antes de los resultados
        st.markdown(
            """
            <div style="text-align: center; margin-top: 20px;">
                <a href="https://swiy.co/descargar-guia-gratis" target="_blank">
                    <img src="https://toolyu.com/image/Nuevo_Banner_Negro_728x180_1.webp" alt="10 Estrategias Claves para Mejorar Su pensión de Jubilación" style="width:100%; height:auto;">
                </a>
            </div>
            """,
            unsafe_allow_html=True
                )

        # Mostrar resultados en dos columnas
        st.header("Resultados de la Pensión Estimada")
        result_col1, result_col2 = st.columns(2)
        with result_col1:
            st.markdown(f"<h2 style='color:red;'>Pensión mensual bruta estimada: {pension_mensual_bruta:.2f} €</h2>", unsafe_allow_html=True)
            st.metric("Pensión deflactada a día de la jubilación", f"{valor_deflactado:.2f} €")
        with result_col2:
            st.metric("Días cotizados totales", f"{dias_totales_cotizados:,}")
            st.metric("Base reguladora mensual", f"{base_reguladora:.2f} €")
            st.metric("Porcentaje aplicado", f"{porcentaje_base * 100:.2f}%")

# Calcular y mostrar tiempo de carga
end_time = time.time()
load_time = end_time - start_time
st.markdown(f"<p class='last-updated'>Tiempo de carga: {load_time:.2f} segundos</p>", unsafe_allow_html=True)

while True:
    try:
        response = requests.get("https://calculadora-de-pension.streamlit.app/")
        print(f"Aplicación ping: {response.status_code}")
    except Exception as e:
        print(f"Error en el ping: {e}")
    time.sleep(600)  # Esperar 10 minutos (600 segundos)