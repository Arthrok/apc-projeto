from html.entities import html5
from click import style
import dash 
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash import callback_context, no_update

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import json

####### 

#Array e dicicionários vazios para usar depois

anos = {}
ns = []
opcoes = {}

#Dicionários para usar no dropdown (selecionar)
#Estrutura dicionário -> dict = {"chave":"valor"}

geral1 = {"Desmatamento no Mundo":"Desmatamento no Mundo"}
america1 = {"Queimadas na América do Norte":"Queimadas na América do Norte"}
brasil1 = {'Desmatamento na Amazônia':"Desmatamento na Amazônia", 'Desmatamento no Cerrado':"Desmatamento no Cerrado"}
euro1 = {'Desmatamento na Europa':"Desmatamento na Europa"}
euro_op = {'1990-2000':"1990-2000", "2000-2010":"2000-2010", "2010-2015":"2010-2015"}
conti_an = {1990:"1990", 2000:"2000", 2010:"2010", 2015:"2015"}
brasil_ce = {2019:"2019", 2020:"2020", 2021:"2021", "todos os anos":"todos os anos"}
brasil_am ={1998:"1998", 1999:"1999", "2000": "2000", 2001:"2001", 2002:"2002", 2003:"2003", 2004:"2004", 2005:"2005", 2006:"2006", 2007:"2007", 2008:"2008", 2009:"2009", 2010:"2010", 2011:"2011", 2012:"2012", 2013:"2013", 2014:"2014", "todos os anos":"todos os anos"}

###################### gráficos

maps = json.load(open("continente.json", "r")) #arquivo .json do mapa (gráfico 2)



### Dataframes para o mapa
dt = pd.read_csv("https://raw.githubusercontent.com/Arthrok/cerrado/main/cerrado%20(2).csv") #Cerrado
dk = pd.read_csv("https://raw.githubusercontent.com/Arthrok/cerrado/main/amazoniaestados.csv") #Amazonia
df = pd.read_csv('https://raw.githubusercontent.com/Dtcbsb/projeto/main/forestAreaChange.csv') #Europa
dn = pd.read_csv('https://raw.githubusercontent.com/LORliveira/desmatamento/main/Desmatamento%20dos%20continentes') #Continente




#cods do cerrado
tt1 = dt.values
ns, c3, v1, v2, v3, h1, h2, h3 = []




#cods da amazônia
dk['qnt'] = dk['qnt'].astype(float)
tt2 = dk.values


#cods europa
tt4 = df.values
vetor1 = [] 


#cods continente
tt3 = dn.values


for element in h1:
    if element not in h3:
        h3.append(element)
            

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])


