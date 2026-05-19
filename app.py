import streamlit as st
import os
import time

# 1. Configuración Pro
st.set_page_config(page_title="pixel_gb.dev | Pro", page_icon="💎", layout="wide")

# CSS para el look visual moderno
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
    .stProgress > div > div > div > div { background-color: #004488; }
    </style>
    """, unsafe_allow_html=True)

# 2. Barra Lateral (Sidebar)
with st.sidebar:
    st.markdown("### ⚙️ Herramientas de pixel_gb.dev")
    st.write("---")
    monto_limpio = st.number_input("¿Cuánto deseas recibir libre? ($)", min_value=0.0, step=1000.0, value=0.0)
    
    # NUEVO: Selector de tipo de tarjeta para marketing y precisión
    tipo_tarjeta = st.selectbox("Tipo de Tarjeta del Cliente:", ["BBVA / Visa / Mastercard", "American Express (AMEX)"])
    
    st.divider()
    st.write(f"🔧 **Base: {tipo_tarjeta}**")
    st.caption("Comisión + IVA calculados al momento.")

# 3. Encabezado de Imagen Seguro
if os.path.exists("header.png"):
    st.image("header.png", use_container_width=True)
else:
    st.title("🚀 pixel_gb.dev")

st.write("---")

if monto_limpio > 0:
    
    # --- ASIGNACIÓN DE TASAS SEGÚN LA SELECCIÓN ---
    if tipo_tarjeta == "BBVA / Visa / Mastercard":
        tasas = {
            "Contado": 0.02900,      # 2.5% + IVA
            "3 Meses": 0.06461,     # 5.57% + IVA
            "6 Meses": 0.11008,     # 9.49% + IVA
            "9 Meses": 0.15300,     # 13.19% + IVA
            "12 Meses": 0.19372     # 16.70% + IVA
        }
        texto_banco = "BBVA"
    else:
        # Tasas oficiales de American Express con IVA de Comisión Incluido
        tasas = {
            "Contado": 0.04466,      # 3.85% + IVA
            "3 Meses": 0.09802,     # (3.85% + 4.60%) + IVA
            "6 Meses": 0.13630,     # (3.85% + 7.90%) + IVA
            "9 Meses": 0.17574,     # (3.85% + 11.30%) + IVA
            "12 Meses": 0.20646     # (3.85% + 13.95%) + IVA
        }
        texto_banco = "American Express"

    # --- EFECTO VISUAL DE SINCRONIZACIÓN (5 SEGUNDOS) ---
    session_key = f"load_{monto_limpio}_{tipo_tarjeta}"
    if session_key not in st.session_state:
        with st.spinner(f"⏳ Estableciendo conexión segura con la red de {texto_banco}..."):
            progreso_bar = st.progress(0)
            for porcentaje in range(101):
                time.sleep(0.05)
                progreso_bar.progress(porcentaje)
        st.success(f"🔒 Enlace de procesamiento autorizado con {texto_banco}.")
        st.session_state[session_key] = True
        time.sleep(1)
        st.rerun()

    # 4. Dashboard de Métricas
    st.write(f"### Su Resumen de Margen ({texto_banco})")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Tu Depósito NETO Real", value=f"${monto_limpio:,.2f}")
    with col_b:
        tasa_max = tasas["12 Meses"]
        total_max = monto_limpio / (1 - tasa_max)
        st.metric(label="Monto Máximo Cobrado (12M)", value=f"${total_max:,.2f}", delta="Todo Incluido")

    st.divider()
    
    # 5. Opciones para el Cliente
    st.write("### 📋 Tabla de Cotizaciones para el Cliente")
    st.caption(f"Valores preferenciales procesados mediante la red {texto_banco}")
    
    col1, col2, col3 = st.columns(3)
    iconos = ["💳", "📅", "⏳", "⌛️", "💎"]

    for i, (plazo, tasa) in enumerate(tasas.items()):
        monto_total = monto_limpio / (1 - tasa)
        pago_mensual = monto_total / (1 if "Contado" in plazo else int(plazo.split()[0]))
        
        target_col = [col1, col2, col3][i % 3]
        with target_col:
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

    # 6. Sección Interna Oculta
    st.sidebar.markdown("---")
    with st.sidebar.expander("🔐 DATOS DE TERMINAL (SÓLO TÚ)"):
        st.table({
            "Plazo": list(tasas.keys()),
            "A Digitar": [f"${monto_limpio/(1-t):,.2f}" for t in tasas.values()],
            "Total Retenido": [f"${(monto_limpio/(1-t))-monto_limpio:,.2f}" for t in tasas.values()]
        })
else:
    st.info("👋 ¡Bienvenido! Ingresa la cantidad neta y selecciona el tipo de tarjeta en la barra lateral.")

st.caption("© 2026 pixel_gb.dev | Soluciones Digitales Inteligentes")
