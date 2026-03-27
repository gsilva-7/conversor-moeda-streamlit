import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="MoneyTech Converter", page_icon="💰")

# Função para buscar cotações em tempo real
def buscar_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    requisicao = requests.get(url)
    return requisicao.json()

st.title("💰 Conversor de Moedas em Tempo Real")
st.write("Valores atualizados via API externa.")

# 1. Buscar dados
try:
    dados = buscar_cotacoes()
    usd = float(dados['USDBRL']['bid'])
    eur = float(dados['EURBRL']['bid'])
    btc = float(dados['BTCBRL']['bid'])

    # 2. Interface de Entrada
    col1, col2 = st.columns(2)

    with col1:
        valor_brl = st.number_input("Valor em Reais (R$):", value=100.0, step=10.0)

    with col2:
        moeda_destino = st.selectbox(
            "Converter para:",
            ["Dólar (USD)", "Euro (EUR)", "Bitcoin (BTC)"]
        )

    # 3. Lógica de Conversão
    if moeda_destino == "Dólar (USD)":
        resultado = valor_brl / usd
        simbolo = "US$"
    elif moeda_destino == "Euro (EUR)":
        resultado = valor_brl / eur
        simbolo = "€"
    else:
        resultado = valor_brl / btc
        simbolo = "₿"

    # 4. Exibição com destaque
    st.divider()
    st.metric(label=f"Total em {moeda_destino}", value=f"{simbolo} {resultado:.2f}")
    
    # Mostrar cotação atual como referência
    st.caption(f"Cotação atual usada: 1.00 unidade da moeda = R$ {usd if 'Dólar' in moeda_destino else (eur if 'Euro' in moeda_destino else btc):.2f}")

except Exception as e:
    st.error("Erro ao conectar com a API de moedas. Verifique sua internet.")

st.divider()
st.caption("Dados fornecidos por AwesomeAPI | Projeto SENAI 2026")