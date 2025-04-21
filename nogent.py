from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.utilities import WikipediaAPIWrapper

from langchain.chat_models import ChatOpenAI
from langchain.llms import Ollama
from newsdataapi import NewsDataApiClient
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
import os

load_dotenv()

wikipedia = WikipediaAPIWrapper()

api_key = os.environ.get("API_KEY")
if not api_key:
    raise ValueError("A variável de ambiente 'API_KEY' não está configurada.")

news_api = NewsDataApiClient(apikey=api_key)

def buscar_noticias(query: str) -> str:
    try:
        response = news_api.news_api(q=query)
        articles = response.get('results', [])

        if not articles:
            return "Nenhuma notícia encontrada para o termo fornecido."

        noticias_formatadas = "\n".join(
            [f"- {artigo['title']} ({artigo['link']})" for artigo in articles[:3]]
        )
        return f"📵️ Notícias sobre '{query}':\n{noticias_formatadas}"

    except Exception as e:
        return f"Erro ao buscar notícias: {str(e)}"

tools = [
    Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Busca informações na Wikipedia sobre qualquer tema."
    ),
    Tool(
        name="Notícias",
        func=buscar_noticias,
        description="Busca notícias recentes em português sobre qualquer assunto. Ex: 'últimas notícias sobre eleições no Brasil'."
    ),
]

llm = Ollama(model="mistral")

memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    memory=memory,
    handle_parsing_errors=True,
    verbose=True
)

if __name__ == "__main__":
    while True:
        query = input("🤖 Pergunte algo: ")
        resposta = agent.invoke({"input": query})
        print(resposta)
