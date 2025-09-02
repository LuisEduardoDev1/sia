import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

def main():
    st.set_page_config(page_title="Monitoramento IA no Piauí", layout="wide")

    st.title("📊 Monitoramento de Notícias - IA no Piauí")
    st.markdown("Este painel mostra notícias coletadas do Google News com análise de sentimento simples.")

    # Carregar dados do CSV 
    try:
        df_processado = pd.read_csv("noticias_processadas.csv", encoding="utf-8-sig")
    except FileNotFoundError:
        st.error("❌ Arquivo 'noticias_processadas.csv' não encontrado. Execute o `main.py` primeiro para gerar os dados.")
        return

    if df_processado.empty: 
        st.error("Nenhuma notícia encontrada no arquivo CSV.")
        return

    # Filtro de termo
    termo_busca = ["Inteligência Artificial Piauí", "SIA Piauí"]
    termo_filtro = st.multiselect("Selecione os termos de busca:", termo_busca)
    df_processado = df_processado[df_processado["termo"].isin(termo_filtro)]


    # Gráfico pizza com percentual de quantidade de notícias por sentimento
    st.subheader("📌 Distribuição de Sentimentos")
    counts = df_processado["sentimento"].value_counts()

    fig1, ax1 = plt.subplots(figsize=(3, 3), dpi=11)
    ax1.pie(counts, labels=counts.index, autopct="%1.1f%%")
    ax1.axis("equal")
    st.pyplot(fig1, use_container_width=False)

    # Nuvem de palavras
    st.subheader("☁️ Nuvem de Palavras")
    texto_unico = " ".join(df_processado["texto_limpo"].astype(str))
    if texto_unico.strip():
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(texto_unico)
        fig2, ax2 = plt.subplots(figsize=(6, 3))
        ax2.imshow(wordcloud, interpolation="bilinear")
        ax2.axis("off")
        st.pyplot(fig2, use_container_width=False)
    else:
        st.warning("Não foi possível gerar a nuvem de palavras (texto vazio).")

    # Tabela
    st.subheader("📄 Tabela de Notícias")
    st.dataframe(df_processado[["titulo", "link", "sentimento"]])

    # Rodapé
    st.markdown("""
    ---
    ⚠️ *Aviso: Esta análise de sentimento é baseada em regras simples e pode não capturar sarcasmo ou contextos complexos.*  
    👨‍💻 Algumas partes do código foram desenvolvidas com auxílio de modelos de IA.
    """)

if __name__ == "__main__":
    main()
