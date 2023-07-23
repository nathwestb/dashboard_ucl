import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Artilheiros",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"]


jogadores = df_data["Jogador"].value_counts().index.sort_values()
jogador = st.sidebar.selectbox("Jogador", jogadores)


player_stats = df_data[df_data["Jogador"] == jogador].iloc[0]

col1, col2 = st.columns(2)
col1.image(player_stats["Imagem"])
col1.subheader(f"{player_stats['Jogador']}")
col1.subheader(f"{player_stats['Gols']}⚽")
col1.caption(f"{player_stats['Clube(s)']}")
col1.caption(f"{player_stats['País']}")

columns = ["Jogador", "Imagem", "Gols"]

col2.dataframe(
    df_data[columns],
    column_config={
        "Imagem": st.column_config.ImageColumn(),
        "Gols": st.column_config.ProgressColumn(format="%f", min_value=0, max_value=140)},
    hide_index=True,
)


st.divider()


cols = ["Jogador", "Gols"]

source = df_data[cols]

chart = alt.Chart(source).mark_circle().encode(
    x=alt.X('Gols', scale=alt.Scale(domain=(40, 145)), axis=alt.Axis(title='Gols', grid=False)),  # Adicionar o eixo x e título
    y='Jogador',
    color=alt.condition(
        alt.datum.Jogador == jogador,
        alt.value('#FF00FF'),   # Jogador selecionado
        alt.value('lightgray')    # Outros jogadores
    ),
    size=alt.condition(
        alt.datum.Jogador == jogador,
        alt.value(150),   # Tamanho dos pontos para o jogador selecionado
        alt.value(50)      # Tamanho dos pontos para outros jogadores
    )
).interactive()

# Adicionar os números no eixo x
x_axis_labels = alt.Chart(source).mark_text(align='left', baseline='middle', dx=3).encode(
    x=alt.X('Gols:Q', scale=alt.Scale(domain=(45, 145))),
    y=alt.value(500),  # Posição dos números no eixo x
    text='Gols:Q'
)

# Exibir o gráfico de dispersão com os números no eixo x
#st.altair_chart(chart + x_axis_labels, use_container_width=True)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart + x_axis_labels, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart + x_axis_labels, theme=None, use_container_width=True)