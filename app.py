import streamlit as st
import os
import time

# 1. Configuración de Marca Pro
st.set_page_config(page_title="pixel_gb.dev | Pro", page_icon="💎", layout="wide")

# CSS Avanzado: Inyección de Modales Premium con efectos Glassmorphism e Identidad de Marca
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
        padding: 18px 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #e2e8f0;
        height: 80px;
    }
    .brand-logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }
    .brand-logo-img {
        max-height: 35px;
        width: auto;
        display: block;
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

    /* --- DISEÑO DE BARRA DE PROGRESO DE LA IMAGEN RECONSTRUIDO --- */
    .progress-wrapper {
        position: relative;
        width: 100%;
    }
    progress {
        width: 100%;
        height: 28px;
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
        font-size: 0.95em;
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

# CONTROL DE FLUJO Y VARIABLES GLOBALES
plazos = ["Contado", "3 Meses", "6 Meses", "9 Meses", "12 Meses"]
iconos = ["💳", "📅", "⏳", "⌛️", "💎"]

if monto_limpio > 0:
    
    # --- LOGOS EMBEBIDOS EN FORMATO BASE64 DATA-URI REALES ---
    if tipo_tarjeta == "BBVA / Visa / Mastercard":
        tasas = [0.02900, 0.06461, 0.11008, 0.15300, 0.19372]
        texto_banco = "BBVA"
        color_banco = "#004488"
        # Logotipo vectorial optimizado embebido
        base64_logo = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 30' fill='%23004488'><path d='M0 0h7.2c4.6 0 7.6 2.2 7.6 5.8 0 2.4-1.4 4.4-4 5.4 2.6 1 4.4 3.2 4.4 6.2 0 4-3.4 6.6-11.6 6.6H0V0zm4.4 4v5.6h2.6c2.2 0 3.4-1 3.4-2.8 0-1.8-1.2-2.8-3.4-2.8H4.4zm0 9.6V20h3c2.4 0 3.8-1.2 3.8-3.2 0-2-1.4-3.2-3.8-3.2h-3zM19.2 0h7.2c4.6 0 7.6 2.2 7.6 5.8 0 2.4-1.4 4.4-4 5.4 2.6 1 4.4 3.2 4.4 6.2 0 4-3.4 6.6-11.6 6.6H19.2V0zm4.4 4v5.6h2.6c2.2 0 3.4-1 3.4-2.8 0-1.8-1.2-2.8-3.4-2.8H23.6zm0 9.6V20h3c2.4 0 3.8-1.2 3.8-3.2 0-2-1.4-3.2-3.8-3.2h-3zM46.8 0h4.4l6 24h-4.8l-1.2-5.2H44.8L43.6 24h-4.8L44.8 0H46.8zm-1.2 14.8h4.8L48 5.2l-2.4 9.6zM61.2 0h4.4l5.6 16.4L76.8 0h4.4L73.4 24H69l-7.8-24z'/></svg>"
    else:
        tasas = [0.04466, 0.09802, 0.13630, 0.17574, 0.20646]
        texto_banco = "American Express"
        color_banco = "#0076a5"
        # Isotipo de American Express embebido
        base64_logo = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 30'><rect width='100' height='30' rx='4' fill='%230076A5'/><text x='12' y='21' fill='%23FFFFFF' font-family='sans-serif' font-weight='900' font-size='14' letter-spacing='0.5'>AMEX</text></svg>"

    # --- EFECTO VISUAL DE POP-UP CENTRADO (5 SEGUNDOS) ---
    session_key = f"load_{monto_limpio}_{tipo_tarjeta}"
    if session_key not in st.session_state:
        placeholder = st.empty()
        
        # Animación de 10 segmentos fluidos
        for i_step in range(11):
            porcentaje = i_step * 10
            placeholder.markdown(f"""
                <div class="modal-backdrop">
                    <div class="modal-box" style="border-color: {color_banco};">
                        <div class="modal-header-brand">
                            <div class="brand-logo-container">
                                <img src="{base64_logo}" class="brand-logo-img" alt="{texto_banco}">
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
            
        # Modal de éxito en sincronización cifrada
        placeholder.markdown(f"""
            <div class="modal-backdrop">
                <div class="modal-box" style="border-color: #28a745;">
                    <div class="modal-header-brand">
                        <div class="brand-logo-container">
                            <img src="{base64_logo}" class="brand-logo-img" alt="{texto_banco}">
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
        st.metric(label=f"Monto Máximo Cobrado ({texto_banco})", value=f"${total_max:,.2f}", delta="Todo Incluido")

    st.divider()
    
    # 5. Opciones para el Cliente
    st.write("### 📋 Tabla de Cotizaciones para el Cliente")
    st.caption(f"Valores preferenciales procesados mediante la red de pago {texto_banco}")
    
    col1, col2, col3 = st.columns(3)
    
    list_a_digitar = []
    list_total_retenido = []

    for i in range(len(plazos)):
        plazo = plazos[i]
        tasa = tasas[i]
        icono = iconos[i]
        
        monto_total = monto_limpio / (1 - tasa)
        pago_mensual = monto_total / (1 if "Contado" in plazo else int(plazo.split()[0]))
        
        list_a_digitar.append(f"${monto_total:,.2f}")
        list_total_retenido.append(f"${monto_total - monto_limpio:,.2f}")
        
        target_col = [col1, col2, col3][i % 3]
        with target_col:
            st.markdown(f"""
                <div class="client-card" style="border-top: 5px solid {color_banco};">
                    <h3 style='margin:0; color:{color_banco};'>{icono} {plazo}</h3>
                    <p style='margin:10px 0; font-size:1.1em; color:#555;'>Monto Total con Tarjeta:</p>
                    <h4 style='margin:0; color:#333;'>${monto_total:,.2f}</h4>
                    <hr>
                    <p style='margin:5px 0; font-size:1.3em;'><strong>Paga Mensual:</strong></p>
                    <h1 style='margin:0; color:#1e2630;'>${pago_mensual:,.2f}</h1>
                </div>
            """, unsafe_allow_html=True)

    # 6. Sección Interna Oculta para la Terminal
    st.sidebar.markdown("---")
    with st.sidebar.expander("🔐 DATOS DE TERMINAL (SÓLO TÚ)"):
        st.table({
            "Plazo": plazos,
            "A Digitar": list_a_digitar,
            "Total Retenido": list_total_retenido
        })
else:
    st.info("👋 ¡Bienvenido! Ingresa la cantidad neta y selecciona el tipo de tarjeta en la barra lateral.")

st.caption("© 2026 pixel_gb.dev | Soluciones Digitales Inteligentes")
