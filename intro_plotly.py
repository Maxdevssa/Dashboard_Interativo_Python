import plotly.express as px
import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv(r'C:\Users\bruno\PycharmProjects\pythonProject1\clientes-v3-preparado.csv')

# Gráfico de dispersão
fig = px.scatter(df, x='idade', y='salario', color='nivel_educacao', hover_data=['estado_civil'])

# Atualização do layout
fig.update_layout(title='Idade vs Salário por Nível de Educação', xaxis_title='Idade', yaxis_title='Salário')

# Exibição do gráfico
fig.show()
