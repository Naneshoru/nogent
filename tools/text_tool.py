from models import llm

def analisar_texto(comando: str) -> str:
    prompt = (
        "Você é um assistente de linguagem natural. "
        "Interprete e execute a seguinte instrução sobre o texto fornecido:\n\n"
        f"{comando}\n\n"
        "Responda de forma clara e objetiva."
    )
    return llm.invoke(prompt)
