import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime
from PIL import Image


st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)


if "data" not in st.session_state:
    df_data = pd.read_excel("Gols.xlsx")
    st.session_state["data"] = df_data
if "data2" not in st.session_state:
    df_data2 = pd.read_excel("Jogos.xlsx")
    st.session_state["data2"] = df_data2
if "data3" not in st.session_state:
    df_data3 = pd.read_excel("Títulos.xlsx")
    st.session_state["data3"] = df_data3

image = Image.open("ucl.png")

st.write("# ESTATÍSTICAS UEFA CHAMPIONS LEAGUE")
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)
col1.image(image, width = 64)
col2.image(image, width = 64)
col3.image(image, width = 64)
col4.image(image, width = 64)
col5.image(image, width = 64)
col6.image(image, width = 64)
col7.image(image, width = 64)
col8.image(image, width = 64)
col9.image(image, width = 64)
col10.image(image, width = 64)
st.sidebar.header("__`DASHBOARD UCL`__")
st.sidebar.markdown("Desenvolvido por [Nathan W. T. Barbosa](https://www.linkedin.com/in/nathanwesley/)")


st.markdown(
    """
    Dashboards que apresentam os dados de jogadores com mais jogos, gols e títulos da Uefa Champions League.
    Feito a partir do scraping da página do Wikipédia por meio da linguagem de programação Python e utilizando a biblioteca Streamlit para a criação dos dashboards.
    
    * Dados atualizados até fevereiro/23
"""
)
