import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import time
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
page_title="UP| Estratégias Ativas",
page_icon = icone,
layout="centered")

sql = 'SELECT * FROM Frases;'
mycursor.execute(sql)
listFrases = (mycursor.fetchall())

with st.sidebar:


	st.info(listFrases[random.randint(0,9)][0])


	st.write("---")
	st.error("Idealizado por  [Cárin Pensin](https://www.linkedin.com/in/c%C3%A1rin-fab%C3%ADola-pensin-hahn/) e [Laís Raycik](https://www.linkedin.com/in/la%C3%ADs-raycik-68351946/)")




st.image(Image.open(f'Identidade visual/logo UP.png'))




sql = 'SELECT * FROM desc_Competencias;'
mycursor.execute(sql)
listDadosCompet = (mycursor.fetchall())

sql = 'SELECT * FROM desc_cognitivo;'
mycursor.execute(sql)
listDadosCogn = (mycursor.fetchall())

sql = 'SELECT * FROM main;'
mycursor.execute(sql)
listDados = (mycursor.fetchall())





for i in range(len(listDados)):
    listDados[i] = list(listDados[i])
    listDados[i][1] = listDados[i][1].replace(", ",",").split(",")
    listDados[i][4] = listDados[i][4].replace(", ",",").split(",")
    listDados[i][5] = listDados[i][5].replace(", ",",").split(",")


col1, col2 = st.columns(2)
with col1:	
	desList = set([item.replace(".","") for sublista in [x[1]  for x in listDados] for item in sublista])
	destinação = st.multiselect('Destinação', desList, desList)
with col2:	
	cogList = set([item.replace(".","") for sublista in [x[4]  for x in listDados] for item in sublista])
	cognitivo = st.multiselect('Cognitivo', cogList, cogList)
compList = set([item.replace(".","") for sublista in [x[5]  for x in listDados] for item in sublista])
competencias = st.multiselect('Competências', compList, compList)
#selection = st.selectbox("selecione a estratégia", df["ESTRATÉGIA"])
selection = st.selectbox("Selecione a estratégia", [x[0] for x in listDados if len(set(x[1]).intersection(destinação)) > 0 and len(set(x[4]).intersection(cognitivo)) > 0 and len(set(x[5]).intersection(competencias)) > 0])
if selection != None:
	if st.button('Buscar'):
		st.write("---")
		#option = [x for x in range(len(df["ESTRATÉGIA"])) if df["ESTRATÉGIA"][x] == selection]
		option = [x for x in range(len(listDados)) if listDados[x][0] == selection]
		st.subheader("Destinação")
		#st.write(listDados[option[0]][1])
		if len(listDados[option[0]][1]) == 2:
			col1, col2, col3 = st.columns(3)
		elif len(listDados[option[0]][1]) == 3:
			col1, col2,col3 = st.columns(len(listDados[option[0]][1]))
		elif len(listDados[option[0]][1]) == 4:
			col1, col2,col3, col4 = st.columns(len(listDados[option[0]][1]))
		if len(listDados[option[0]][1]) == 1:
			col1, col2,col3 = st.columns(3)
			with col1:
				st.image(Image.open(f'destinação/{listDados[option[0]][1][0]}.jpg') )
		if len(listDados[option[0]][1]) > 1:
			with col1:
				st.image(Image.open(f'destinação/{listDados[option[0]][1][0]}.jpg'))
			with col2:
				st.image(Image.open(f'destinação/{listDados[option[0]][1][1]}.jpg'))
			if len(listDados[option[0]][1]) > 2:
				with col3:
					st.image(Image.open(f'destinação/{listDados[option[0]][1][2]}.jpg'))
				if len(listDados[option[0]][1]) > 3:
					with col4:
						st.image(Image.open(f'destinação/{listDados[option[0]][1][3]}.jpg'))
			
		st.write("---")
		st.subheader("Breve descrição")
		st.write(listDados[option[0]][2])
		st.write("---")
		st.subheader("Passo a passo didático")
		st.write(listDados[option[0]][3])
		st.write("---")
		st.subheader("Nível Cognitivo Potencializado na Taxonomia de Bloom")
		#st.write(listDados[option[0]][4])
		categories = ['Relembrar', 'Entender', 'Aplicar', 'Analisar', 'Avaliar', 'Criar']
		values = [50, 45, 40, 35, 30, 25]
		colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow']
		colorsf = ['w', 'k', 'k', 'w', 'k', 'k']
		for i in range(len(colors)):
			if categories[i] not in listDados[option[0]][4]:
				colors[i] = "whitesmoke"
				colorsf[i] = "silver"
		def plotCogn():
			plt.figure(figsize=(20,10))
			plt.barh(categories, values, color=colors, height= 0.95, left = [0, 2.5, 5, 7.5, 10, 12.5])
			for i, v in enumerate([[25,categories[x]] for x in range(6)]):
			    plt.text(v[0], i, str(v[1]), color = colorsf[i], fontsize = 25, fontweight='bold', va = "center", ha = "center")
			plt.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False)
			plt.axis('off')
			st.set_option('deprecation.showPyplotGlobalUse', False)
		st.pyplot(plotCogn())
		def plotCogn2(cog):
			col1, col2 = st.columns((1,3))
			with col1:
				#st.image(Image.open(f'competências/{cog}.jpg'))
				st.subheader(cog)
			with col2:
				for j in listDadosCogn:
					if j[1] == cog:
						st.write(j[2])
		for i in listDados[option[0]][4]:
			plotCogn2(i)
		st.write("---")
		st.subheader("Competências comportamentais que podem ser desenvolvidas")
		#st.write(listDados[option[0]][5])
		def plotCompetencias(compt):
			col1, col2 = st.columns((1,3))
			with col1:
				st.image(Image.open(f'competências/{compt}.jpg'))
			with col2:
				for j in listDadosCompet:
					if j[1] == compt:
						st.write("")
						st.write(j[2])
		for i in listDados[option[0]][5]:
			plotCompetencias(i)
		st.write("---")
		st.subheader("Referências")
		st.write(listDados[option[0]][6])
st.write("---")
st.write("")
st.write("")
st.write("")
st.write("<center>Todos os direitos reservados © 2023 v0.0.1 - UP - Unindo potencialidades",unsafe_allow_html = True)