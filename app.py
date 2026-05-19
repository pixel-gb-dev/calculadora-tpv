import streamlit as st
import os
import time

# 1. Configuración de Marca Pro
st.set_page_config(page_title="pixel_gb.dev | Pro", page_icon="💎", layout="wide")

# CSS Avanzado: Modales premium con inyección de marcas y efectos de alta fidelidad (Fiel a la imagen)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    div.stNumberInput > div > div > input { background-color: #1e2630; color: white; border-radius: 10px; font-size: 1.2em; }
    div.stSelectbox > div > div > div { background-color: #1e2630; color: white; border-radius: 10px; }
    .stMetric { background-color: #1e2630; padding: 20px; border-radius: 15px; border: 1px solid #3e4a5b; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    
    .client-card { 
        background-color: #ffffff; padding: 25px; border-radius: 15px; color: #1e2630; 
        margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    [data-testid="stSidebar"] { background-color: #11141a; border-right: 1px solid #3e4a5b; }
    
    /* --- EFECTO VISUAL DE POP-UP (MODAL) Y BACKDROP BLUR --- */
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
        background-color: #141923;
        border-radius: 16px;
        border: 2px solid #004488;
        box-shadow: 0 20px 50px rgba(0,0,0,0.7);
        width: 90%;
        max-width: 520px;
        overflow: hidden;
    }

    /* --- ENCABEZADO IDÉNTICO A LA IMAGEN (BLANCO PURO) --- */
    .modal-header-brand {
        background-color: #ffffff;
        padding: 15px 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #e2e8f0;
    }
    .brand-logo-container {
        display: flex;
        align-items: center;
    }
    .brand-logo-img {
        height: 32px;
        object-fit: contain;
    }
    .brand-title-text {
        text-align: right;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        line-height: 1.1;
    }
    .brand-title-main {
        color: #000000;
        font-size: 22px;
        font-weight: 500;
        display: block;
    }
    .brand-title-sub {
        color: #000000;
        font-size: 22px;
        font-weight: 700;
        display: block;
    }

    /* --- CUERPO DEL MODAL --- */
    .modal-body-content {
        padding: 30px 25px;
        text-align: center;
    }
    .modal-body-content p {
        color: #ffffff;
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 1.05em;
        margin: 0 0 25px 0;
        line-height: 1.4;
    }

    /* --- DISEÑO DE BARRA DE PROGRESO DE LA IMAGEN --- */
    .progress-wrapper {
        position: relative;
        width: 100%;
    }
    progress {
        width: 100%;
        height: 26px;
        display: block;
        -webkit-appearance: none;
        appearance: none;
    }
    progress::-webkit-progress-bar {
        background-color: #0d1117;
        border-radius: 14px;
        border: 1px solid #1f293d;
        padding: 2px;
    }
    progress::-webkit-progress-value {
        background: linear-gradient(180deg, #0088ff 0%, #004488 100%);
        border-radius: 12px;
    }
    .progress-text-overlay {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: #ffffff;
        font-family: system-ui, sans-serif;
        font-size: 0.9em;
        font-weight: bold;
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

# DECLARACIÓN GLOBAL DE VARIABLES PARA EVITAR EL NAMEERROR
plazos = ["Contado", "3 Meses", "6 Meses", "9 Meses", "12 Meses"]
iconos = ["💳", "📅", "⏳", "⌛️", "💎"]

if monto_limpio > 0:
    
    # --- ASIGNACIÓN DE TASAS E IMÁGENES DE MARCA ---
    if tipo_tarjeta == "BBVA / Visa / Mastercard":
        tasas = [0.02900, 0.06461, 0.11008, 0.15300, 0.19372]
        texto_banco = "BBVA"
        color_banco = "#004488"
        # URL de imagen limpia oficial de BBVA
        url_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/BBVA_Logo.svg/320px-BBVA_Logo.svg"
    else:
        tasas = [0.04466, 0.09802, 0.13630, 0.17574, 0.20646]
        texto_banco = "American Express"
        color_banco = "#0076a5"
        # URL de imagen limpia oficial de AMEX
        url_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/American_Express_logo_2018.svg/240px-American_Express_logo_2018.svg"

    # --- EFECTO VISUAL DE POP-UP CENTRADO (5 SEGUNDOS) ---
    session_key = f"load_{monto_limpio}_{tipo_tarjeta}"
    if session_key not in st.session_state:
        placeholder = st.empty()
        
        # Animación de 10 pasos fluidos
        for i_step in range(11):
            porcentaje = i_step * 10
            placeholder.markdown(f"""
                <div class="modal-backdrop">
                    <div class="modal-box" style="border-color: {color_banco};">
                        <div class="modal-header-brand">
                            <div class="brand-logo-container">
                                <img src="{url_logo}.png" class="brand-logo-img" alt="{texto_banco}">
                            </div>
                            <div class="brand-title-text">
                                <span class="brand-title-main">Sincronizando</span>
                                <span class="brand-title-sub">Interfaz</span>
                            </div>
                        </div>
                        <div class="modal-body-content">
                            <p>Conectando de forma segura con los servidores de información de {texto_banco}...</p>
                            <div class="progress-wrapper">
                                <progress value="{porcentaje}" max="100"></progress>
                                <span class="progress-text-overlay">{porcentaje}%</span>
                            </div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(0.5)
            
        # Pantalla final de éxito
        placeholder.markdown(f"""
            <div class="modal-backdrop">
                <div class="modal-box" style="border-color: #28a745;">
                    <div class="modal-header-brand">
                        <div class="brand-logo-container">
                            <img src="{url_logo}.png" class="brand-logo-img" alt="{texto_banco}">
                        </div>
                        <div class="brand-title-text">
                            <span class="brand-title-main" style="color: #28a745;">Enlace</span>
                            <span class="brand-title-sub" style="color: #28a745;">Exitoso</span>
                        </div>
                    </div>
                    <div class="modal-body-content">
                        <p style="color: #28a745; font-weight: bold; margin-bottom: 10px;">Sincronización Exitosa (Base {texto_banco} Oficial)</p>
                        <div style="font-size: 3em; margin-top: 5px;">✅</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        time.sleep(1.2)
        placeholder.empty() 
        st.session_state[session_key] = True
        st.rerun()

    # 4. Dashboard de Métricas
    st.write(f"### Su Resumen de Margen | 📱 Gestión {texto_banco}")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Tu Depósito NETO Real", value=f"${monto_limpio:,.2f}")
    with col_b:
        tasa_max = tasas[-1]
        total_max = monto_limpio / (1 - tasa_max)
        st
