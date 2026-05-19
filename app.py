import streamlit as st
import os
import time

# 1. Configuración de Marca Pro
st.set_page_config(page_title="pixel_gb.dev | Pro", page_icon="💎", layout="wide")

# CSS Avanzado: Interfaz Premium con efecto Pop-up, Desenfoque de fondo (Fiel a la imagen)
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
    
    /* --- CONTENEDOR FLOTANTE DE ALTA FIDELIDAD (POP-UP) --- */
    .custom-modal-bg {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background-color: rgba(4, 6, 10, 0.8);
        backdrop-filter: blur(8px);
        z-index: 999999;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .custom-modal-box {
        background-color: #141923;
        border-radius: 16px;
        border: 2px solid #004488;
        box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        width: 90%;
        max-width: 500px;
        overflow: hidden;
        animation: fadeIn 0.3s ease-out;
    }
    
    /* CABECERA BLANCA IDÉNTICA A LA IMAGEN */
    .custom-modal-header {
        background-color: #ffffff;
        padding: 20px 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #e2e8f0;
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
    .text-slot-main { color: #000000; font-size: 22px; font-weight: 400; display: block; }
    .text-slot-sub { color: #000000; font-size: 22px; font-weight: 700; display: block; }
    
    /* CUERPO DEL MODAL RECONSTRUIDO */
    .custom-modal-body {
        padding: 35px 25px;
        text-align: center;
    }
    .custom-modal-body p {
        color: #ffffff;
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 1.1em;
        margin: 0 0 25px 0;
        line-height: 1.5;
    }
    
    /* FORZAR ESTILOS A LA BARRA DE PROGRESO NATIVA DE STREAMLIT PARA AJUSTARLA A LA IMAGEN */
    .stProgress > div > div {
        background-color: #0d1117 !important;
        height: 28px !important;
        border-radius: 14px !important;
        border: 1px solid #1f293d !important;
        overflow: hidden !important;
    }
    .stProgress > div > div > div {
        background: linear-gradient(180deg, #0099ff 0%, #004488 100%) !important;
        border-radius: 12px !important;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: scale(1); }
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

# DECLARACIÓN GLOBAL DE CONTROL DE ARRAYS
plazos = ["Contado", "3 Meses", "6 Meses", "9 Meses", "12 Meses"]
iconos = ["💳", "📅", "⏳", "⌛️", "💎"]

if monto_limpio > 0:
    
    # --- ASIGNACIÓN DE PARÁMETROS GRÁFICOS VECTORIALES (LOGOS EXACTOS) ---
    if tipo_tarjeta == "BBVA / Visa / Mastercard":
        tasas = [0.02900, 0.06461, 0.11008, 0.15300, 0.19372]
        texto_banco = "BBVA"
        color_banco = "#004488"
        # SVG nativo exacto de BBVA con dimensiones fijas de lectura
        html_logo = """
        <svg width="120" height="30" viewBox="0 0 120 30" xmlns="http://www.w3.org/2000/svg" style="display:block;">
            <path d="M0 0h8.4c4.8 0 7.8 2.2 7.8 5.8 0 2.4-1.4 4.4-4.2 5.4 2.8 1 4.6 3.2 4.6 6.2 0 4-3.6 6.6-12.2 6.6H0V0zm4.8 4.2V9.4h2.4c2 0 3.2-.8 3.2-2.6s-1.2-2.6-3.2-2.6H4.8zm0 9.2v6.8h2.8c2.2 0 3.6-1 3.6-3.4 0-2.4-1.4-3.4-3.6-3.4H4.8zM21.6 0h8.4c4.8 0 7.8 2.2 7.8 5.8 0 2.4-1.4 4.4-4.2 5.4 2.8 1 4.6 3.2 4.6 6.2 0 4-3.6 6.6-12.2 6.6h-4.4V0zm4.8 4.2V9.4h2.4c2 0 3.2-.8 3.2-2.6s-1.2-2.6-3.2-2.6h-2.4zm0 9.2v6.8h2.8c2.2 0 3.6-1 3.6-3.4 0-2.4-1.4-3.4-3.6-3.4h-2.8zM51.6 0h4.8l6.4 24h-5.2l-1.2-5.4H49.6L48.4 24h-5.2L49.6 0zm-1.2 14.4h5.2L53.2 4.8l-2.8 9.6zM67.2 0h4.8l6 16.4L84 0h4.8L80.4 24h-4.8l-8.4-24z" fill="#004488"/>
        </svg>
        """
    else:
        tasas = [0.04466, 0.09802, 0.13630, 0.17574, 0.20646]
        texto_banco = "American Express"
        color_banco = "#0076a5"
        # SVG nativo estilizado de la caja AMEX
        html_logo = """
        <svg width="110" height="32" viewBox="0 0 100 30" xmlns="http://www.w3.org/2000/svg" style="display:block;">
            <rect width="100" height="30" rx="4" fill="#0076A5"/>
            <text x="50" y="21" fill="#FFFFFF" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-weight="900" font-size="15" letter-spacing="0.5" text-anchor="middle">AMEX</text>
        </svg>
        """

    # --- EFECTO VISUAL DE POP-UP CENTRADO CROMETRICAMENTE BLINDADO ---
    session_key = f"load_{monto_limpio}_{tipo_tarjeta}"
    if session_key not in st.session_state:
        # Creamos la inyección estructural del marco de fondo fijo y la caja blanca superior
        modal_placeholder = st.empty()
        
        # Ejecutamos la animación en 10 iteraciones limpias acopladas al loop seguro
        for percent in range(0, 101, 10):
            with modal_placeholder.container():
                st.markdown(f"""
                    <div class="custom-modal-bg">
                        <div class="custom-modal-box" style="border-color: {color_banco};">
                            <div class="custom-modal-header">
                                <div class="logo-slot">{html_logo}</div>
                                <div class="text-slot">
                                    <span class="text-slot-main">Sincronizando</span>
                                    <span class="text-slot-sub">Interfaz</span>
                                </div>
                            </div>
                            <div class="custom-modal-body">
                                <p>Conectando de forma segura con los servidores de información de {texto_banco}...</p>
                                <div style="text-align: left; color:#a0aec0; margin-bottom:5px; font-weight:bold; font-size:0.9em;">Progreso: {percent}%</div>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Renderizamos la barra de progreso de Streamlit de forma interna, pero el CSS de arriba la intercepta y le da el look exacto de la imagen
                st.progress(percent / 100)
                time.sleep(0.4) # 0.4s * 11 pasos = ~4.5 a 5 segundos perfectos
                
        # Mostrar pantalla corta de éxito rotundo
        with modal_placeholder.container():
            st.markdown(f"""
                <div class="custom-modal-bg">
                    <div class="custom-modal-box" style="border-color: #28a745;">
                        <div class="custom-modal-header">
                            <div class="logo-slot">{html_logo}</div>
                            <div class="text-slot">
                                <span class="text-slot-main" style="color: #28a745;">Enlace</span>
                                <span class="text-slot-sub" style="color: #28a745;">Exitoso</span>
                            </div>
                        </div>
                        <div class="custom-modal-body">
                            <p style="color: #28a745; font-weight: bold;">Sincronización Exitosa (Base {texto_banco} Oficial)</p>
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
