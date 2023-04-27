import streamlit as st

st.title("Cálculo do MDE")

st.write("O **MDE**, é o tamanho mínimo da diferença entre as taxas de conversão das variantes e do grupo de controle que pode ser detectado com um nível de significância alpha e um poder de teste beta. Em outras palavras, se a diferença entre as taxas de conversão das variantes e do grupo de controle for menor que o MDE, não será possível detectar essa diferença com um nível de significância alpha e um poder de teste beta especificados.")

st.write("**Equação para cálculo do MDE**")
st.write("A equação do Mínimo Tamanho Detectável do Efeito (MDE) é:")
st.latex(r'''\text{MDE} = \sqrt{\frac{1}{p-1} \div \frac{n}{16}}''')

st.write("**A equação apresentada anteriormente é um derivação da seguinte equação:**")
st.latex(r'''n = \frac{16 \σ^2}{\Δ}''')
        
