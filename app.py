import streamlit as st
from datetime import date

# Configuración de la página
st.set_page_config(page_title="Calculadora de Pensión de Jubilación", page_icon="💼")

# Ocultar menú de hamburguesa y footer de Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Estilos personalizados
st.markdown("""
    <style>
    .block-container {
        background-color: #FFF8E1;
        padding: 25px;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #FF5722;  /* Color naranja-rojizo */
        color: white;
        font-size: 20px;
        padding: 10px;
        border-radius: 8px;
    }
    h1 {
        font-weight: bold;
        color: #333333;
    }
    label, .stRadio, .stNumberInput, .stTextInput {
        font-size: 18px;
        color: #333333;
    }
    .stNumberInput input {
        font-size: 14px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar el estado de la sesión
def init_session_state():
    if 'edad_actual' not in st.session_state:
        st.session_state.edad_actual = None
    if 'anios_cotizados' not in st.session_state:
        st.session_state.anios_cotizados = None
    if 'dias_cotizados' not in st.session_state:
        st.session_state.dias_cotizados = None
    if 'base_reguladora' not in st.session_state:
        st.session_state.base_reguladora = None
    if 'sueldo_bruto_anual' not in st.session_state:
        st.session_state.sueldo_bruto_anual = None
    if 'fecha_dia' not in st.session_state:
        st.session_state.fecha_dia = None
    if 'fecha_mes' not in st.session_state:
        st.session_state.fecha_mes = None
    if 'fecha_anio' not in st.session_state:
        st.session_state.fecha_anio = None
    if 'pension_mensual_bruta' not in st.session_state:
        st.session_state.pension_mensual_bruta = None
    if 'valor_deflactado' not in st.session_state:
        st.session_state.valor_deflactado = None
    if 'calculate_button_visible' not in st.session_state:
        st.session_state.calculate_button_visible = True

# Inicializar el estado de la sesión
init_session_state()

# Título principal
st.title("Calculadora de Pensión de Jubilación")

# Entradas de datos
st.markdown("#### Introduzca sus datos:")
col_edad, col_tipo_cotizacion, col_cotizacion_valor = st.columns(3)

with col_edad:
    edad_actual = st.number_input("Edad actual (18-67):", min_value=18, max_value=67, step=1, value=st.session_state.edad_actual, key="edad_actual")

with col_tipo_cotizacion:
    tipo_cotizacion = st.radio("Cotización en:", ["Años", "Días"], key="tipo_cotizacion")

with col_cotizacion_valor:
    if tipo_cotizacion == "Años":
        anios_cotizados = st.number_input("Años cotizados (máx. 51):", min_value=0, max_value=51, step=1, value=st.session_state.anios_cotizados, key="anios_cotizados")
        dias_cotizados = anios_cotizados * 365 if anios_cotizados is not None else 0
    else:
        dias_cotizados = st.number_input("Días cotizados (máx. 18615):", min_value=0, max_value=18615, step=1, value=st.session_state.dias_cotizados, key="dias_cotizados", format="%d")

# Campos de fecha de nacimiento
st.markdown("#### Introduzca su fecha de nacimiento:")
col_dia, col_mes, col_anio = st.columns(3)
with col_dia:
    dia = st.number_input("Día", min_value=1, max_value=31, value=st.session_state.fecha_dia, key="fecha_dia", step=1, format="%d")
with col_mes:
    mes = st.number_input("Mes", min_value=1, max_value=12, value=st.session_state.fecha_mes, key="fecha_mes", step=1, format="%d")
with col_anio:
    anio = st.number_input("Año", min_value=1900, max_value=date.today().year, value=st.session_state.fecha_anio, key="fecha_anio", step=1, format="%d")

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
col_opcion_base, col_base_valor = st.columns(2)
with col_opcion_base:
    opcion_base = st.radio("Selecciona una opción:", ["Base reguladora mensual", "Sueldo bruto anual"], key="opcion_base")

with col_base_valor:
    if opcion_base == "Base reguladora mensual":
        base_reguladora = st.number_input("Base reguladora mensual:", min_value=0.0, format="%.2f", value=st.session_state.base_reguladora, key="base_reguladora")
    else:
        sueldo_bruto_anual = st.number_input("Sueldo bruto anual:", min_value=0.0, format="%.2f", value=st.session_state.sueldo_bruto_anual, key="sueldo_bruto_anual")
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
