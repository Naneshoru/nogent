from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.utilities import WikipediaAPIWrapper

from langchain.chat_models import ChatOpenAI
from langchain.llms import Ollama

wikipedia = WikipediaAPIWrapper()

tools = [
    Tool(
        name="Wikipedia",
        func=wikipedia.run,
        description="Busca informações"
    )
]

llm = Ollama(model="mistral")

agent = initialize_agent(
    tools, 
    llm, 
    agent="zero-shot-react-description",
    handle_parsing_errors=True,
    verbose=True
)

if __name__ == "__main__":
    while True:
        query = input("🤖 Pergunte algo: ")
        resposta = agent.run(query)
        print(resposta)
