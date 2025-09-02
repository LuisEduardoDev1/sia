import requests
import xml.etree.ElementTree as ET
import pandas as pd
from urllib.parse import quote_plus

def coletar_noticias(termo, max_noticias=15):
    termo_codificado = quote_plus(termo)
    
    # URL do feed RSS do Google News com idioma e região
    url = f"https://news.google.com/rss/search?q={termo_codificado}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    
    # Requisição HTTP
    resposta = requests.get(url)
    noticias = []
    
    if resposta.status_code == 200:
        root = ET.fromstring(resposta.content)
        
        # Encontra todos os itens do feed RSS
        itens = root.findall(".//item")
        print(f"Total de itens retornados pelo RSS: {len(itens)}")
        
        # Percorre até o número máximo definido de notícias
        for item in itens[:max_noticias]:
            titulo = item.find("title").text
            link = item.find("link").text
            descricao = item.find("description").text if item.find("description") is not None else ""
            noticias.append({
                "titulo": titulo, 
                "link": link, 
                "descricao": descricao, 
                "termo": termo
            })
    else:
        print(f"Erro na requisição. Status code: {resposta.status_code}")
    
    return pd.DataFrame(noticias)

