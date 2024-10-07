from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Lê os dados do CSV
df = pd.read_csv(r'C:\Users\bruno\PycharmProjects\pythonProject1\clientes-v3-preparado.csv')
lista_nivel_educacao = df['nivel_educacao'].unique()

# Cria opções para o dropdown de seleção de nível de educação
options = [{'label': nivel, 'value': nivel} for nivel in lista_nivel_educacao]


# Função para criar gráficos
def cria_graficos(selecao_nivel_educacao):
    # Verifica se a seleção não está vazia
    if not selecao_nivel_educacao:
        selecao_nivel_educacao = lista_nivel_educacao  # Seleciona todos os níveis de educação se nenhum estiver selecionado

    # Filtra o DataFrame com base na seleção
    filtro_df = df[df['nivel_educacao'].isin(selecao_nivel_educacao)]

    # Gráfico de Barras
    fig1 = px.bar(filtro_df, x='estado_civil', y='salario', color="nivel_educacao", barmode="group", opacity=1,
                  color_discrete_sequence=px.colors.qualitative.Set1)
    fig1.update_layout(
        title="Salário por Estado Civil e Nível de Educação",
        xaxis_title="Estado Civil",
        yaxis_title="Salário",
        legend_title="Nível de Educação",
        plot_bgcolor="rgba(222, 225, 223, 1)",  # Fundo Interno
        paper_bgcolor="rgba(240, 240, 240, 1)"  # Fundo Externo
    )

    # Gráfico 3D
    fig2 = px.scatter_3d(filtro_df, x='idade', y='salario', z='anos_experiencia', color='nivel_educacao')
    fig2.update_layout(
        title="Distribuição de Idade, Salário e Experiência por Nível de Educação",
        scene=dict(
            xaxis_title="Idade",
            yaxis_title="Salário",
            zaxis_title="Anos de Experiência"
        ),
        plot_bgcolor="rgba(225, 225, 225, 1)",  # Fundo Interno
        paper_bgcolor="rgba(240, 240, 240, 1)"  # Fundo Externo
    )

    return fig1, fig2


# Função para criar a aplicação Dash
def cria_app():
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1('Dashboard Interativo'),
        html.Div('''Interatividade entre os dados.'''),
        html.Br(),
        html.H2("Gráfico de Salário por Estado Civil"),
        dcc.Checklist(
            id='id_selecao_nivel_educacao',
            options=options,
            value=[lista_nivel_educacao[0]],  # Define valor padrão
        ),
        dcc.Graph(id='id_grafico_barra'),
        dcc.Graph(id='id_grafico_3d')
    ])

    return app


# Execução da aplicação
if __name__ == '__main__':
    app = cria_app()


    # Callback para atualizar os gráficos
    @app.callback(
        [
            Output(component_id='id_grafico_barra', component_property='figure'),
            Output(component_id='id_grafico_3d', component_property='figure')
        ],
        [Input(component_id='id_selecao_nivel_educacao', component_property='value')]
    )
    def atualiza_graficos(selecao_nivel_educacao):
        fig1, fig2 = cria_graficos(selecao_nivel_educacao)
        return fig1, fig2


    # Executa a aplicação
    app.run_server(debug=True, port=8085)
