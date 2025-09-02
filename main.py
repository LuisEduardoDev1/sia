from dados import coletar_noticias
from processamento import processar_noticias
import pandas as pd

def main():
    termos_busca = ["Inteligência Artificial Piauí", "SIA Piauí"]

    todas_noticias = pd.DataFrame()
    for termo in termos_busca:
        df = coletar_noticias(termo, max_noticias=10)
        print(f"[{termo}] Notícias coletadas: {len(df)}")
        todas_noticias = pd.concat([todas_noticias, df], ignore_index=True)

    df_processado = processar_noticias(todas_noticias)

    print("\n=== Notícias Coletadas e Classificadas ===\n")
    print(df_processado[["titulo", "sentimento"]].head(20))

    # Salvar Dataframe em CSV
    df_processado.to_csv("noticias_processadas.csv", index=False, encoding="utf-8-sig")
    print("\n✅ Arquivo 'noticias_processadas.csv' salvo com sucesso!")

if __name__ == "__main__":
    main()