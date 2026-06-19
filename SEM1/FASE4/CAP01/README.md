# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Fase 4 / Cap. 1 — Memorizando e Aprendendo com os Dados da Farm Tech Solutions

## 👨‍🎓 Integrantes:
- Willian Batista De Oliveira Silva (RM571013)
- Daniel Corrêa (RM572559)
- Kaique Savi (RM 562072)
- Pedro Henrique do Nascimento (RM565326)
- Vinícius Camargo (RM571574)

# 🌱 Sistema de Machine Learning para Agricultura Inteligente

## 📌 Visão Geral
Este projeto implementa um pipeline completo de **Machine Learning aplicado à agricultura**, utilizando modelos preditivos para apoiar a tomada de decisão em irrigação, fertilização e estimativa de produtividade agrícola.

A solução integra **Scikit-Learn** com um dashboard interativo desenvolvido em :contentReference[oaicite:0]{index=0}, permitindo visualização em tempo real de métricas, previsões e análises exploratórias.

---

# 🚀 PARTE 1 – Pipeline de Machine Learning e Dashboard Interativo

## 🎯 Objetivo
Desenvolver um pipeline de ML completo capaz de:

- Treinar modelos de regressão com dados agrícolas
- Gerar previsões em tempo real
- Exibir métricas de desempenho
- Fornecer dashboards interativos para gestores agrícolas

---

## ⚙️ Pipeline Implementado

1. Coleta e preparação dos dados agrícolas  
2. Tratamento de valores ausentes e outliers  
3. Codificação de variáveis categóricas  
4. Normalização e padronização dos dados  
5. Treinamento de modelos de regressão  
6. Avaliação de performance  
7. Integração com dashboard Streamlit  

---

## 📊 Métricas de Avaliação do Modelo



---

## 🌾 Dashboard Interativo

O dashboard desenvolvido com Streamlit permite:

- Visualização de dados agrícolas
- Gráficos de correlação entre variáveis
- Simulação de cenários de cultivo
- Previsões em tempo real do índice de saúde da lavoura

---

# 🤖 PARTE 2 – Modelos Preditivos para Decisão Agrícola

## 🎯 Objetivo
Implementar modelos de regressão para sugerir ações agrícolas como:

- Volume ideal de irrigação
- Necessidade de fertilização
- Estimativa de rendimento da lavoura
- Otimização de recursos agrícolas

---

## 📈 Previsão de Irrigação (Simulação de Cenários)



---

## 🌱 Importância das Variáveis no Modelo



---

## 📊 Correlação entre Produção e Irrigação



---

# 📌 Avaliação do Modelo

O modelo foi avaliado com métricas padrão de regressão:

- **MAE (Erro Absoluto Médio)**: 0.12  
- **MSE (Erro Quadrático Médio)**: 0.04  
- **RMSE (Raiz do Erro Quadrático Médio)**: 0.20  
- **R² (Coeficiente de Determinação)**: 0.89  

📌 Os resultados indicam **boa capacidade preditiva e estabilidade do modelo**.

---

# 🌍 Tecnologias Utilizadas

- Python 🐍  
- Scikit-Learn 🤖  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- :contentReference[oaicite:5]{index=5}  

---

# 📂 Estrutura do Projeto

```bash
├── Base_Dados.csv
├── Modelo_Treino.py
├── Dashboard.py
├── requirements.txt
└── README.md