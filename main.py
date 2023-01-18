import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


icone = Image.open(f'icone.png')
st.set_page_config(
page_title="UP | UNINDO POTENCIALIDADES",
page_icon = icone,
layout="centered")





with st.sidebar:
	col1, col2,col3  = st.columns((1,2,1))
	with col2:
		st.image(icone,width = 100)

	st.write("<center>Planeje suas aulas com assertividade!",unsafe_allow_html = True)

	add_radio = st.radio("", ("Home", "UP | UNINDO POTENCIALIDADES"))
	
	st.write("---")
	st.info("""*A educação é a arma mais poderosa que você pode usar para mudar o mundo.* 

				Nelson Mandela""")
	#st.write("---")
	st.info("Idealizado por  [Cárin Pensin](https://www.linkedin.com/in/c%C3%A1rin-fab%C3%ADola-pensin-hahn/) e [Laís Raycik](https://www.linkedin.com/in/la%C3%ADs-raycik-68351946/)")
	

if add_radio == "Home":
	st.image(Image.open(f'home.png'))
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









if add_radio == "UP | UNINDO POTENCIALIDADES":
	st.image(Image.open(f'logo UP.png'))
	#st.title("UP | UNINDO POTENCIALIDADES")
	#st.write("---")

	df = pd.read_excel("UP2.xlsx", sheet_name = "Página2")
	df1 = pd.read_excel("UP2.xlsx", sheet_name = "Página1")
	listDadosCompet = df1.values.tolist()
	df2 = pd.read_excel("UP2.xlsx", sheet_name = "Página3")
	listDadosCogn = df2.values.tolist()

	listDados = df.values.tolist()
	for i in range(len(listDados)):
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
