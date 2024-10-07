import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc

# Carregar o dataset
df = pd.read_csv(r'C:\Users\bruno\PycharmProjects\pythonProject1\clientes-v3-preparado.csv')

# Função para criar os gráficos
def cria_graficos(df):
    # --- Gráfico de Histograma ---
    fig1 = px.histogram(df, x='salario', nbins=30, title='Distribuição de Salários')

    # --- Gráfico de Pizza ---
    fig2 = px.pie(df, names='area_atuacao', color='area_atuacao', hole=0.2,
                  color_discrete_sequence=px.colors.sequential.RdBu)

    # --- Gráfico de Bolha ---
    fig3 = px.scatter(df, x='idade', y='salario', size='anos_experiencia',
                      color='area_atuacao', hover_name='estado', size_max=60)
    fig3.update_layout(title='Salário por Idade e Anos de Experiência')

    # --- Gráfico de Linha ---
    fig4 = px.line(df, x='idade', y='salario', color='area_atuacao', facet_col='nivel_educacao')
    fig4.update_layout(title='Salário por Idade e Área de Atuação para cada Nível de Educação',
                       xaxis_title='Idade', yaxis_title='Salário')

    # --- Gráfico 3D ---
    fig5 = px.scatter_3d(df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')

    # --- Gráfico de Barra ---
    fig6 = px.bar(df, x='estado_civil', y='salario', color='nivel_educacao', barmode='group',
                  color_discrete_sequence=px.colors.qualitative.Plotly, opacity=1)
    fig6.update_layout(title='Salário por Estado Civil e Nível de Educação',
                       xaxis_title='Estado Civil', yaxis_title='Salário',
                       legend_title='Nível de Educação',
                       plot_bgcolor='rgba(222, 255, 253, 1)',
                       paper_bgcolor='rgba(186, 245, 241, 1)')

    return fig1, fig2, fig3, fig4, fig5, fig6

# Função para criar a aplicação Dash
def cria_app(df):
    # Cria os gráficos
    fig1, fig2, fig3, fig4, fig5, fig6 = cria_graficos(df)

    # Configuração da aplicação Dash
    app = Dash(__name__)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6)
    ])

    # Executa a aplicação
    return app

# Executa a aplicação se o script for o principal
if __name__ == '__main__':
    app = cria_app(df)
    app.run_server(debug=True, port=8050)  # Executa na porta 8050 por padrão
