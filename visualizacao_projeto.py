import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import plotly.express as px

# Leitura do dataset
df = pd.read_csv(r'C:\Users\bruno\PycharmProjects\pythonProject1\clientes-v3-preparado.csv')
print(df.columns)

# Mapa de calor interativo de correlações (Pearson)
df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos',
              'nivel_educacao_cod', 'area_atuacao_cod', 'estado_cod']].corr()

fig = px.imshow(df_corr, text_auto=True, aspect="auto",
                color_continuous_scale='Viridis', title="Mapa de Calor de Correlação")
fig.show()

# Área Plot do salário ao longo da idade
fig = px.area(df, x='idade', y='salario', line_group='estado_civil',
              color='estado_civil', title='Evolução do Salário por Idade e Estado Civil')
fig.show()

# Divisão dos dados para treino de modelos (exemplo com colunas de features e target)
X = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos']]  # Colunas de exemplo para features
y = df['estado_civil']  # Coluna alvo de exemplo

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinando o modelo de Regressão Logística
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
y_pred_lr = log_reg.predict(X_test)

# Treinando o modelo de Árvore de Decisão
tree_clf = DecisionTreeClassifier()
tree_clf.fit(X_train, y_train)
y_pred_dt = tree_clf.predict(X_test)

# Matriz de confusão para Regressão Logística
cm_lr = confusion_matrix(y_test, y_pred_lr)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_lr, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title("Matriz de Confusão: Regressão Logística")
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.show()

# Matriz de confusão para Árvore de Decisão
cm_dt = confusion_matrix(y_test, y_pred_dt)
plt.figure(figsize=(8, 6))
sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title("Matriz de Confusão: Árvore de Decisão")
plt.xlabel('Previsto')
plt.ylabel('Real')
plt.show()

# Gráfico de Regressão Linear (valores reais vs. predições)
# Supondo que y_pred seja a predição de um modelo de regressão
y_pred = log_reg.predict(X_test)  # Exemplo usando a regressão logística para predição

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
plt.title("Valores Reais vs. Predições: Regressão Linear")
plt.xlabel('Real')
plt.ylabel('Previsto')
plt.show()

# Heatmap de correlações de Spearman
spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos']].corr(method='spearman')

plt.figure(figsize=(10, 8))
sns.heatmap(spearman_corr, annot=True, cmap='viridis', fmt='.2f')
plt.title('Correlação de Spearman entre variáveis')
plt.show()

# Visualização interativa usando Plotly para correlação de Pearson
pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos']].corr(method='pearson')

fig = px.imshow(pearson_corr, text_auto=True, aspect='auto', color_continuous_scale='RdBu', title='Correlação de Pearson Interativa')
fig.show()

# Visualização interativa usando Plotly para correlação de Spearman
fig = px.imshow(spearman_corr, text_auto=True, aspect='auto', color_continuous_scale='RdBu', title='Correlação de Spearman Interativa')
fig.show()
