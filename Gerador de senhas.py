# 3 - Gerador de senhas

import streamlit as st
from random import choice 
from string import ascii_letters

#Entrada
tamanho = st.select_slider(
    "Digite o tamanho da senha",
    [
        5.
        6.
        7.
        8.
    ]
)
aleatorio = ""

for in in range(tamanho):
    aleatorio += choice(ascii_letters)

st.text(f"A senha gerada foi: {aleatorio}")
print(tamanho)
