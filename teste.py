import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Empresas Parceiras",
    page_icon="🏢",
    layout="wide"
)

# Fundo preto + texto branco
st.markdown("""
<style>
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

/* Textos */
h1, h2, h3, p, div {
    color: white;
}
</style>
""", unsafe_allow_html=True)


# Título da página
st.title("Empresas Parceiras")


# Criação das três colunas
col1, col2, col3 = st.columns(3)


# HYBE
with col1:
    st.image("Hybe.jpg", use_container_width=True)
    st.subheader("HYBE")

    st.link_button(
        "Acessar",
        "https://hybecorp.com/ko/main"
    )

    st.write(
        "A HYBE é uma empresa sul-coreana de entretenimento, "
        "conhecida por gerenciar artistas como o BTS e investir "
        "em música, tecnologia e plataformas digitais."
    )


# JYP Entertainment
with col2:
    st.image(
        "JYP_Entertainment_logo_2021.webp",
        use_container_width=True
    )

    st.subheader("JYP Entertainment")

    st.link_button(
        "Acessar",
        "https://www.jype.com/"
    )

    st.write(
        "Empresa sul-coreana de entretenimento responsável "
        "por artistas como TWICE, Stray Kids e ITZY."
    )


# YG Entertainment
with col3:
    st.image(
        "YG Entertainment.jpg",
        use_container_width=True
    )

    st.subheader("YG Entertainment")

    st.link_button(
        "Acessar",
        "https://ygfamily.com/en/main"
    )

    st.write(
        "Empresa sul-coreana de entretenimento conhecida "
        "por artistas como BLACKPINK, TREASURE e BABYMONSTER."
    )
