FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir langchain openai wikipedia

CMD ["python", "agente.py"]
