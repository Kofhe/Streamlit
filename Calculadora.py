# Calculadora de IMC

import streamlit as st

st.title("Calculadora")

# Entrada
numero1 = st.number_input("Digite seu número para a calculadora:", placeholder="Digite seu número")
numero2 = st.number_input("Digite seu segundo número para a calculadora", placeholder="Digite seu segundo número")

# Processamento
sinal = st.selectbox("Escolha o cálculo que quer realizar", ("Soma", "Menos", "Divisão", "Multiplicação"))
st.write("Você selecionou:", sinal)

# Botão para calcular
if st.button("Calcular",type="primary"):
    if sinal == "Soma":
        resultado = numero1 + numero2
    elif sinal == "Menos":
        resultado = numero1 - numero2
    elif sinal == "Divisão":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            st.error("Erro: Divisão por zero não é permitida.")
            resultado = "Indefinido"
    elif sinal == "Multiplicação":
        resultado = numero1 * numero2

    # Saída
    if resultado != "Indefinido":
        st.success(f"O resultado da {sinal} é: {resultado}")
