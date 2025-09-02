import re
import pandas as pd

positivas = ["avanço", "progresso", "sucesso", "oportunidade", "benefício", "melhoria", "crescimento", "promove", "melhora"]
negativas = ["problema", "crise", "risco", "ameaça", "falha", "dificuldade", "desafio", "perigo", "danos", "perda"]

def limpar_texto(texto: str) -> str:
    if not isinstance(texto, str):
        return ""
    texto = re.sub(r"<.*?>", "", texto)
    texto = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto)
    return texto.lower()

def analisar_sentimento(texto: str) -> str:
    texto = limpar_texto(texto)
    score = 0
    for p in positivas:
        if p in texto:
            score += 1
    for n in negativas:
        if n in texto:
            score -= 1

    if score > 0:
        return "Positivo"
    elif score < 0:
        return "Negativo"
    else:
        return "Neutro"

def processar_noticias(df: pd.DataFrame) -> pd.DataFrame:
    df["texto_limpo"] = (df["titulo"].fillna("") + " " + df["descricao"].fillna("")).apply(limpar_texto)
    df["sentimento"] = df["texto_limpo"].apply(analisar_sentimento)
    return df

if __name__ == "__main__":
    # Teste rápido
    dados_teste = pd.DataFrame([
        {"titulo": "Avanço da IA no Piauí", "descricao": "Um grande progresso"},
        {"titulo": "Crise em projeto de IA", "descricao": "Problemas dificultam o uso"}
    ])
    print(processar_noticias(dados_teste)[["titulo", "sentimento"]])
