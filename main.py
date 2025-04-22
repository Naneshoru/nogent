from models.llm import llm
from config.settings import load_environment
from langchain.agents import initialize_agent, Tool
from memory.conversation import memory
from tools.wikipedia_tool import wikipedia_tool
from tools.news_tool import buscar_noticias
from langchain.prompts import PromptTemplate
from datetime import datetime

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

prompt_template = PromptTemplate(
    input_variables=["input", "agent_scratchpad"],
    template=(
        "Você é um assistente inteligente. Use as ferramentas disponíveis para responder às perguntas do usuário.\n\n"
        "Pergunta: {input}\n\n"
        "{agent_scratchpad}"
    )
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    memory=memory,
    handle_parsing_errors=True,
    verbose=True,
    prompt=prompt_template
)

if __name__ == "__main__":
    while True:
        query = input("🤖 Pergunte algo: ")
        full_input = f"{query}"
        resposta = agent.invoke({"input": full_input})
        print(resposta)