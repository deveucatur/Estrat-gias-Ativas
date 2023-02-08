import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from openpyxl import load_workbook


icone = Image.open(f'Identidade visual/icone.png')
st.set_page_config(
page_title="UP|Planejamento de aulas",
page_icon = icone,
layout="centered")



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