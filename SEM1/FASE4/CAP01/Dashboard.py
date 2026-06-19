import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Configuração da página
st.set_page_config(
    page_title="Dashboard Agrícola Inteligente",
    page_icon="🌱",
    layout="wide"
)

# Carregar dados
df = pd.read_csv("Base_Dados.csv")

# Carregar modelo
with open("modelo_agricola.pkl", "rb") as arquivo:
    modelo = pickle.load(arquivo)

st.title("🌱 Dashboard de Gestão Agrícola com Machine Learning")

st.markdown("""
Sistema de apoio à decisão para irrigação e manejo agrícola.
""")

# Menu lateral
st.sidebar.header("Parâmetros da Fazenda")

temperatura = st.sidebar.slider(
    "Temperatura (°C)",
    15,
    45,
    30
)

umidade = st.sidebar.slider(
    "Umidade (%)",
    20,
    100,
    60
)

chuva = st.sidebar.slider(
    "Chuva (mm)",
    0,
    50,
    5
)

fertilizante = st.sidebar.slider(
    "Fertilizante (kg/ha)",
    50,
    200,
    120
)

area = st.sidebar.slider(
    "Área Cultivada (ha)",
    10,
    300,
    100
)

# Dados para previsão
entrada = pd.DataFrame({
    "temperatura":[temperatura],
    "umidade":[umidade],
    "chuva":[chuva],
    "fertilizante":[fertilizante],
    "area":[area]
})

# Previsão
previsao = modelo.predict(entrada)[0]

# Indicadores
col1, col2, col3 = st.columns(3)

col1.metric(
    "Irrigação Prevista",
    f"{previsao:.2f} L"
)

col2.metric(
    "Temperatura",
    f"{temperatura} °C"
)

col3.metric(
    "Umidade",
    f"{umidade}%"
)

st.divider()

# Correlação
st.subheader("Mapa de Correlação")

corr = df.corr(numeric_only=True)

fig_corr = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="Viridis"
)

st.plotly_chart(
    fig_corr,
    use_container_width=True
)

# Dispersão
st.subheader("Temperatura x Irrigação")

fig = px.scatter(
    df,
    x="temperatura",
    y="irrigacao",
    size="area",
    color="umidade",
    title="Relação entre Temperatura e Irrigação"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Recomendações
st.subheader("Recomendações Inteligentes")

if previsao > 500:
    st.error(
        "Alta necessidade de irrigação. Recomenda-se aumento do fornecimento hídrico."
    )

elif previsao > 400:
    st.warning(
        "Necessidade moderada de irrigação."
    )

else:
    st.success(
        "Necessidade baixa de irrigação."
    )

if umidade < 50:
    st.warning(
        "Baixa umidade detectada. Monitorar estresse hídrico."
    )

if chuva < 3:
    st.warning(
        "Pouca chuva prevista. Considere irrigação complementar."
    )

# Dados
st.subheader("Base de Dados")

st.dataframe(
    df,
    use_container_width=True
)