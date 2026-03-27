import streamlit as st

# Configuração visual
st.set_page_config(page_title="TechCalc SENAI", page_icon="🔢")

st.title("🔢 Calculadora Técnica de Conversão")
st.markdown("---")

# Interface de entrada
col1, col2 = st.columns(2)

with col1:
    valor = st.number_input("Insira o valor:", value=1.0, step=0.1)

with col2:
    tipo = st.selectbox(
        "Converter de:",
        ["Polegadas para mm", "mm para Polegadas", "Celsius para Fahrenheit", "PSI para Bar"]
    )

# Lógica de processamento
if tipo == "Polegadas para mm":
    res = valor * 25.4
    unidade = "mm"
elif tipo == "mm para Polegadas":
    res = valor / 25.4
    unidade = "pol"
elif tipo == "Celsius para Fahrenheit":
    res = (valor * 9/5) + 32
    unidade = "°F"
else: # PSI para Bar
    res = valor * 0.0689476
    unidade = "bar"

# Exibição do Resultado
st.subheader("Resultado:")
st.metric(label=tipo, value=f"{res:.2f} {unidade}")

st.divider()
st.caption("Dica: Use o '.' para casas decimais e os botões de + e - para ajustar o valor.")