![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/status-done-yellow)

# 📊 Análise de Salários em Data Jobs  
Projeto desenvolvido durante a **Imersão de Dados da Alura**, utilizando **Python e Pandas**, com foco em análise exploratória de dados salariais na área de tecnologia.

> Diferente do Google Colab, este projeto foi estruturado para rodar localmente no **VS Code**, com código organizado em funções e pronto para versionamento no GitHub.

---

## 📁 Base de Dados

Os dados são carregados diretamente do repositório oficial da Alura:

🔗 https://github.com/guilhermeonrails/data-jobs

A base contém informações como:
- Ano de trabalho  
- Nível de experiência  
- Tipo de emprego  
- Cargo  
- Salário  
- Regime remoto  
- Localização da empresa  
- Porte da empresa  

---

## 🔄 Traduções Aplicadas

Para facilitar a leitura e análise, o projeto realiza:

### ✔ Tradução das colunas
Exemplo:
- `experience_level` → `mapa_experiencia`
- `job_title` → `cargo`
- `salary_in_usd` → `salario_em_usd`

### ✔ Tradução dos níveis de experiência
- `EN` → **junior**
- `MI` → **pleno**
- `SE` → **senior**
- `EX` → **executivo**

---

## 📊 Funcionalidades Atuais (Aula 01)

- Carregamento da base de dados
- Tradução de colunas
- Análise exploratória:
  - `head()`
  - `info()`
  - `describe()`
- Contagem de categorias:
  - Nível de experiência
  - Tipo de emprego
  - Regime remoto
  - Porte da empresa

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Pandas
- VS Code
- Git & GitHub

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git

2. Instale as dependências:
pip install -r requirements.txt

3. Execute o script:
python aula_01_exploracao.py


🚀 Próximos Passos

Aula 02: análise de salários
Gráficos com Matplotlib / Seaborn
Limpeza de dados
Insights para portfólio