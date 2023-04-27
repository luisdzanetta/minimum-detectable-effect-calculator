import math
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from bokeh.plotting import figure
from bokeh.models.ranges import Range1d
from bokeh.models import LinearAxis

#Define a configuração da página
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

#Título e descrição da página
st.title("Calculadora de Mínimo Efeito Detectável")
st.write("Este aplicativo calcula o Efeito Mínimo Detectável (MDE) para testes de taxa de conversão com base no nível de significância estatística e poder, número de semanas no experimento, taxa de conversão do controle, tamanho da amostra por semana e número de variantes. Caso você tenha alguma dúvida sobre o cálculo foi feito, visite a página **'Cálculo'**. Para saber mais sobre os conceitos utilizados nesse app, visite a página **'Conceitos e Definições'**.")

# Define the inputs using Streamlit widgets
sample_per_variant = st.number_input("Amostra por variante por semana:", value=1000, step=100, min_value=100, max_value=1000000)
base_conversion = st.number_input("Conversão do controle (%):", value=1.0, step=0.1, min_value=0.1, max_value=100.0) / 100
num_weeks = st.slider("Número de semanas do experimento", value=4, step=1, min_value=1, max_value=20)

# Define the MDE function
def calculate_mde(p, n):
    return math.sqrt((1/p - 1)/(n/16))


# Calculate the MDE for each week and store the data in a list of dictionaries
mde_data = []
for week in range(1, num_weeks+1):
    total_sample = sample_per_variant * week
    mde = calculate_mde(base_conversion, total_sample)
    mde_data.append({'Semana do experimento': week, 'Amostra por variante': total_sample, 'MDE': mde*100})

# Convert the list of dictionaries to a Pandas dataframe
mde_df = pd.DataFrame(mde_data)

# Display the table
#st.write(mde_df)
st.dataframe(mde_df, use_container_width=True)

#Gráfico 1 | MDE x semana
y_overlimit = 0.05
p = figure(title="Efeito Mínimo Detectável (MDE) por Semana", 
           x_axis_label="Semana do Experimento", 
           y_axis_label="MDE (%)",
           plot_width=600,
           plot_height=400)

# Add grid lines for both the x and y grids
p.xgrid.grid_line_color = 'whitesmoke'
p.ygrid.grid_line_color = 'whitesmoke'


#Second axis (Amostra por variante. Ordem invertida para ajustar elemtnos do gráfico)
y_column2_range = 'Semana do experimento' + "_range"
p.extra_y_ranges = {y_column2_range: Range1d(start=mde_df['Amostra por variante'].min() * (1 - y_overlimit),end=mde_df['Amostra por variante'].max() * (1 + y_overlimit))}
p.add_layout(LinearAxis(y_range_name=y_column2_range, axis_label="Amostra por Variante"), "right")
sample_bar = p.vbar(mde_df['Semana do experimento'], 
                    top=mde_df['Amostra por variante'], 
                    legend_label="Amostra por variante",
                    width=0.8,
                    alpha=0.4,
                    color='silver',
                    y_range_name=y_column2_range)

#Fist axis (MDE. Ordem invertida para ajustar elemtnos do gráfico)
mde_line = p.line(mde_df['Semana do experimento'], 
                  mde_df['MDE'], 
                  legend_label="MDE (%)", 
                  color='mediumvioletred',
                  line_width=3)

p.y_range = Range1d(mde_df['MDE'].min() * (1 - y_overlimit), mde_df['MDE'].max() * (1 + y_overlimit))

# Increase the font size of axis labels and legend labels
p.xaxis.axis_label_text_font_size = "14pt"
p.yaxis.axis_label_text_font_size = "14pt"
p.legend.label_text_font_size = "12pt"

# Add padding to the plot to make room for the legend
p.legend.location = "top_left"
p.legend.spacing = 10
p.legend.padding = 5

st.bokeh_chart(p, use_container_width=True)
