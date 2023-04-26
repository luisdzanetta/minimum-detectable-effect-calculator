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
p = figure(title="MDE por semana", 
           x_axis_label="Semana", 
           y_axis_label="MDE")

#First axis
p.line(mde_df['Semana do experimento'], 
        mde_df['MDE'], 
        legend_label="MDE (%)", 
        color='blue',
        line_width=2)

p.y_range = Range1d(mde_df['MDE'].min() * (1 - y_overlimit), mde_df['MDE'].max() * (1 + y_overlimit))

#Second axis
y_column2_range = 'Semana do experimento' + "_range"
p.extra_y_ranges = {y_column2_range: Range1d(start=mde_df['Amostra por semana'].min() * (1 - y_overlimit),end=mde_df['Amostra por semana'].max() * (1 + y_overlimit))}
p.add_layout(LinearAxis(y_range_name=y_column2_range), "right")
p.vbar(mde_df['Semana do experimento'], 
        mde_df['Amostra por semana'], 
        legend_label="Amostra por variante", 
        color='blue',
        line_width=2)

st.bokeh_chart(p, use_container_width=True)
