# Análise de salários em Data Jobs - Base usada na Imersão de Dados - Alura

import pandas as pd


def carregar_dados():   # Carrega o arquivo CSV, pela variavel DF
    df = pd.read_csv("dados-imersao.csv")
    return df

def traduzir_colunas(df):   # Renomeia as colunas para português
    columns_translation = {
        'work_year': 'ano_trabalho',
        'experience_level': 'mapa_experiencia',
        'employment_type': 'tipo_emprego',
        'job_title': 'cargo',
        'salary': 'salario',
        'salary_currency': 'moeda_salario',
        'salary_in_usd': 'salario_em_usd',
        'employee_residence': 'residencia_funcionario',
        'remote_ratio': 'taxa_remoto',
        'company_location': 'localizacao_empresa',
        'company_size': 'porte_empresa'
    }

    return df.rename(columns=columns_translation)

    
def traduzir_experiencia(df):    # Traduz siglas de nivel_experiencia
    mapa_experiencia = {
        'EN': 'junior',
        'MI': 'pleno',
        'SE': 'senior',
        'EX': 'executivo'
    }

    return df


def explorar_dados(df):    # Exibe informações iniciais do dataframe
    print("\n📌 Primeiras linhas:")
    print(df.head())

    print("\n📌 Informações gerais:")
    df.info()   

    print("\n📌 Estatísticas descritivas:")
    print(df.describe())

    linhas, colunas = df.shape
    print(f"\n📌 Total de linhas: {linhas}")
    print(f"📌 Total de colunas: {colunas}")


def analisar_categorias(df):    # Análises simples de colunas categóricas
    print("\n📊 Mapa experiencia:")
    print(df['mapa_experiencia'].value_counts())

    print("\n📊 Tipo de emprego:")
    print(df['tipo_emprego'].value_counts())

    print("\n📊 Regime de trabalho:")
    print(df['taxa_remoto'].value_counts())
    print("")

    print("\n📊 Porte da empresa:")
    print(df['porte_empresa'].value_counts())


def main():
    df = carregar_dados()   # Carrega os dados
    df = traduzir_colunas(df)   # Traduz colunas
    df = traduzir_experiencia(df)    # Traduz valores categóricos   


if __name__ == "__main__":
    df = carregar_dados()
    explorar_dados(df)      # Agora sim analisa
    analisar_categorias(df)