app.layout = dbc.Container(
    dbc.Row([
            dbc.Row([
                html.Div([
                    html.H2('Desmatamento - Uma comparação: Brasil x Mundo', style={"text-align":"center",})
                ], id="header", style={"opacity":"80%", "border-radius":"10px"})
            ]),
            dbc.Row([   ## Coluna dos integrantes do grupo e texto
                dbc.Col([ 
                    dbc.Row ([
                        dbc.Col ([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Arthur Alves Melo', style={"color": "#FFFFFF"}),
                                    html.H6( '211007856', style={"color": "#FFFFFF"}),               
                                ]),
                            ], style={"background-color":"rgb(144, 179, 64)", "border-radius":"25px", "opacity":"65%"}),
                        ]),    
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Arthur L. Mercadante', style={"color": "#FFFFFF"}),
                                    html.H6( '202028730', style={"color": "#FFFFFF"}),   
                                ])
                            ], style={"background-color":"rgb(144, 179, 64)", "border-radius":"25px", "opacity":"65%"})
                        ]),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Davi Toledo da Costa', style={"color": "#FFFFFF"}),
                                    html.H6( '180118838 ', style={"color": "#FFFFFF"}),   
                                ])
                            ], style={"background-color":"rgb(144, 179, 64)", "border-radius":"25px", "opacity":"65%"})
                        ]),                                                                                                                                         
                    ], id="n1"),
                    dbc.Row ([
                        dbc.Col ([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Filipe Ferreira Pereira', style={"color": "#FFFFFF"}),
                                    html.H6( '211061734', style={"color": "#FFFFFF"}),   
                                ]),
                            ], style={"background-color":"rgb(144, 179, 64)", "border-radius":"25px", "opacity":"65%"}),
                        ]),    
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Henrique M. Alencar', style={"color": "#FFFFFF"}),
                                    html.H6( '211061860', style={"color": "#FFFFFF"}),   
                                ])
                            ], style={"background-color":"rgb(144, 179, 64)", "border-radius":"25px", "opacity":"65%"})
                        ]),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Henrique M. Fortes', style={"color": "#FFFFFF"}),
                                    html.H6( '211061879', style={"color": "#FFFFFF"}),   
                                ])
                            ], style={"background-color":"rgb(144, 179, 64)", "border-radius":"25px", "opacity":"65%"})
                        ]),                                                                                                                                         
                    ], id="n2"),
                    dbc.Row ([
                        dbc.Col ([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Lucas O. Rodrigues', style={"color": "#FFFFFF"}),
                                    html.H6( '202017684', style={"color": "#FFFFFF"}),   
                                    
                                ]),
                            ], style={"background-color":"rgb(144, 179, 64)", "border-radius":"25px", "opacity":"65%"}),
                        ]),    
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Pedro Pinheiro Saad ', style={"color": "#FFFFFF"}),
                                    html.H6( '211062393', style={"color": "#FFFFFF"}),   
                                ])
                            ], style={"background-color":"rgb(144, 179, 64)", "border-radius":"25px", "opacity":"65%"})
                        ]),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Img(src=("https://cdn-icons-png.flaticon.com/512/711/711769.png"), height=51),
                                    html.H6( 'Walker D. A. Andrade', style={"color": "#FFFFFF"}),
                                    html.H6( '190096748', style={"color": "#FFFFFF"}),   
                                ])
                            ], style={"background-color":"rgb(144, 179, 64)", "border-radius":"25px", "opacity":"65%"})
                        ]),                                                                                                                                         
                    ], id="n3"),                                                                                                                         
                ], md=5),
                dbc.Col([
                    dbc.Card ([
                        dbc.CardBody([
                            html.Span(
                                'Em prol do desenvolvimento tecnológico, a humanidade vem utilizando recursos naturais, tanto como matéria-prima, quanto como fonte energética. Como por exemplo, carvão, que é utilizado como combustível para diversas indústrias, e como matriz energética. Outro exemplo é a madeira, que tem diversos usos, em sua forma bruta, como matéria-prima para construções e artesanatos, em uma forma processada, pode se tornar papel, carvão vegetal, entre outras coisas.'
                                'No entanto, nos últimos 50 anos, surgiu uma discussão sobre a extração desmedida e desenfreada dos recursos naturais. Isso é decorrente de diversos estudos científicos relacionados ao aquecimento global. Um estudo que nos diz que as mudanças de temperatura no nosso planeta estão aumentando de frequência e intensidade, e que a tendência é que isso continue a aumentar se não nos dispusermos a controlar a extração e consumo de recursos naturais.'
                                'Dentre todos os problemas que ocorrem para a progressão do aquecimento global, um dos que nos chamam mais atenção é o desmatamento e as queimadas ilegais. '
                                'A gravidade do desmatamento se torna mais evidente quando pensamos que as árvores, colocadas como o pulmão do mundo, filtradoras de ar, grandes responsáveis pela manutenção de gases na atmosfera, como o oxigênio e gás carbônico, esse último sendo um dos responsáveis pela deterioração da camada de ozônio.'
                                'A UN FAO (Organização das Nações Unidas para Alimentação e Agricultura), estima que, desde 2010, 10 milhões de hectares de floresta foram derrubadas por ano, o pior é que, graças a essa mesma instituição, podemos afirmar que aproximadamente 50%, do número de arvores cortadas, foram plantadas para reflorestamento.'
                                'É importante dizer que apesar de termos trazido atenção para esse problema apenas no último século, o desflorestamento é algo que sempre esteve presente na história da humanidade, de toda a área terrestre do planeta apenas 71% é habitável, os outros 29% são inviáveis para vida humana de maneira sustentável, devido a gelo, desertos, entre outros problemas.'
                                'Pesquisas indicam que a 10.000 anos atrás, aproximadamente 57% dessa área era coberta em florestas, o equivalente a 6 Bilhões de Hectares, hoje em dia, no entanto, temos somente 4 Bilhões restantes. '
                                'Isso nos leva a seguinte reflexão, todo esse consumo de recursos naturais, foi sem sombra de dúvidas necessário para o desenvolvimento humano, e se não tomarmos cuidado esse recurso finito irá se esgotar, no entanto é possível que países subdesenvolvidos e em desenvolvimento, consigam crescer e competir com países que tiveram tempo para usufruir desses recursos sem se importar com o tamanho do consumo? '
                                'Para ponderarmos sobre essa pergunta trouxemos dados sobre o desflorestamento no nível continental, passando por países desenvolvidos do continente europeu, e por ultimo trazendo para algumas regiões do brasil, para uma comparação em escala reduzida a algumas décadas. '
                            )
                        ])
                    ], id="texto"),
                ],md=7),
            ]),

            html.Div([ 
                html.Br(),  ## Quebra de linha
                html.Br()
            ]),
            dbc.Row([
                    html.Div([ ## Botões
                        dbc.Button("Geral", color="primary", id="but-geral", size="lg", n_clicks=0),
                        dbc.Button("América do Norte", color="primary", id="but-america", size="lg", n_clicks=0),
                        dbc.Button("Brasil", color="primary", id="but-brasil", size="lg", n_clicks=0),
                        dbc.Button("Europa", color="primary", id="but-europa", size="lg", n_clicks=0),
                    ], id="b1"),
                    
            ]),
            html.Div([
                html.Br()
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Row ([      ##Dropdown
                        dbc.Col ([
                            dcc.Dropdown(id="drop1", placeholder="Selecione o local",
                                options=[{"label": j, "value": i} for i, j in opcoes.items()], #j recebe a chave do dicicionário e j recebe o valor
                                style={"margin-top": "10px"},
                                clearable=True
                                ),                        
                        ], id="select1"),
                        dbc.Col ([
                            dcc.Dropdown(id="drop2", placeholder="Selecione o ano",
                            options=[{"label": j, "value": i} for i, j in anos.items()], #j recebe a chave do dicicionário e j recebe o valor
                            style={"margin-top": "10px"},
                            clearable=True,
                        
                            ),                        
                        ], id="select2"), 
                    ]),
                    dcc.Loading(children=[
                        dcc.Graph(id="graph1", style={"height":"50vh"})
                        ]) ,             
                ],md=6),
                dbc.Col([
                    html.Div([
                        html.Br(),
                        html.Br(),
                    ]),
                    dcc.Loading(children=[

                        dcc.Graph(id="graph2", style={"height": "50vh", "margin-right": "10px", "bottom":"400px"})
                        ])

                ],md=6),

            ], id = "corpo2"),
            html.Div([
                html.Br()
            ]),
            dbc.Row([
                dbc.Card ([
                    dbc.CardBody([
                        html.Span (
                            'Após analisarmos os gráficos percebemos que as áreas consideradas como as menos desenvolvidas, tiveram um maior índice de desmatamento de até 10x maior que as áreas mais desenvolvidas. '
                            'Isso pode ser atribuído a diversos fatores, o primeiro, é o fato que esses países já possuem uma flora mais devastada, com poucas áreas florestadas restantes, o que impossibilita a extração, e favorece a exportação entre diversos países. O segundo fator é a não necessidade de extração de madeiras, utilizada apenas de maneira não-industrial, o que pode ser sustentada, como dito no item anterior, pela importação de madeira vinda de países em desenvolvimento.'
                            'No entanto, a informação mais importante a ser extraída desses gráficos é, que o número de hectares desmatados vem diminuindo nos últimos 5 anos, porém é importante notar que devido a queimadas acidentais recentes, a área desmatada teve um pico momentâneo na área da Oceania, e na Amazônia brasileira.'
                            'Por último é importante ressaltar que enquanto o tamanho da área desmatada é importante, o real valor está no “Net forest Conversion”, que é uma simples conta que considera os hectares desmatados e o tamanho da área replantada. Esse número infelizmente permanece por volta dos 50% nos últimos 15 anos, de acordo com a UN FAO.'
                        )
                    ])
                ], id="final"),
            ]),
        ], id="pai2"),
