#Importa as bibliotecas
import math
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from bokeh.plotting import figure
from bokeh.models.ranges import Range1d
from bokeh.models import LinearAxis
from bokeh.models import LabelSet
from bokeh.models import ColumnDataSource

#Define a configuração da página (aba do navegador)
st.set_page_config(page_title="Calculadora de Mínimo Efeito Detectável",
                   page_icon="https://companieslogo.com/img/orig/BBD-6b19aac5.png?t=1654497020",
                   layout="centered",
                   initial_sidebar_state="auto",
                   menu_items=None)

roboto = {"fontname": "Roboto", "size": "11"}
roboto_light = {"fontname": "Roboto", "size": "10", "weight": "light"}
roboto_title = {"fontname": "Roboto", "size": "12", "weight": "bold"}
roboto_small = {"fontname": "Roboto", "size": "7.5", "weight": "light"}

font = {"family": "sans-serif", "sans-serif": "roboto", "size": 11}

plt.rc("font", **font)

#Título da página
st.title("Calculadora de Mínimo Efeito Detectável")

#Descrição abaixo do título
st.write("Este aplicativo calcula o Efeito Mínimo Detectável (MDE) para testes de taxa de conversão com base no nível de significância estatística e poder, número de semanas no experimento, taxa de conversão do controle, tamanho da amostra por semana e número de variantes. Caso você tenha alguma dúvida sobre o cálculo foi feito, visite a página **'Cálculo'**. Para saber mais sobre os conceitos utilizados nesse app, visite a página **'Conceitos e Definições'**.")

#Define os inputs utilizados no Streamlit
sample_per_variant = st.number_input("Amostra por variante por semana:", value=1000, step=100, min_value=100, max_value=1000000)
base_conversion = st.number_input("Conversão do controle (%):", value=1.0, step=0.1, min_value=0.1, max_value=100.0) / 100
num_weeks = st.slider("Número de semanas do experimento", value=4, step=1, min_value=1, max_value=20)

#Define a função que calcula o MDE
def calculate_mde(p, n):
    return math.sqrt((1/p - 1)/(n/16))

#Calcula o MDE para cada semana e armazena em uma lista
mde_data = []
for week in range(1, num_weeks+1):
    total_sample = sample_per_variant * week
    mde = calculate_mde(base_conversion, total_sample)
    mde_data.append({'Semana do experimento': week, 'Amostra por variante': total_sample, 'MDE': round(mde*100, 2)})

#Converte a lista em um dataframe
mde_df = pd.DataFrame(mde_data)

#Mostra a tabela
#st.write(mde_df)
mde_df = mde_df.reset_index(drop=True)
st.dataframe(mde_df, use_container_width=True)

#Gera a figura do gráfico MDE x Semana
y_overlimit = 0.05
p = figure(title="Efeito Mínimo Detectável (MDE) por semana", 
           x_axis_label="Semana do experimento", 
           y_axis_label="MDE (%)",
           plot_width=600,
           plot_height=400)

#Seta os ticks do eixo x de 1 em 1
p.xaxis.ticker = mde_df['Semana do experimento']

#Adiciona o grid x e y na cor whitesmoke à figura
p.xgrid.grid_line_color = 'whitesmoke'
p.ygrid.grid_line_color = 'whitesmoke'


#Cria o eixo y secundário - Amostra por variante (Ordem invertida para ajustar os elemtnos do gráfico)
y_column2_range = 'Semana do experimento' + "_range"
p.extra_y_ranges = {y_column2_range: Range1d(start=mde_df['Amostra por variante'].min() * (1 - y_overlimit),end=mde_df['Amostra por variante'].max() * (1 + y_overlimit))}
p.add_layout(LinearAxis(y_range_name=y_column2_range, axis_label="Amostra por variante"), "right")
sample_bar = p.vbar(mde_df['Semana do experimento'], 
                    top=mde_df['Amostra por variante'], 
                    legend_label="Amostra por variante",
                    width=0.8,
                    alpha=0.3,
                    color='silver',
                    y_range_name=y_column2_range)

#Cria o eixo y primário - MDE (%) (Ordem invertida para ajustar os elemtnos do gráfico)
mde_line = p.line(mde_df['Semana do experimento'], 
                  mde_df['MDE'], 
                  legend_label="MDE (%)", 
                  color='lightcoral',
                  line_width=3)


#Cria a source para os labels
labels_source = ColumnDataSource(data=dict(
    x=mde_df['Semana do experimento'],
    y=mde_df['MDE'],
    label=mde_df['MDE'].astype(str) + '%'
))

#Adiciona o label no gráfico (eixo y primário)
labels = LabelSet(x='x', y='y', text='label', y_offset=8, source=labels_source,
                  text_font_size="8pt", text_color="dimgray")
p.add_layout(labels)

p.y_range = Range1d(mde_df['MDE'].min() * (1 - y_overlimit), mde_df['MDE'].max() * (1 + y_overlimit))

#Seta o tamanho das fontes dos labels e das legendas
p.xaxis.axis_label_text_font_size = "12pt"
p.yaxis.axis_label_text_font_size = "12pt"
p.legend.label_text_font_size = "12pt"

#Adiciona espaços ao gráfico
p.legend.location = "top_left"
p.legend.spacing = 10
p.legend.padding = 5

#Plota o gráfico
st.bokeh_chart(p, use_container_width=True)
