import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

# Leitura do dataset
df = pd.read_csv(r'C:\Users\bruno\PycharmProjects\visualização_dados_avançada\ecommerce_estatistica.csv')

# Função para limpar e converter valores numéricos
def clean_numeric_columns(df, column):
    # Converte a coluna para string, trata valores nulos, remove símbolos e converte para float
    df[column] = df[column].astype(str).replace({r'[^\d.,-]': ''}, regex=True)  # Remove qualquer caractere não numérico
    df[column] = df[column].str.replace(',', '.').astype(float)  # Troca vírgula por ponto e converte para float

# Limpeza das colunas que precisam ser numéricas
clean_numeric_columns(df, 'Nota')
clean_numeric_columns(df, 'N_Avaliações')
clean_numeric_columns(df, 'Desconto')
clean_numeric_columns(df, 'Qtd_Vendidos')
clean_numeric_columns(df, 'Preço')

# Inicializando a aplicação Dash
app = Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Dashboard de Ecommerce"),
    dcc.Tabs(id='tabs', value='tab-1', children=[
        dcc.Tab(label='Correlação', value='tab-1'),
        dcc.Tab(label='Gráfico de Preço', value='tab-2'),
    ]),
    html.Div(id='tabs-content')  # Esse div será preenchido pelo callback
])

# Callback para renderizar o conteúdo das abas
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        try:
            # Mapa de calor interativo de correlações (Pearson)
            df_corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos', 'Preço']].corr()

            fig = px.imshow(df_corr, text_auto=True, aspect="auto",
                            color_continuous_scale='Viridis', title="Mapa de Calor de Correlação")

            return html.Div([
                dcc.Graph(figure=fig)
            ])
        except Exception as e:
            return html.Div([
                html.H3(f"Ocorreu um erro ao gerar o gráfico de correlação: {str(e)}")
            ])

    elif tab == 'tab-2':
        try:
            # Área Plot do preço ao longo das vendas
            fig = px.area(df, x='Qtd_Vendidos', y='Preço', line_group='Marca',
                          color='Marca', title='Preço ao longo das Vendas por Marca')

            return html.Div([
                dcc.Graph(figure=fig)
            ])
        except Exception as e:
            return html.Div([
                html.H3(f"Ocorreu um erro ao gerar o gráfico de preço: {str(e)}")
            ])

    else:
        return html.Div([
            html.H3("Nenhum gráfico disponível.")
        ])

# Executando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
