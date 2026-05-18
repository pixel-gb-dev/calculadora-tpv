import streamlit as st
import time

# 1. Configuración de Marca y Estilo
st.set_page_config(page_title="pixel_gb.dev | Pro", page_icon="💎", layout="wide")

# CSS para que se vea "Visual" y Moderno
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    div.stNumberInput > div > div > input { background-color: #1e2630; color: white; border-radius: 10px; }
    .stMetric { background-color: #1e2630; padding: 15px; border-radius: 15px; border: 1px solid #3e4a5b; }
    .client-card { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 15px; 
        color: #1e2630; 
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Barra Lateral (Sidebar)
with st.sidebar:
    st.title("⚙️ Configuración")
    monto_limpio = st.number_input("Monto libre deseado ($)", min_value=0.0, step=100.0, value=1000.0)
    st.divider()
    st.write("🔧 **Ajustes de Comisión**")
    st.caption("Tasas configuradas para BBVA 2026")

# 3. Encabezado Principal
st.title("🚀 pixel_gb.dev")
st.write("---")

if monto_limpio > 0:
    # 4. Visualización de Métricas (Dashboard)
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="Tu Ganancia Neta", value=f"${monto_limpio:,.2f}")
    with col_b:
        # Ejemplo con 12 meses para ver el máximo
        total_max = monto_limpio / (1 - 0.208)
        st.metric(label="Monto Máximo Sugerido", value=f"${total_max:,.2f}", delta="Financiado")

    st.write("### 📋 Opciones para presentar al Cliente")
    
    # Creamos columnas para que las tarjetas no sean una lista larga
    col1, col2, col3 = st.columns(3)
    
    tasas = {
        "Contado": 0.029,
        "3 Meses": 0.081,
        "6 Meses": 0.123,
        "9 Meses": 0.165,
        "12 Meses": 0.208
    }

    # Distribución en tarjetas visuales
    for i, (plazo, tasa) in enumerate(tasas.items()):
        monto_total = monto_limpio / (1 - tasa)
        pago_mensual = monto_total / (1 if "Contado" in plazo else int(plazo.split()[0]))
        
        # Elegir en qué columna poner la tarjeta
        target_col = [col1, col2, col3][i % 3]
        
        with target_col:
            st.markdown(f"""
                <div class="client-card">
                    <h3 style='margin:0; color:#004488;'>{plazo}</h3>
                    <p style='margin:5px 0; font-size:1.2em;'>Mensualidad:</p>
                    <h2 style='margin:0; color:#1e2630;'>${pago_mensual:,.2f}</h2>
                    <hr>
                    <p style='font-size:0.8em; color:#666;'>Total a pasar: ${monto_total:,.2f}</p>
                </div>
            """, unsafe_allow_html=True)

    # 5. Sección Interna Protegida
    with st.expander("🔐 VER DATOS PARA TERMINAL (SÓLO PARA TI)"):
        st.table({
            "Plazo": list(tasas.keys()),
            "Monto a Digitar": [f"${monto_limpio/(1-t):,.2f}" for t in tasas.values()],
            "Comisión": [f"${(monto_limpio/(1-t))-monto_limpio:,.2f}" for t in tasas.values()]
        })

else:
    st.info("👋 ¡Bienvenido! Ingresa un monto en la barra lateral para empezar a calcular.")

st.caption("© 2026 pixel_gb.dev | Innovación Digital")