fluid=True, id="pai1")



@app.callback( ## Toda vez que clicar em algum dos botões, o dropdown é redefinido ; as opções estão armazenadas em country1 e opcoes assume o valor ao clicar em algum botão
    Output('drop1', 'options'),
    Input('but-brasil', 'n_clicks'), Input('but-geral', 'n_clicks'), Input('but-europa', 'n_clicks'), Input('but-america', 'n_clicks'))
def butsgeral(bras, geral, euro, eua):
    global opcoes #opcoes é um dicionário vazio que vai receber valores de acordo com o botão a ser clicado, o global é pra não dar erro de escopo
    changed_id = [p['prop_id'] for p in callback_context.triggered][0] #atualiza a callback caso outro botão seja clicado
    if 'but-brasil' in changed_id:
        opcoes = brasil1    #brasil1, geral1, euro1, america1 são dicionários definidos anteriormente
    if 'but-geral' in changed_id:
        opcoes = geral1
    if 'but-europa' in changed_id:
        opcoes = euro1
    if 'but-america' in changed_id:
        opcoes = america1
    return opcoes
   

@app.callback( #essa callback considera a opção escolhida no primeiro select, e manda pro segundo select opções de anos de acordo com o primeiro select
    Output('drop2', 'options'),
    Input('drop1', 'value'))
