from newsdataapi import NewsDataApiClient
import os

api_key = os.environ.get("NEWS_API_KEY")
if not api_key:
    raise ValueError("A variável de ambiente 'NEWS_API_KEY' não está configurada.")

news_api = NewsDataApiClient(apikey=api_key)

def buscar_noticias(query: str) -> str:
    try:
        print(f"🔍 Buscando notícias para o termo: {query}")
        response = news_api.news_api(q=query, language='pt', country='br')
        print(f"📋 Resposta da API: {response}")
        articles = response.get('results', [])

        if not articles:
            return "Nenhuma notícia encontrada para o termo fornecido."

        noticias_formatadas = "\n".join(
            [f"- {artigo['title']} ({artigo['link']})" for artigo in articles[:3]]
        )
        return f"🗞️ Notícias sobre '{query}':\n{noticias_formatadas}"
    except Exception as e:
        return f"Erro ao buscar notícias: {str(e)}"