import streamlit as st
import os
import time

# 1. Configuración de Marca Pro
st.set_page_config(page_title="pixel_gb.dev | Pro", page_icon="💎", layout="wide")

# CSS Avanzado: Copiado exacto de las reglas visuales de tu imagen de referencia con transiciones fluidas
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
    
    /* --- ESTRUCTURA DEL MODAL (POP-UP) CENTRADO FIEL A LA IMAGEN --- */
    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(4, 6, 10, 0.85);
        backdrop-filter: blur(8px);
        z-index: 999999 !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    .custom-modal-box {
        background-color: #141923;
        border-radius: 16px;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        width: 90%;
        max-width: 500px;
        overflow: hidden;
    }
    
    /* CABECERA BLANCA CON LOGO Y TEXTO DE TU IMAGEN */
    .custom-modal-header {
        background-color: #ffffff;
        padding: 15px 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #e2e8f0;
        height: 85px;
        box-sizing: border-box;
    }
    .logo-slot {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .text-slot {
        text-align: right;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        line-height: 1.2;
    }
    .text-slot-main { color: #000000; font-size: 20px; font-weight: 400; display: block; }
    .text-slot-sub { color: #000000; font-size: 20px; font-weight: 700; display: block; }
    
    /* CUERPO DEL POP-UP */
    .custom-modal-body {
        padding: 30px 25px 35px 25px;
        text-align: center;
    }
    .custom-modal-body p {
        color: #ffffff;
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 1.05em;
        margin: 0 0 20px 0;
        line-height: 1.5;
    }

    /* --- DISEÑO DE BARRA DE PROGRESO FLUIDA (HTML PURO) --- */
    .custom-progress-wrapper {
        position: relative;
        width: 100%;
        text-align: center;
    }
    .custom-progress-bar-bg {
        width: 100%;
        height: 28px;
        background-color: #0d1117;
        border-radius: 14px;
        border: 1px solid #1f293d;
        overflow: hidden;
        position: relative;
        padding: 2px;
        box-sizing: border-box;
    }
    .custom-progress-bar-value {
        height: 100%;
        background: linear-gradient(180deg, #0099ff 0%, #004488 100%);
        border-radius: 11px;
        /* ANIMACIÓN LINEAL NATURAL DE PASO CORTO */
        transition: width 0.04s linear; 
    }
    .custom-progress-text {
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        color: #ffffff;
        font-family: system-ui, sans-serif;
        font-size: 0.95em;
        font-weight: bold;
        z-index: 2;
    }
    .success-icon-badge {
        position: absolute;
        right: 8px; top: 50%;
        transform: translateY(-50%);
        background-color: #28a745;
        color: white;
        border-radius: 50%;
        width: 18px; height: 18px;
        font-size: 11px;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 3;
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

# 3. Encabezado de Imagen Principal (Tu Banner)
if os.path.exists("header.png"):
    st.image("header.png", use_container_width=True)
else:
    st.title("🚀 pixel_gb.dev")

st.write("---")

# DECLARACIÓN GLOBAL DE VARIABLES
plazos = ["Contado", "3 Meses", "6 Meses", "9 Meses", "12 Meses"]
iconos = ["💳", "📅", "⏳", "⌛️", "💎"]

if monto_limpio > 0:
    
    # --- RENDERIZADO VECTORIAL SEGURO DE LOGOS ---
    if tipo_tarjeta == "BBVA / Visa / Mastercard":
        tasas = [0.02900, 0.06461, 0.11008, 0.15300, 0.19372]
        texto_banco = "BBVA"
        color_banco = "#004488"
        html_logo = """
        <div style="color: #004488; font-family: 'Arial Black', sans-serif; font-size: 26px; font-weight: 900; letter-spacing: -2px; display: flex; align-items: center;">
            <div style="width: 8px; height: 22px; background-color: #004488; margin-right: 5px; display: inline-block;"></div>
            BBVA
        </div>
        """
    else:
        tasas = [0.04466, 0.09802, 0.13630, 0.17574, 0.20646]
        texto_banco = "American Express"
        color_banco = "#0076a5"
        html_logo = """
        <div style="background-color: #0076A5; color: #FFFFFF; font-family: 'Arial Black', sans-serif; font-size: 13px; font-weight: 900; padding: 6px 12px; border-radius: 4px; letter-spacing: 0.5px; display: inline-block;">
            AMEX
        </div>
        """

    # --- SIMULACIÓN DEL POP-UP CON DESLIZAMIENTO NATURAL (1% EN 1%) ---
    session_key = f"load_{monto_limpio}_{tipo_tarjeta}"
    if session_key not in st.session_state:
        modal_placeholder = st.empty()
        
        # Incremento continuo de 1 en 1 para eliminar el efecto bloque
        for percent in range(0, 101, 1):
            badge_html = '<div class="success-icon-badge">✓</div>' if percent == 100 else ''
            
            modal_placeholder.markdown(f"""
                <div class="modal-backdrop">
                    <div class="custom-modal-box" style="border: 2px solid {color_banco};">
                        <div class="custom-modal-header">
                            <div class="logo-slot">{html_logo}</div>
                            <div class="text-slot">
                                <span class="text-slot-main">Sincronizando</span>
                                <span class="text-slot-sub">Interfaz</span>
                            </div>
                        </div>
                        <div class="custom-modal-body">
                            <p>Conectando de forma segura con los servidores de información de {texto_banco}...</p>
                            <div class="custom-progress-wrapper">
                                <div class="custom-progress-bar-bg">
                                    <div class="custom-progress-bar-value" style="width: {percent}%;"></div>
                                    <span class="custom-progress-text">{percent}%</span>
                                    {badge_html}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            # 0.04 segundos * 100 pasos = 4 segundos de carga continua e impecable
            time.sleep(0.04)
            
        # Breve mensaje de éxito centrado
        modal_placeholder.markdown(f"""
            <div class="modal-backdrop">
                <div class="custom-modal-box" style="border: 2px solid #28a745;">
                    <div class="custom-modal-header">
                        <div class="logo-slot">{html_logo}</div>
                        <div class="text-slot">
                            <span class="text-slot-main" style="color: #28a745;">Enlace</span>
                            <span class="text-slot-sub" style="color: #28a745;">Exitoso</span>
                        </div>
                    </div>
                    <div class="custom-modal-body">
                        <p style="color: #28a745; font-weight: bold; margin-bottom: 10px;">Sincronización Exitosa (Base {texto_banco} Oficial)</p>
                        <div style="font-size: 3em; margin-top: 10px;">✅</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        time.sleep(1.2)

        modal_placeholder.empty()
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
