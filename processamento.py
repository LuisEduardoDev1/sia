import re
import pandas as pd
from dados import coletar_noticias
from processamento import processar_noticias

# Lista bem simples de palavras positivas e negativas
positivas = ["avanço", "progresso", "sucesso", "oportunidade", "benefício", "melhoria", "crescimento"]
negativas = ["problema", "crise", "risco", "ameaça", "falha", "dificuldade", "desafio"]

if __name__ == "__main__":
    # 1. Coletar notícias
    df = coletar_noticias("Inteligência Artificial Piauí")

    # 2. Processar
    df_processado = processar_noticias(df)

    # 3. Mostrar resultado no terminal
    print(df_processado[["titulo", "sentimento"]])

def limpar_texto(texto: str) -> str:
    """
    Limpa o texto removendo tags HTML, caracteres especiais e deixando em minúsculo.
    """
    if not isinstance(texto, str):
        return ""
    texto = re.sub(r"<.*?>", "", texto)                   # remove tags HTML
    texto = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", texto)          # remove caracteres especiais
    return texto.lower()

def analisar_sentimento(texto: str) -> str:
    """
    Retorna o sentimento do texto com base em regras simples.
    """
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
    """
    Recebe um DataFrame com colunas ['titulo', 'descricao'] e retorna com
    texto limpo + coluna de sentimento.
    """
    df["texto_limpo"] = (df["titulo"].fillna("") + " " + df["descricao"].fillna("")).apply(limpar_texto)
    df["sentimento"] = df["texto_limpo"].apply(analisar_sentimento)
    return df

# Teste rápido do módulo
if __name__ == "__main__":
    dados_teste = pd.DataFrame([
        {"titulo": "Avanço da Inteligência Artificial no Piauí", "descricao": "Um grande progresso para o estado"},
        {"titulo": "Crise na implementação de sistemas de IA", "descricao": "Problemas dificultam o uso"},
        {"titulo": "Evento sobre IA em Teresina", "descricao": "Discussões sobre aplicações"}
    ])
    
    resultado = processar_noticias(dados_teste)
    print(resultado[["titulo", "sentimento"]])