# **Agent Project**

Este projeto é um assistente inteligente que utiliza ferramentas como Wikipedia, Google Calendar e APIs de notícias para responder a perguntas e realizar tarefas. Ele é integrado com o framework LangChain para gerenciar agentes e ferramentas.

---

## **Recursos**

- **Wikipedia Tool**: Busca informações na Wikipedia.
- **News Tool**: Obtém notícias recentes com base em consultas e intervalos de datas.
- **Calendar Tool**: Consulta eventos do Google Calendar.
- **Prompt Personalizado**: Configuração de prompts para interagir com o modelo de linguagem.

---

## **Requisitos**

1. **Python**: Certifique-se de ter o Python 3.8 ou superior instalado.
2. **Bibliotecas Necessárias**:
   - Instale as dependências listadas no arquivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```
3. **Credenciais**:
   - **Google Calendar**:
     - Configure os arquivos `credentials.json` e `token.json` para acessar sua conta do Google.
   - **News API**:
     - Adicione sua chave de API no arquivo `.env`:
       ```properties
       NEWS_API_KEY=your_api_key_here
       ```

---

## **Configuração**

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/agent.git
   cd agent
   ```

2. **Virtual environment**:
  ```bash
  source .venv/Scripts/activate
  ```
3. **Rodar o projeto**:
  ```bash
  python main.py
  ```