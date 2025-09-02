import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

from dados import coletar_noticias
from processamento import processar_noticias

def main():
    st.set_page_config(page_title="Monitoramento IA no Piauí", layout="wide")

    st.title("📊 Monitoramento de Notícias - IA no Piauí")
    st.markdown("Este painel mostra notícias coletadas do Google News com análise de sentimento simples.")

    # Quais notícias coletar
    termos_busca = ["Inteligência Artificial Piauí", "SIA Piauí"]
    todas_noticias = pd.DataFrame()

    for termo in termos_busca:
        df = coletar_noticias(termo, max_noticias=10)
        todas_noticias = pd.concat([todas_noticias, df], ignore_index=True)

    if todas_noticias.empty:
        st.error("Nenhuma notícia encontrada. Tente novamente mais tarde.")
        return

    df_processado = processar_noticias(todas_noticias)

    # Gráfico pizza para quantidade de notícias por sentimento
    st.subheader("📌 Distribuição de Sentimentos")
    counts = df_processado["sentimento"].value_counts()

    fig1, ax1 = plt.subplots(figsize=(3, 3), dpi = 11)
    ax1.pie(counts, labels=counts.index, autopct="%1.1f%%")
    ax1.axis("equal")
    st.pyplot(fig1, use_container_width=False)

    # Nuvem de palavras
    st.subheader("☁️ Nuvem de Palavras")
    texto_unico = " ".join(df_processado["texto_limpo"])
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