def define_ano(year):
    global anos #anos é um dicionário vazio, o global é pra não dar erro de escopo
    if year == "Desmatamento no Cerrado":
        anos = brasil_ce #anos recebe uma lista de opções definidas em brasil_ce
    if year == "Desmatamento na Amazônia":
        anos = brasil_am
    if year == "Desmatamento na Europa":
        anos = euro_op
    if year == "Desmatamento no Mundo":
        anos = conti_an
    return anos

@app.callback ( #o primeiro gráfico é atualizado de acordo com as opções escolhidas no select 1  e 2
    Output('graph1', 'figure'),
    Input('drop2', 'value'), Input('drop1', 'value'), Input('drop1', 'value'), Input('drop1', 'value'), Input('drop1', 'value'))
def cerrado(ano_select, cerra, amaz, europ, geral):

##### MUNDO
    if geral == "Desmatamento no Mundo":
        v1 = [] #armazena os estados
        v2 = [] #armazena o valor de desmatamento
        v3 = [] #armazena os estados não filtrados
        for i in range (len(tt3)): #linhas de dados
            v3.append(tt3[i][0]) 
            if tt3[i][1] == int(ano_select): 
                v2.append(tt3[i][2]) 
        for element in v3:
            if element not in v1:
                v1.append(element)
        c1 = v1
        c2 = v2
        c3 = v3
        title_e = "Desmatamento por Continente"
        xaxis = "Continente"
        yaxis = "Área Desmatada"

##### CERRADO
    if cerra == "Desmatamento no Cerrado":
        v1 = []
        v2 = []
        v3 = []
        for i in range (len(tt1)): 
            v3.append(tt1[i][0]) 
            if tt1[i][2] == int(ano_select): 
                v2.append(tt1[i][1]) 
        for element in v3:
            if element not in v1:
                v1.append(element)
        c1 = v1
        c2 = v2
        c3 = v3
        title_e = "Área de Desmatamento no Cerrado"
        xaxis = "Estado"
        yaxis = "Área Desmatada (Km2)"

##### AMAZÔNIA
    if amaz == "Desmatamento na Amazônia":
        v1 = []
        v2 = []
        v3 = []
        for i in range (len(tt2)): 
            v3.append(tt2[i][1]) 
            if tt2[i][2] == int(ano_select): 
                v2.append(tt2[i][3]) 
        for element in v3:
            if element not in v1:
                v1.append(element)
        c1 = v1
        c2 = v2
        c3 = v3
        title_e = "Área de Desmatamento na Amazônia"
        xaxis = "Estado"
        yaxis = "Área Desmatada (Km2)"

