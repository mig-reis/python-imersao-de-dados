import aula_01_exploracao as a1
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def limpar_dados(df):   # Limpa dados faltantes e ajusta tipos
    print(df.columns)   # Verifica colunas disponíveis
    df_limpo = df.dropna()  # Remove linhas com dados faltantes

    if 'ano_trabalho' in df_limpo.columns: # Ajusta tipo de dado da coluna 'ano_trabalho'
        df_limpo['ano_trabalho'] = df_limpo['ano_trabalho'].astype('Int64')   # Usa Int64 para permitir NaN se necessário

    return df_limpo # Retorna o DataFrame limpo


def salvar_csv(df, nome_arquivo='dados-imersao.csv'):   # Salva o DataFrame limpo em um arquivo CSV
    df.to_csv(nome_arquivo, index=False)    # Salva sem o índice


def grafico_distribuicao_senioridade(df):   # Gráfico de barras da distribuição de níveis de experiência
    df['mapa_experiencia'].value_counts().plot( # Plota o gráfico de barras
        kind='bar',
        title='Distribuição dos níveis de experiência'
    )
    plt.show()  # Exibe o gráfico


def grafico_salario_medio_senioridade(df):  # Gráfico de barras do salário médio por nível de experiência
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=df,
        x='mapa_experiencia',
        y='salario_em_usd',
        estimator='mean'
    )
    plt.title('Salário médio por nível de experiência')
    plt.ylabel('Salário médio (USD)')
    plt.xlabel('Nível de experiência')
    plt.show()


def analise_estatistica_salarios(df):   # Análise estatística dos salários por nível de experiência
    print(
        df.groupby('mapa_experiencia')['salario_em_usd'] # Agrupa por nível de experiência
        .mean()
        .sort_values(ascending=False)
    )


def graficos_distribuicao_salarios(df): ## Gráficos de distribuição dos salários
    plt.figure(figsize=(8, 4))
    sns.histplot(df['salario_em_usd'], bins=50, kde=True)
    plt.title('Distribuição dos Salários')
    plt.xlabel('Salário em USD')
    plt.ylabel('Frequência')
    plt.show()

    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df['salary_in_usd'])
    plt.title('Boxplot dos salários')
    plt.xlabel('Salário em USD')
    plt.show()


def boxplot_por_senioridade(df):    # Boxplot dos salários por nível de experiência
    ordem_senioridade = ['EN', 'MI', 'SE', 'EX']  # Define a ordem dos níveis de experiência

    plt.figure(figsize=(8, 5))
    sns.boxplot(
        x='mapa_experiencia',
        y='salario_em_usd',
        data=df,
        order=ordem_senioridade
    )
    plt.title('Distribuição salarial por nível de experiência')
    plt.xlabel('Nível de experiência')
    plt.ylabel('Salário (USD)')
    plt.show()


def analise_data_scientist(df): ## Análise específica para Data Scientists
    df_ds = df[df['cargo'] == 'Data Scientist']     # Filtra apenas Data Scientists

    media_ds = (    # Calcula a média dos salários por país
        df_ds.groupby('residencia_funcionario')['salario_em_usd']
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    plt.figure(figsize=(10, 5))
    sns.barplot(
        x='residencia_funcionario',
        y='salario_em_usd',
        data=media_ds.head(5)
    )
    plt.title('Top 5 países com maiores salários para Data Scientists')
    plt.xlabel('País')
    plt.ylabel('Salário Médio (USD)')
    plt.show()


def grafico_interativo_senioridade(df): ## Gráfico interativo de salário médio por nível de experiência
    media_senioridade = (
        df.groupby('mapa_experiencia')['salario_em_usd']
        .mean()
        .reset_index()
    )

    fig = px.bar(
        media_senioridade,  # Cria gráfico de barras interativo
        x='mapa_experiencia',
        y='salario_em_usd',
        color='mapa_experiencia',
        title='Salário Médio por Nível de Experiência'
    )

    fig.update_layout(
        xaxis={'categoryorder': 'total descending'}
    )

    fig.show()


def main(): #  # Função principal para executar o fluxo de trabalho
    df = a1.carregar_dados()    # Carrega os dados
    df = a1.traduzir_colunas(df)    # Renomeia as colunas
    df = a1.traduzir_experiencia(df)    # Traduz os níveis de experiência
    df_limpo = limpar_dados(df) # Limpa os dados

    salvar_csv(df_limpo)

    grafico_distribuicao_senioridade(df_limpo)
    grafico_salario_medio_senioridade(df_limpo)
    analise_estatistica_salarios(df_limpo)
    graficos_distribuicao_salarios(df_limpo)
    boxplot_por_senioridade(df_limpo)
    analise_data_scientist(df_limpo)
    grafico_interativo_senioridade(df_limpo)


if __name__ == "__main__":  # Executa a função principal
    main()
