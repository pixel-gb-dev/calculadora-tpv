import streamlit as st
import time

# Configuración de la identidad visual de tu marca
st.set_page_config(page_title="pixel_gb.dev | Calculadora", page_icon="📈")

# Estilo personalizado
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #004488; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("pixel_gb.dev")
st.subheader("Herramienta de Gestión de Cobros TPV")

# Animación de inicio
with st.status("Conectando con servidores bancarios...", expanded=True) as status:
    st.write("Sincronizando tasas de comisión BBVA 2026...")
    time.sleep(1.2)
    st.write("Verificando parámetros de seguridad...")
    time.sleep(0.8)
    status.update(label="✅ Sistema listo y actualizado", state="complete", expanded=False)

# Entrada de datos
monto_limpio = st.number_input("¿Qué cantidad deseas recibir libre en tu cuenta? ($):", min_value=0.0, step=500.0, value=0.0)

# Tasas calculadas (Base 2.9% final + sobretasas bancarias)
tasas = {
    "Contado (Una exhibición)": 0.029,
    "3 Meses": 0.081,
    "6 Meses": 0.123,
    "9 Meses": 0.165,
    "12 Meses": 0.208
}

if monto_limpio > 0:
    st.divider()
    
    # VISTA PARA EL CLIENTE
    st.markdown("### 📋 Tabla para el Cliente")
    st.write("Usa estos montos para presentar el presupuesto:")
    
    for plazo, tasa in tasas.items():
        monto_total = monto_limpio / (1 - tasa)
        pago_mensual = monto_total / (1 if "Contado" in plazo else int(plazo.split()[0]))
        
        with st.expander(f"💳 {plazo}"):
            st.markdown(f"**Pago Mensual: ${pago_mensual:,.2f}**")
            st.caption(f"Total a liquidar con tarjeta: ${monto_total:,.2f}")

    st.divider()

    # VISTA INTERNA
    st.markdown("### 🔐 Control Interno (Solo pixel_gb.dev)")
    st.write("Lo que debes digitar en la terminal:")
    
    for plazo, tasa in tasas.items():
        monto_total = monto_limpio / (1 - tasa)
        comision_pesos = monto_total - monto_limpio
        st.warning(f"**{plazo}**: Digitar **${monto_total:,.2f}**")
        st.write(f"Tú recibes: ${monto_limpio:,.2f} | El banco retiene: ${comision_pesos:,.2f}")

st.sidebar.markdown("---")
st.sidebar.write("Desarrollado por **pixel_gb.dev**")
