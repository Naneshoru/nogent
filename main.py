from tools.wikipedia_tool import wikipedia_tool
from tools.news_tool import buscar_noticias
from models.llm import llm
from config.settings import load_environment
from langchain.agents import initialize_agent, Tool
from memory.conversation import memory

load_environment()

tools = [
    Tool(
        name="Wikipedia",
        func=wikipedia_tool,
        description="Busca informações na Wikipedia sobre qualquer tema."
    ),
    Tool(
        name="Notícias",
        func=buscar_noticias,
        description="Busca notícias recentes em português sobre qualquer assunto."
    ),
    Tool(
        name="AnalisadorDeTexto",
        func=lambda x: llm.invoke(f"Faça um resumo/tradução/análise de sentimento do seguinte texto:\n{x}"),
        description="Processa textos com tarefas específicas como resumo ou tradução."
    )
]

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