import streamlit as st
import os  # Para verificar la imagen header.png de forma segura
import time

# 1. Configuración de Marca y Estilo Pro
st.set_page_config(page_title="pixel_gb.dev | Pro", page_icon="💎", layout="wide")

# CSS para el look visual y moderno
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
        border-top: 5px solid #004488;
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
    monto_limpio = st.number_input("¿Cuánto deseas recibir libre? ($)", min_value=0.0, step=1000.0, value=0.0)
    st.divider()
    st.write("🔧 **Base BBVA Oficial**")
    st.caption("Tasas con Comisión + IVA incluido.")

# 3. Encabezado de Imagen Seguro
if os.path.exists("header.png"):
    st.image("header.png", use_container_width=True)
else:
    st.title("🚀 pixel_gb.dev")
    st.info("💡 Tip visual: Asegúrate de que tu diseño en GitHub se llame 'header.png' para que aparezca aquí.")

st.write("---")

if monto_limpio > 0:
    # 4. Dashboard de Métricas Visuales
    st.write("### Su Resumen de Margen")
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Tu Depósito NETO Real", value=f"${monto_limpio:,.2f}")
    with col_b:
        tasa_max = 0.19372
        total_max = monto_limpio / (1 - tasa_max)
        st.metric(label="Monto Máximo Cobrado (12M)", value=f"${total_max:,.2f}", delta="Todo Incluido")

    st.divider()
    
    # 5. Opciones para Presentar al Cliente
    st.write("### 📋 Tabla de Cotizaciones para el Cliente")
    st.write("Muestra estas mensualidades elegantes:")
    
    col1, col2, col3 = st.columns(3)
    
    # TASAS OFICIALES BBVA + IVA (Completas para dejarte tu dinero neto libre)
    tasas = {
        "Contado": 0.0290,      # 2.5% + IVA
        "3 Meses": 0.06461,     # 5.57% + IVA
        "6 Meses": 0.11008,     # 9.49% + IVA
        "9 Meses": 0.15300,     # 13.19% + IVA (redondeado a 15.30%)
        "12 Meses": 0.19372     # 16.70% + IVA
    }

    # Ajuste por si hubo un typo en el valor de 9 meses en la ejecución del diccionario
    tasas["9 Meses"] = 0.15300

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

    # 6. Sección Interna Protegida en la Barra Lateral
    st.sidebar.markdown("---")
    with st.sidebar.expander("🔐 DATOS DE TERMINAL (SÓLO TÚ)"):
        st.table({
            "Plazo": list(tasas.keys()),
            "A Digitar": [f"${monto_limpio/(1-t):,.2f}" for t in tasas.values()],
            "Total Retenido": [f"${(monto_limpio/(1-t))-monto_limpio:,.2f}" for t in tasas.values()]
        })

else:
    st.info("👋 ¡Bienvenido! Ingresa la cantidad neta que deseas ganar en la barra lateral para activar las tarjetas.")

st.caption("© 2026 pixel_gb.dev | Soluciones Digitales Inteligentes")
