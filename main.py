from models.llm import llm
from config.settings import load_environment
from langchain.agents import initialize_agent, Tool
from memory.conversation import memory
from tools.calendar_tool import listar_eventos
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
    ),
     Tool(
        name="Agenda",
        func=listar_eventos,
        description="Consulta os próximos eventos da sua agenda no Google Calendar."
    )
]

prompt_template = PromptTemplate(
    input_variables=["input", "agent_scratchpad", "current_date"],
    template=(
        "Hoje é {current_date}.\n"
        "Você é um assistente inteligente. Use as ferramentas disponíveis para responder às perguntas do usuário.\n\n"
        "Pergunta: {input}\n\n"
        "{agent_scratchpad}\n\n"
        "Se você precisar usar uma ferramenta, siga este formato:\n"
        "Thought: [Seu pensamento aqui]\n"
        "Action: [Nome da Ferramenta]\n"
        "Action Input: [Entrada para a ferramenta ou deixe vazio com \"\"]\n\n"
        "Se você já souber a resposta final, forneça-a neste formato:\n"
        "Final Answer: [Sua resposta final]\n"
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
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        full_input = f"Hoje é {current_date}. {query}"
        resposta = agent.invoke({"input": full_input})
        print(resposta)