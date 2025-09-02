import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

def main():
    st.set_page_config(page_title="Monitoramento IA no Piauí", layout="wide")

    st.title("📊 Dashboard de Notícias - IA no Piauí")
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
    termo_filtro = st.multiselect("Selecione os termos de busca:", termo_busca, default=termo_busca)
    df_processado = df_processado[df_processado["termo"].isin(termo_filtro)]


    st.subheader("📌 Distribuição de Sentimentos")
    
    col1, col2 = st.columns(2)

    # Gráfico pizza com percentual de quantidade de notícias por sentimento
    with col1:
        counts = df_processado["sentimento"].value_counts()

        fig1, ax1 = plt.subplots(figsize=(3, 3), dpi=11)

        def func(pct):
            return f"({pct:.1f}%)"
        
        cores = ["#4CAF50", "#F44336", "#FFC107"][:len(counts)]

        ax1.pie(
            counts,
            labels=counts.index,
            autopct=lambda pct: func(pct),
            textprops={'fontsize': 6},
            colors=cores
        )
        ax1.axis("equal")
        st.pyplot(fig1, use_container_width=False)


    # Gráfico de colunas
    with col2:
        fig, ax = plt.subplots(figsize=(3, 2), dpi=11)
        ax.bar(
            counts.index,
            counts.values, 
            color=["#4CAF50", "#F44336", "#FFC107"]
            )
        ax.set_xlabel("Sentimentos")
        ax.set_ylabel("Quantidade")
        ax.set_title("Distribuição de Sentimentos")

        st.pyplot(fig, use_container_width=False)


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
    ⚠️ *Aviso: Esta análise de sentimento é baseada em regras simples de comparação de strings e pode não capturar sarcasmo ou contextos complexos.*  
    """)

if __name__ == "__main__":
    main()
