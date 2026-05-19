import streamlit as st
import os
import time

# 1. Configuración de Marca Pro
st.set_page_config(page_title="pixel_gb.dev | Pro", page_icon="💎", layout="wide")

# CSS Avanzado: Modales con efecto Pop-up, Desenfoque de fondo y personalización de marcas
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    div.stNumberInput > div > div > input { background-color: #1e2630; color: white; border-radius: 10px; font-size: 1.2em; }
    div.stSelectbox > div > div > div { background-color: #1e2630; color: white; border-radius: 10px; }
    .stMetric { background-color: #1e2630; padding: 20px; border-radius: 15px; border: 1px solid #3e4a5b; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    
    .client-card { 
        background-color: #ffffff; padding: 25px; border-radius: 15px; color: #1e2630; 
        margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3); border-top: 5px solid #004488;
    }
    [data-testid="stSidebar"] { background-color: #11141a; border-right: 1px solid #3e4a5b; }
    
    /* --- EFECTO VISUAL DE POP-UP (MODAL) Y DESENFOQUE --- */
    .modal-backdrop {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: rgba(0, 0, 0, 0.75);
        backdrop-filter: blur(6px);
        z-index: 99999;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .modal-box {
        background-color: #1e2630;
        padding: 40px;
        border-radius: 20px;
        border: 2px solid #3e4a5b;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6);
        text-align: center;
        width: 85%;
        max-width: 450px;
    }

    /* --- DISEÑO DE LA BARRA DE PROGRESO PREMIUM --- */
    progress {
        width: 100%;
        height: 14px;
        margin: 20px 0 10px 0;
        display: block;
        -webkit-appearance: none;
        appearance: none;
    }
    progress::-webkit-progress-bar {
        background-color: #11141a;
        border-radius: 10px;
    }
    progress::-webkit-progress-value {
        background-color: #004488;
        border-radius: 10px;
        box-shadow: 0 0 10px #004488;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Barra Lateral (Sidebar)
with st.sidebar:
    st.markdown("### ⚙️ Herramientas de pixel_gb.dev")
    st.write("---")
    monto_limpio = st.number_input("¿Cuánto deseas recibir libre? ($)", min_value=0.0, step=1000.0, value=0.0)
    tipo_tarjeta = st.selectbox("Tipo de Tarjeta del Cliente:", ["BBVA / Visa / Mastercard", "American Express (AMEX)"])
    st.divider()
    st.write(f"🔧 **Base actual: {tipo_tarjeta}**")
    st.caption("Comisión + IVA integrados para cálculo Neto.")

# 3. Encabezado de Imagen Autónomo
if os.path.exists("header.png"):
    st.image("header.png", use_container_width=True)
else:
    st.title("🚀 pixel_gb.dev")

st.write("---")

if monto_limpio > 0:
    
    # --- CONFIGURACIÓN DE ASIGNACIÓN ASOCIATIVA Y SÍMBOLOS DE MARCA ---
    if tipo_tarjeta == "BBVA / Visa / Mastercard":
        plazos = ["Contado", "3 Meses", "6 Meses", "9 Meses", "12 Meses"]
        tasas =
