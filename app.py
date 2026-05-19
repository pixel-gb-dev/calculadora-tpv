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
        margin-bottom: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.3);
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
    
    # --- CONFIGURACIÓN DE ASIGNACIÓN ASOCIATIVA Y SÍMBOLOS ---
    if tipo_tarjeta == "BBVA / Visa / Mastercard":
        plazos = ["Contado", "3 Meses", "6 Meses", "9 Meses", "12 Meses"]
        tasas = [0.02900, 0.06461, 0.11008, 0.15300, 0.19372]
        texto_banco = "BBVA"
        simbolo_banco = "🟦 BBVA"
        color_banco = "#004488"
    else:
        plazos = ["Contado", "3 Meses", "6 Meses", "9 Meses", "12 Meses"]
        tasas = [0.04466, 0.09802, 0.13630, 0.17574, 0.20646]
        texto_banco = "American Express"
        simbolo_banco = "🔷 AMEX"
        color_banco = "#0076a5"

    iconos = ["💳", "📅", "⏳", "⌛️", "💎"]

    # --- EFECTO VISUAL DE POP-UP CENTRADO CON BARRA Y SÍMBOLO ---
    session_key = f"load_{monto_limpio}_{tipo_tarjeta}"
    if session_key not in st.session_state:
        placeholder = st.empty()
        
        # Animación de 10 pasos fluidos (5 segundos en total)
        for i in range(11):
            porcentaje = i * 10
            placeholder.markdown(f"""
                <div class="modal-backdrop">
                    <div class="modal-box" style="border-color: {color_banco};">
                        <h2 style='color: white; margin: 0 0 10px 0; font-family: sans-serif;'>{simbolo_banco}</h2>
                        <h3 style='color: white; margin: 0 0 10px 0; font-family: sans-serif; font-size: 1.3em;'>Sincronizando Interfaz</h3>
                        <p style='color: #a0aec0; font-size: 1.0em; margin: 0;'>Estableciendo enlace seguro con la red de procesamiento...</p>
                        <progress value="{porcentaje}" max="100"></progress>
                        <p style='color: #3e4a5b; font-size: 0.9em; margin: 0; text-align: right;'>{porcentaje}%</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            time.sleep(0.5)
            
        # Pantalla final de éxito con el símbolo de la red de pago
        placeholder.markdown(f"""
            <div class="modal-backdrop">
                <div class="modal-box" style="border-color: #28a745;">
                    <h2 style='color: #28a745; margin: 0 0 10px 0; font-family: sans-serif;'>🔒 {texto_banco} Conectado</h2>
                    <p style='color: white; font-size: 1.1em; margin: 0;'>Enlace de procesamiento autorizado y cifrado con éxito.</p>
                    <div style="font-size: 3em; margin-top: 15px;">✅</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        time.sleep(1.2)
        placeholder.empty() 
        st.session_state[session_key] = True
        st.rerun()

    # 4. Dashboard de Métricas
    st.write(f"### Su Resumen de Margen | {simbolo_banco}")
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
    st.caption(f"Valores preferenciales procesados mediante la red oficial {simbolo_banco}")
    
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
