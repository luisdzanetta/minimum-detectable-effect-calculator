import math
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Define the MDE function
def calculate_mde(p, n):
    return math.sqrt((1/p - 1)/(n/16))

# Define the inputs using Streamlit widgets
num_weeks = st.number_input("Enter the number of weeks:", value=4, step=1, min_value=1, max_value=52)
sample_per_variant = st.number_input("Enter the sample per variant:", value=1000, step=100, min_value=100, max_value=100000)
base_conversion = st.number_input("Enter the base conversion of the control variant:", value=0.05, step=0.01, min_value=0.01, max_value=1.0)

# Calculate the MDE for each week and store the data in a list of dictionaries
mde_data = []
for week in range(1, num_weeks+1):
    total_sample = sample_per_variant * week
    mde = calculate_mde(base_conversion, total_sample)
    mde_data.append({'Experiment week number': week, 'Total sample per variant': total_sample, 'Sample per variant': sample_per_variant, 'MDE': mde*100})

# Convert the list of dictionaries to a Pandas dataframe
mde_df = pd.DataFrame(mde_data)

# Display the table
st.write(mde_df)

# Plot the graph
fig, ax = plt.subplots()
ax.plot(mde_df['Experiment week number'], mde_df['MDE'])
ax.set(xlabel='Experiment week number', ylabel='MDE', title='MDE over time')
st.pyplot(fig)
