import streamlit as st
import pandas as pd


st.title("Relação entre as Estratégias Ativas e Competências Comportamentais")
df = pd.read_excel("dados.xlsx")

listDados = df.values.tolist()

#selection = st.selectbox("selecione a estratégia", df["ESTRATÉGIA"])
selection = st.selectbox("selecione a estratégia", [x[0] for x in listDados])

#option = [x for x in range(len(df["ESTRATÉGIA"])) if df["ESTRATÉGIA"][x] == selection]
option = [x for x in range(len(listDados)) if listDados[x][0] == selection]



st.subheader("Destinação")
st.write(listDados[option[0]][1])

st.subheader("Breve descrição")
st.write(listDados[option[0]][2])

st.subheader("Passo a passo didático")
"A sequência didática é uma forma de estruturar o pensamento de maneira lógica, coerente e rigorosa para planejar o trabalho docente tanto de uma aula, quanto de um projeto."
st.write(listDados[option[0]][3])


st.subheader("Nível Cognitivo Potencializado na Taxonomia de Bloom")
st.write(listDados[option[0]][4])

st.subheader("Competências comportamentais que podem ser desenvolvidas")
st.write(listDados[option[0]][5])