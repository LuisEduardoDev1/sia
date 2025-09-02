Este documento registra algumas das **decisões de projeto** tomadas durante o desenvolvimento do sistema de dashboard das notícias sobre IA no Piauí.

---

## 1. Abordagem de Regras para Análise de Sentimento

Optamos por uma **abordagem baseada em regras simples** para classificar os sentimentos (Positivo, Negativo, Neutro), em vez de utilizar **modelos de Machine Learning**, pois devido ao pouco tempo de realização do sistema e o pouco conhecimento em streamlit, a comparação de strings do texto e descrição da notícia com duas lista de strings ganharia tempo para o desenvolvimento do dashboard.

---

## 2. Tratamento de Erros e Falta de Notícias no RSS

Durante a coleta de dados via feed RSS do Google News, foram considerados possíveis problemas:

- ❌ **Feed vazio ou erro de conexão**  
  - Se a requisição HTTP retornar erro, exibimos a mensagem com o **status code**.  
  - Se o RSS não contiver notícias, retornamos um **DataFrame vazio** para evitar falhas no fluxo.  

- 🔄 **Número limitado de notícias**  
  - Mesmo que o feed traga centenas de itens, limitamos o processamento a um número definido (`max_noticias`) para manter a execução rápida por ordem do case fornecido que limitiava a 15 notícias.  

- ✅ **Validação dos dados**  
  - Antes de salvar ou processar, garantimos que títulos, links e descrições sejam extraídos com segurança (checando se os campos existem).  

---