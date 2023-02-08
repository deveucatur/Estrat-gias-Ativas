import streamlit as st
import pandas as pd
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
page_title="UP | Home",
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
st.title("Bem-vindo(a) ao nosso site!")
st.info("Oferecemos ferramentas e recursos para professores aumentarem assertividade na educação, unindo potencialidades das estratégias ativas de ensino com as principais competências do século XXI e a Taxonomia de Bloom para o sucesso dos alunos. Possibilitando a criação de planos de aula personalizados e desafiantes, acompanhando tendências e novidades na educação para fazer a diferença na vida dos alunos.")
st.write("---")

st.title("Estratégias ativas de ensino")
st.info("Oferecemos mais de 40 estratégias ativas de ensino filtradas por destinação, nível cognitivo da Taxonomia de Bloom e principais competências do século XXI para promover a participação ativa dos estudantes e desenvolver habilidades necessárias para o mundo atual. Professores podem escolher as melhores estratégias para seus alunos e objetivos de aula, explorando a seção e experimentando novas técnicas para melhorar a prática e oferecer uma educação mais significativa e desafiadora.")
st.image(Image.open(f'home/palavrasEstratégias.png'))
st.write("---")
st.title("Competências do Século XXI")
st.info("Apresentamos as principais habilidades e competências  que o Fórum Econômico Mundial definiu para alunos serem bem-sucedidos na sociedade atual, como pensamento crítico, comunicação eficaz, colaboração, criatividade, resolução de problemas. Essas habilidades e competências são desenvolvidas através de estratégias ativas de ensino, que promovem a participação ativa dos estudantes e aplicação prática do conhecimento. Nossas estratégias ativas de ensino são projetadas para desenvolver essas competências de forma significativa e desafiadora, para ser incorporadas na prática de ensino e ajudar os alunos a serem líderes no mundo de hoje.")
st.image(Image.open(f'home/palavrasCompetencias.png'))
st.write("---")

st.title("Nível Cognitivo")
st.info("Mostramos como metodologias ativas são essenciais para o desenvolvimento dos níveis cognitivos da Taxonomia de Bloom (Criar, Aplicar, Entender, Avaliar, Analisar, Relembrar) através de trabalhos em grupo, debates, projetos, jogos e outras atividades. Estas metodologias também ajudam a desenvolver habilidades como pensamento crítico, resolução de problemas, criatividade e colaboração fundamentais para o mundo atual. Descubra como utilizar metodologias ativas para desenvolver níveis cognitivos da Taxonomia de Bloom e melhorar a aprendizagem dos alunos.")
st.image(Image.open(f'home/palavrasCognitivo.png'))
st.write("---")
st.title("Idealizadoras")
col1, col2 = st.columns(2)

with col1:
	st.subheader("Cárin Pensin")
	st.image(Image.open(f'home/carin.png'))
	st.info(""" Sou mulher, mãe, filha, irmã e aluna. Possuo graduação em Farmácia, pós graduação em Manipulação de Produtos Farmacêuticos e Cosméticos, mestrado em Farmacologia e duas pós-graduações na área da educação. Sou especialista em Metodologias Ativas e entusiasta na educação, acreditando na necessidade de mudança no modelo educacional e fazendo parte dessa mudança.
		Sou portanto, especialista em Metodologias Ativas, entusiasta na EDUCAÇÃO! Acredito na necessidade de mudança no modelo educacional e, faço parte da mudança em que acredito! Uma inquieta e curiosa no que se refere ao processo de ensino x aprendizagem!
		Muito Prazer! Esta sou eu!!
		""")
with col2:
	st.subheader("Laís Raycik")
	st.image(Image.open(f'home/lais.png'))
	st.info(""" Com mais de 15 anos de experiência em gestão de pessoas, formação em Psicologia, mestrado em processos psicossociais no trabalho, MBA em Gestão de Negócios, Pós-MBA em TrendsInnovation, atuação em varejo, serviços, indústria e educação, implantando e conduzindo projetos e programas estratégicos com foco em atração, engajamento de talentos, educação corporativa, gestão de carreira e performance e comunicação corporativa, também atua como professora e coordenadora pedagógica de programas de pós-graduação e graduação, além de consultoria, assessoria, mentoria, cursos e workshops para desenvolvimento de pessoas e organizações.
		""")
st.write("---")
st.write("")
st.write("")
st.write("")
st.write("<center>Todos os direitos reservados © 2023 v0.0.1 - UP - Unindo potencialidades",unsafe_allow_html = True)




#user = None
#password = None
#logged_in = False
#
#username = ["admin"]
#password = ["0000"]
#
#
#def login():
#	with placeholder.container():
#		col1, col2, col3 = st.columns(3)
#		with col2:
#			st.image(Image.open(f'home.png'))
#			user_input = st.text_input("Login")
#			pass_input = st.text_input("Senha", type='password')
#
#            #submitted = st.button("Entrar")
#            #if submitted:
#			if user_input in username and pass_input in password:
#				placeholder.success("Login realizado com sucesso")
#				placeholder.empty()
#				return True
#			else:
#				st.error("Insira Usuário e Senha Válidos")
#				return False
#
#
#
#
#placeholder = st.empty()
#
#logged_in = False
#
#if not logged_in:
#    logged_in = login()
#
#if logged_in:
#	PaginaPrincipal()
