Agent Project
Este projeto é um assistente inteligente que utiliza ferramentas como Wikipedia, Google Calendar e APIs de notícias para responder a perguntas e realizar tarefas. Ele é integrado com o framework LangChain para gerenciar agentes e ferramentas.

Recursos
Wikipedia Tool: Busca informações na Wikipedia.
News Tool: Obtém notícias recentes com base em consultas e intervalos de datas.
Calendar Tool: Consulta eventos do Google Calendar.
Prompt Personalizado: Configuração de prompts para interagir com o modelo de linguagem.
Integração com Telegram: Pode ser configurado para responder via bot do Telegram.
Requisitos
Python: Certifique-se de ter o Python 3.8 ou superior instalado.
Bibliotecas Necessárias:
Instale as dependências listadas no arquivo requirements.txt:
Credenciais:
Google Calendar:
Configure os arquivos credentials.json e token.json para acessar sua conta do Google.
News API:
Adicione sua chave de API no arquivo .env:
Configuração
Clone o Repositório:

Instale as Dependências:

Configure as Credenciais:

Coloque o arquivo credentials.json na raiz do projeto para o Google Calendar.
Certifique-se de que o arquivo .env contém a chave da API de notícias.
Uso
Execução Local
Execute o programa principal:

Integração com Telegram
Configure o token do bot no código:
Execute o programa:
Estrutura do Projeto
Exemplo de Uso
Perguntas Suportadas
Wikipedia:
"O que é inteligência artificial?"
Notícias:
"Quais são as notícias de hoje sobre tecnologia?"
Agenda:
"Quais são os meus próximos eventos?"