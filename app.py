import streamlit as st
from PIL import Image  # Necesaria para manejar imágenes visualmente
import time

# 1. Configuración de Marca y Estilo
st.set_page_config(page_title="pixel_gb.dev | Pro", page_icon="💎", layout="wide")

# CSS Avanzado para mejorar visualmente las tarjetas y métricas
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    div.stNumberInput > div > div > input { background-color: #1e2630; color: white; border-radius: 10px; font-size: 1.2em; }
    .stMetric { background-color: #1e2630; padding: 20px; border-radius: 15px; border: 1px solid #3e4a5b; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    .client-card { 
        background-color: #ffffff; 
        padding: 25px; 
        border-radius: 15px; 
        color: #1e2630; 
        margin-bottom: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        border-top: 5px solid #004488; /* Detalle de color visual */
    }
    [data-testid="stSidebar"] {
        background-color: #11141a;
        border-right: 1px solid #3e4a5b;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Barra Lateral (Sidebar)
with st.sidebar:
    st.markdown("### ⚙️ Herramientas de pixel_gb.dev")
    st.write("---")
    monto_limpio = st.number_input("¿Cuánto deseas recibir libre? ($)", min_value=0.0, step=1000.0, value=10000.0)
    st.divider()
    st.write("🔧 **Base BBVA 2026**")
    st.caption("Comisiones y sobretasas actualizadas.")

# 3. Encabezado Principal (AQUÍ ESTÁ EL CAMBIO VISUAL)
# Intentamos cargar la imagen diseñada por ti
try:
    # use_container_width=True asegura que se adapte al ancho del celular
    st.image("header.png", use_container_width=True) 
except FileNotFoundError:
    # Si aún no subes la imagen, mostramos un título elegante de respaldo
    st.title("📈 pixel_gb.dev | TPV Calculator")
    st.caption("💡 Sube tu imagen 'header.png' a GitHub para verla aquí.")

st.write("---")

if monto_limpio > 0:
    # 4. Dashboard de Métricas Visuales
    st.write("### Su Resumen de Margen")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Tu Depósito NETO (Libre)", value=f"${monto_limpio:,.2f}")
    with col_b:
        # Tasa de 12 meses como referencia máxima
        tasa_max = 0.208
        total_max = monto_limpio / (1 - tasa_max)
        st.metric(label="Monto Máximo Sugerido", value=f"${total_max:,.2f}", delta="Financiado (Aprox)")

    st.divider()
    
    # 5. Opciones para Presentar al Cliente
    st.write("### 📋 Tabla de Cotizaciones para el Cliente")
    st.write("Muestra estas mensualidades elegantes:")
    
    # Creamos columnas para una distribución visual
    col1, col2, col3 = st.columns(3)
    
    tasas = {
        "Pago de Contado": 0.029,
        "A 3 Meses": 0.081,
        "A 6 Meses": 0.123,
        "A 9 Meses": 0.165,
        "A 12 Meses": 0.208
    }

    # Íconos visuales (Unicode) para cada opción
    iconos = ["💳", "📅", "⏳", "⌛️", "💎"]

    # Ciclo para generar las tarjetas visuales
    for i, (plazo, tasa) in enumerate(tasas.items()):
        monto_total = monto_limpio / (1 - tasa)
        pago_mensual = monto_total / (1 if "Contado" in plazo else int(plazo.split()[0]))
        
        target_col = [col1, col2, col3][i % 3]
        
        with target_col:
            # HTML y CSS personalizados para una tarjeta "Visual"
            st.markdown(f"""
                <div class="client-card">
                    <h3 style='margin:0; color:#004488;'>{iconos[i]} {plazo}</h3>
                    <p style='margin:10px 0; font-size:1.1em; color:#555;'>Monto Total con Tarjeta:</p>
                    <h4 style='margin:0; color:#333;'>${monto_total:,.2f}</h4>
                    <hr>
                    <p style='margin:5px 0; font-size:1.3em;'><strong>Paga Mensual:</strong></p>
                    <h1 style='margin:0; color:#1e2630;'>${pago_mensual:,.2f}</h1>
                </div>
            """, unsafe_allow_html=True)

    # 6. Sección Interna Protegida (Menos visual, más técnica)
    st.sidebar.markdown("---")
    with st.sidebar.expander("🔐 DATOS DE TERMINAL (SÓLO TÚ)"):
        st.table({
            "Plazo": list(tasas.keys()),
            "A Digitar": [f"${monto_limpio/(1-t):,.2f}" for t in tasas.values()]
        })

else:
    st.info("👋 ¡Bienvenido! Ingresa la cantidad neta que deseas ganar en la barra lateral.")

st.caption("© 2026 pixel_gb.dev | Innovación Digital de Gilberto Barboza")
