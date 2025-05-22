# Chatbot com IA Generativa 🚧

## Descrição

Este projeto é um chatbot backend desenvolvido com Python e FastAPI, integrado com a API da OpenAI para gerar respostas inteligentes usando IA generativa. As conversas são armazenadas em um banco de dados SQLite. O objetivo é construir um projeto júnior que demonstre conhecimentos em backend, banco de dados e IA.

---

## Tecnologias utilizadas

- Python 3.10+
- FastAPI
- Uvicorn (servidor ASGI)
- SQLite (banco de dados leve e simples)
- OpenAI API (GPT-3.5 turbo)
- python-dotenv (para gerenciar variáveis de ambiente)

---

## Funcionalidades

- Servidor FastAPI com rotas REST
- Integração com OpenAI para gerar respostas em linguagem natural
- Armazenamento de conversas em SQLite para manter contexto
- Endpoint `/chat` que recebe mensagens e retorna respostas da IA
- Documentação automática das rotas via Swagger UI

---

## Como rodar localmente

### Pré-requisitos

- Python 3.10 ou superior instalado
- Conta e chave de API da OpenAI (https://platform.openai.com/account/api-keys)

### Passos

1. Clone este repositório:
   
   git clone https://github.com/luaramaciel/chatbot-atendimento.git  
   cd chatbot-atendimento

2. Crie e ative o ambiente virtual:
   
  python -m venv venv  
  Windows :arrow_right: .\venv\Scripts\activate  
  macOS/Linux :arrow_right: source venv/bin/activate

3. Instale as dependências:
   
   pip install -r requirements.txt

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave API da OpenAI:
   
   OPENAI_API_KEY=sua_chave_aqui

5. Rode o servidor FastAPI:
   
   uvicorn main:app --reload

6. Acesse a documentação da API em:
   
   http://127.0.0.1:8000/docs

---

## Endpoints principais

- `GET /` – Rota de teste que retorna uma mensagem de boas-vindas.  
- `POST /chat` – Envia uma mensagem para o chatbot e recebe uma resposta gerada pela IA.