##### EUROPA
    if europ == "Desmatamento na Europa":
        v1 = []
        v2 = []
        v3 = []
        for i in range (len(tt4)): 
            v3.append(tt4[i][0]) 
            if tt4[i][1] == ano_select: 
                v2.append(tt4[i][2]) 

        for element in v3:
            if element not in v1:
                v1.append(element)
        c1 = v2
        c2 = v1
        c3 = v3 
        title_e = "Desmatamento na Europa"
        xaxis = "Área Desmatada em Hectares"
        yaxis = "Países"

##### FIG
    fig = px.bar(c3, x = c1, y = c2, barmode='group', 
                labels = {'0': 'Continente', '1' :'Ano', '2':'Desmatamento'},
                title = 'Perca de áreas florestais por continente')
    fig.update_layout(barmode='group', xaxis_tickangle=-45, font_color = 'white', paper_bgcolor="#242424", 
                plot_bgcolor="#242424", title=title_e, xaxis_title=xaxis, yaxis_title=yaxis
                        )
    return fig

@app.callback ( #callback do segundo mapa, leva em consideração os valores selecionados em select1 e select2,
    Output('graph2', 'figure'),
    Input('drop2', 'value'), Input('drop1', 'value'), Input('drop1', 'value'), Input('drop1', 'value'), Input('drop1', 'value'))
def amazonia(ano_selects, cerra, amaz, europ, conti):

##### EUROPA
    if europ == "Desmatamento na Europa": #verifica se a opção no select 1 para passar as próximas variáveis pro mapa
        v1 = [] #armazena os estados sem repetição
        v2 = [] #armazena os valores
        v3 = [] #armazena os estados
        for i in range (len(tt4)): 
            v3.append(tt4[i][0]) 
            if tt4[i][1] == ano_selects: 
                v2.append(tt4[i][2]) 

        for element in v3: #filtra os elementos repetidos em v3 e separa para armazenar em v1
            if element not in v1:
                v1.append(element)
        k1 = v1 #locations do mapa
        k2 = v2 #valor desmatado pro mapa
        k3 = v3 #k3 ocupa o dataframe do mapa
        lt, ln = 58.46, 15.59 #define latitude e longitude no mapa
        
##### AMAZÔNIA
    if amaz == "Desmatamento na Amazônia":
        v1 = []
        v2 = []
        v3 = []
        for i in range (len(tt2)): 
            v3.append(tt2[i][1]) 
            if tt2[i][2] == int(ano_selects): 
                v2.append(tt2[i][3]) 
        for element in v3:
            if element not in v1:
                v1.append(element)
        k1 = v1
        k2 = v2
        k3 = v3 
        lt, ln = -16.95, -47.78

##### CERRADO    
    if cerra == "Desmatamento no Cerrado":
        v1 = []
        v2 = []
        v3 = []
        for i in range (len(tt1)): 
            v3.append(tt1[i][0]) 
            if tt1[i][2] == int(ano_selects): 
                v2.append(tt1[i][1]) 
        for element in v3:
            if element not in v1:
                v1.append(element) 
        k1 = v1
        k2 = v2
        k3 = v3
        lt, ln = -16.95, -47.78

##### MUNDO
    if conti == "Desmatamento no Mundo": 
        v1 = []
        v2 = []
        v3 = []
        for i in range (len(tt3)): #linhas de dados
            v3.append(tt3[i][0]) 
            if tt3[i][1] == int(ano_selects): 
                v2.append(tt3[i][2]) 
        for element in v3:
            if element not in v1:
                v1.append(element)
        k1 = v1
        k2 = v2
        k3 = v3
        lt, ln = 31.58, 119.77

##### FIG
    fig2 = px.choropleth_mapbox(k3, locations=k1, color=k2,
                        center={"lat": lt, "lon": ln}, zoom=3.2,
                            geojson=maps, color_continuous_scale="turbid", opacity=0.4,
                        )
    fig2.update_layout(
        paper_bgcolor="rgb(170, 211, 223)", 
        autosize=True, 
        margin = go.Margin(l=0, r=0, t=0, b=0),
        showlegend = False,
        mapbox_style="open-street-map",
        font_color = 'white'
    )



    return fig2





if __name__ == '__main__':
    app.run_server(debug=True)


