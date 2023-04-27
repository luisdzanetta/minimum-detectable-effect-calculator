import streamlit as st

st.title("Cálculo do MDE")

st.write("O **MDE**, é o tamanho mínimo da diferença entre as taxas de conversão das variantes e do grupo de controle que pode ser detectado com um nível de significância alpha e um poder de teste beta. Em outras palavras, se a diferença entre as taxas de conversão das variantes e do grupo de controle for menor que o MDE, não será possível detectar essa diferença com um nível de significância alpha e um poder de teste beta especificados.")

st.write("**Equação para cálculo do MDE**")
st.write("A equação do Mínimo Tamanho Detectável do Efeito (MDE) é:")
st.latex(r'''\text{MDE} = \sqrt{\frac{1}{p-1} \div \frac{n}{16}}''')
st.write("**Onde:**")
st.write("**p:** É a conversão base do controle")
st.write("**n:** É a amostra por variante, considerando distribuição proporcional")

st.write("**A equação apresentada anteriormente é um derivação da seguinte equação:**")
st.latex(r'''n = \frac{16 \sigma^2}{\Delta}''')
st.write("**Onde:**")
st.write("**σ:** É a variância, adaptada para distribuição de Bernoulli")
st.write("**Δ:** É a amostra por variante, considerando distribuição proporcional")

st.divider()

st.write("**Referência:**")
def show_pdf("https://github.com/luisdzanetta/repo2/blob/main/Kohav%20et%20al(2009)_Controlled%20experiments%20on%20the%20web.pdf"):
    with open("https://github.com/luisdzanetta/repo2/blob/main/Kohav%20et%20al(2009)_Controlled%20experiments%20on%20the%20web.pdf","rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

show_pdf('post1-compressed.pdf')

#st.image("https://github.com/luisdzanetta/repo2/blob/main/kohav.png")
#st.download_button('Baixar o artigo', "https://link.springer.com/content/pdf/10.1007/s10618-008-0114-1.pdf?pdf=button", file_name="Kohav et al. (2009)_Controlled experiments on the web: survey and practical guide")

        
