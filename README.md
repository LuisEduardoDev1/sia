# 📊 Monitoramento de Notícias - IA no Piauí

Este projeto realiza o **monitoramento automático de notícias** relacionadas à **Inteligência Artificial (IA) no estado do Piauí**, coletando informações do **Google News** e apresentando análises em um **dashboard interativo** feito com [Streamlit](https://streamlit.io/).

O objetivo é **acompanhar notícias sobre IA no Piauí**, destacando **sentimentos (positivo, negativo, neutro)** e **palavras-chave mais frequentes**.

---

## 🚀 Funcionalidades

- 🔎 **Coletar notícias** no Google News sobre "IA no Piauí".  
- 🧹 **Pré-processamento de texto** (remoção de stopwords, pontuação, acentos etc.).  
- 😀 **Análise de sentimentos simples** (Positivo, Negativo, Neutro).  
- 📊 **Dashboard interativo** com:
  - Gráfico de pizza da **distribuição de sentimentos**. 
  - Gráfico de colunas com a quantidade de notícias por **sentimentos**. 
  - **Nuvem de palavras** com os termos mais frequentes.  
- ⚡ Interface leve e rápida via **Streamlit**.  

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) → Interface do dashboard  
- [Pandas](https://pandas.pydata.org/) → Manipulação dos dados  
- [Matplotlib](https://matplotlib.org/) → Gráficos  
- [WordCloud](https://amueller.github.io/word_cloud/) → Geração da nuvem de palavras  
- [NLTK](https://www.nltk.org/) → Pré-processamento e stopwords  

---

## 📦 Instalação e Execução

Segue a sequência de comandos a serem seguidos para execução do projeto:

```bash
git clone https://github.com/seu-usuario/monitoramento-ia-piaui.git
cd monitoramento-ia-piaui
pip install -r requirements.txt
py main.py
streamlit run app.py
```

## 👍 Ética e Transparência

Algumas etapas do projeto contaram com o apoio de modelos de Inteligência Artificial (IA), especificamente o ChatGPT (OpenAI), para:
- Auxílio na escrita inicial de trechos de código em Python (requisições HTTP, criação do arquivo CSV e gráficos do Streamlit).
- Apoio na redação de partes da documentação.