import streamlit as st

Fundo preto + texto branco

st.markdown("""

.stApp {
background-color: black;
color: white;
}
/* Botões */
.stLinkButton a {
background-color: #262730;
color: white !important;
text-decoration: none;
}

.stLinkButton a:hover {
    background-color: #ff4b4b;
    color: white !important;
}

h1, h2, h3, p, div {
    color: white;
}
</style>


""", unsafe_allow_html=True)

st.title("Empresas Parceiras")

col1, col2, col3 = st.columns(3)

with col1:
st.image("Hybe.jpg", use_container_width=True)
st.title("Hybe")
st.link_button("Acessar", "https://hybecorp.com/ko/main")
st.write("A HYBE é uma empresa sul-coreana de entretenimento, conhecida por gerenciar artistas como o BTS e investir em música, tecnologia e plataformas digitais.")

with col2:
st.image("JYP_Entertainment_logo_2021.webp", use_container_width=True)
st.title("JYP Entertainment")
st.link_button("Acessar", "https://www.jype.com/")
st.write("Empresa sul-coreana de entretenimento responsável por artistas como TWICE, Stray Kids e ITZY.")

with col3:
st.image("YG Entertainment.jpg", use_container_width=True)
st.title("YG Entertainment")
st.link_button("Acessar", "https://ygfamily.com/en/main")
st.write("Empresa sul-coreana de entretenimento conhecida por artistas como BLACKPINK, TREASURE e BABYMONSTER.")
