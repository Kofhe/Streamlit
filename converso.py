#1 - Conversor de moedas

import streamlit as st

st.title("Conversor")

#Entrada
dolar = st.number_input("Digite o valor em dolar:", placeholder = "Digite seu valor em dolar",step = 2)

#Processamento
reais = dolar * 5

#Saída
st.text(f"O valor de dolar {dolar:.2f} dolares é igual a {reais:.2f} reais")
#.2f formatar para duas casas fracionais
