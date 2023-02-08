import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from openpyxl import load_workbook



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
page_title="UP|Editar",
page_icon = icone,
layout="centered")





st.image(Image.open(f'Identidade visual/logo UP.png'))


	
sql = 'SELECT * FROM main;'
mycursor.execute(sql)
listDados = (mycursor.fetchall())

tab1, tab2, tab3 = st.tabs(["Alterar", "Adicionar", "Excluir"])

with tab1:
	st.subheader("Alterar")
	#selection = st.selectbox("selecione a estratégia", df["ESTRATÉGIA"])
	selection = st.selectbox("Selecione a estratégia", [x[0] for x in listDados])
	st.write("---")
	option = [x for x in range(len(listDados)) if listDados[x][0] == selection]
	st.subheader("Destinação")
	dest = st.text_area("Colocar Primeira Letra Maiúscula, separado por vírgula e sem espaço. EX:.(Individual, Pares, Pequeno grupo) ", listDados[option[0]][1])
	st.write("---")
	st.subheader("Breve descrição")
	breDes = st.text_area("Breve descrição", listDados[option[0]][2])
	st.write("---")
	st.subheader("Passo a passo didático")
	ppDid = st.text_area("Passo a passo didático",listDados[option[0]][3])
	st.write("---")
	st.subheader("Nível Cognitivo Potencializado na Taxonomia de Bloom")
	NivCog = st.text_area("Colocar Primeira Letra Maiúscula, separado por vírgula e sem espaço. EX:.(Relembrar, Entender) ",listDados[option[0]][4])
	st.write("---")
	st.subheader("Competências comportamentais que podem ser desenvolvidas")
	compC = st.text_area('Colocar Primeira Letra Maiúscula, separado por vírgula e sem espaço. EX:.(Comunicação, Gestão do tempo, Planejamento, Liderança, Relacionamento)',listDados[option[0]][5])
	st.write("---")
	st.subheader("Referências")
	Ref = st.text_area("Referências", listDados[option[0]][6])
	st.write("---")
	if st.button("Alterar"):

		linrow = [dest, breDes, ppDid, NivCog, compC, Ref]

		colunas = ['Destinacao','Descricao','passo_passo', 'cognitivo','competencia','referencia']

		for i in range(len(colunas)):
			sql = f"UPDATE main SET {colunas[i]} = '{linrow[i]}'  WHERE Estrategia = '{selection}'"
			mycursor.execute(sql)
			conexao.commit()

		st.success(f"Atualizado Com Sucesso")


with tab2:
	st.subheader("Criar Nova Estratégia")
	#selection = st.selectbox("selecione a estratégia", df["ESTRATÉGIA"])
	Nome = st.text_input("Nome da Estratégia")
	st.write("---")
	st.subheader("Destinação")
	dest = st.text_area("Colocar Primeira Letra Maiúscula, separado por vírgula e sem espaço. EX:.(Individual, Pares, Pequeno grupo) ")
	st.write("---")
	st.subheader("Breve descrição")
	breDes = st.text_area("Breve descrição")
	st.write("---")
	st.subheader("Passo a passo didático")
	ppDid = st.text_area("Passo a passo didático")
	st.write("---")
	st.subheader("Nível Cognitivo Potencializado na Taxonomia de Bloom")
	NivCog = st.text_area("Colocar Primeira Letra Maiúscula, separado por vírgula e sem espaço. EX:.(Relembrar, Entender) ")
	st.write("---")
	st.subheader("Competências comportamentais que podem ser desenvolvidas")
	compC = st.text_area('Colocar Primeira Letra Maiúscula, separado por vírgula e sem espaço. EX:.(Comunicação, Gestão do tempo, Planejamento, Liderança, Relacionamento)')
	st.write("---")
	st.subheader("Referências")
	Ref = st.text_area("Referências", )
	st.write("---")
	if st.button("Criar"):
		sql = f'''INSERT INTO main 
        (Estrategia ,Destinacao,Descricao,passo_passo, cognitivo,competencia,referencia ) 
        VALUES ('{Nome}','{dest}','{breDes}','{ppDid}','{NivCog}','{compC}','{Ref}');'''

		mycursor.execute(sql)
		conexao.commit()
		st.success(f"Nova Estratégia Criada Com Sucesso")


with tab3:
	st.subheader("Excluir")
	#selection = st.selectbox("selecione a estratégia", df["ESTRATÉGIA"])
	selection = st.selectbox("Selecione a estratégia para Excluir", [x[0] for x in listDados])
	st.write("---")

	if st.button("Excluir"):
		sql = f"DELETE FROM main  WHERE Estrategia = '{selection}';"

		mycursor.execute(sql)
		conexao.commit()
		st.success(f"Estratégia Excluida Com Sucesso")



st.write("")
st.write("")
st.write("")
st.write("<center>Todos os direitos reservados © 2023 v0.0.1 - UP - Unindo potencialidades",unsafe_allow_html = True)
