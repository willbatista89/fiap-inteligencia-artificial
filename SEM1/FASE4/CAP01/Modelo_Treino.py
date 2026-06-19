import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Carregar dados
df = pd.read_csv("Base_Dados.csv")

# Variáveis independentes
X = df[[
    "temperatura",
    "umidade",
    "chuva",
    "fertilizante",
    "area"
]]

# Variável alvo
y = df["irrigacao"]

# Divisão treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Modelo
modelo = LinearRegression()

# Treinamento
modelo.fit(X_train, y_train)

# Previsões
y_pred = modelo.predict(X_test)

# Métricas
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nRESULTADOS")
print(f"MAE : {mae:.2f}")
print(f"MSE : {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²  : {r2:.4f}")

# Salvar modelo
with open("modelo_agricola.pkl", "wb") as arquivo:
    pickle.dump(modelo, arquivo)

print("\nModelo salvo com sucesso!")