import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import random
import mysql.connector
conexao = mysql.connector.connect(
    passwd='unindo2023',
    port=3306,
    user='unindoUP',
    host='up.cbpypdsteipw.us-east-1.rds.amazonaws.com',
    database= 'UP'
)
mycursor = conexao.cursor()

icone = Image.open(f'Identidade visual/icone.png')
st.set_page_config(
page_title="UP|Planejamento de aulas",
page_icon = icone,
layout="centered")

sql = 'SELECT * FROM Frases;'
mycursor.execute(sql)
listFrases = (mycursor.fetchall())

with st.sidebar:


	st.info(listFrases[random.randint(0,9)][0])


	st.write("---")
	st.error("Idealizado por  [Cárin Pensin](https://www.linkedin.com/in/c%C3%A1rin-fab%C3%ADola-pensin-hahn/) e [Laís Raycik](https://www.linkedin.com/in/la%C3%ADs-raycik-68351946/)")


st.image(Image.open(f'Identidade visual/home.png'))

st.write("")
st.write("")
st.write("")
col1, col2 = st.columns(2)
	
with col1:
	st.info("Faça o download do nosso e-Book de planejamento")
	with open("eBook Planejamento.pdf", "rb") as file:
	    btn = st.download_button(
		    label="Baixar e-Book",
		    data=file.read(),
		    file_name="eBook Planejamento.pdf"
	    )	

with col2:
	st.info("Faça o download do nosso modelo de planejamento")
	with open("Modelo Plano de aula Planejamento Reverso.docx", "rb") as file:
	    btn = st.download_button(
		    label="Baixar Modelo",
		    data=file.read(),
		    file_name="Modelo Plano de aula Planejamento Reverso.docx"
	    )

st.write("---")
st.write("")
st.write("")
st.write("")
st.write("<center>Todos os direitos reservados © 2023 v0.0.1 - UP - Unindo potencialidades",unsafe_allow_html = True)