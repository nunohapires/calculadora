import streamlit as st

from calculadora import (
    divisao,
    divisao_inteira,
    multiplicacao,
    potencia,
    resto,
    soma,
    subtracao,
)


OPERACOES = {
    "Soma (+)": soma,
    "Subtração (-)": subtracao,
    "Multiplicação (*)": multiplicacao,
    "Divisão (/)": divisao,
    "Divisão inteira (//)": divisao_inteira,
    "Resto da divisão (%)": resto,
    "Potência (**)": potencia,
}


def calcular(operacao: str, a: float, b: float) -> float:
    funcao = OPERACOES[operacao]
    return funcao(a, b)


st.set_page_config(page_title="Calculadora Streamlit", page_icon="🧮", layout="centered")
st.title("🧮 Calculadora em Streamlit")
st.caption("Interface web para as operações da calculadora Python.")

with st.form("form_calculadora"):
    col_a, col_b = st.columns(2)
    with col_a:
        numero_a = st.number_input("Primeiro número", value=0.0, format="%.6f")
    with col_b:
        numero_b = st.number_input("Segundo número", value=0.0, format="%.6f")

    operacao = st.selectbox("Operação", options=list(OPERACOES.keys()))
    submitted = st.form_submit_button("Calcular")

if submitted:
    try:
        resultado = calcular(operacao, numero_a, numero_b)
        st.success(f"Resultado: {resultado}")
        st.info(f"Operação aplicada: {operacao}")
    except ValueError as err:
        st.error(f"Erro: {err}")

st.divider()
st.markdown(
    """
    ### Operações disponíveis
    - Soma (+)
    - Subtração (-)
    - Multiplicação (*)
    - Divisão (/)
    - Divisão inteira (//)
    - Resto da divisão (%)
    - Potência (**)
    """
)
