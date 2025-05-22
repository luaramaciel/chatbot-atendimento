# Chatbot de Atendimento com IA Generativa e Logs Inteligentes 🚧
## Descrição
Projeto Full Stack simples que integra um backend em Python (FastAPI) com uma API de IA generativa da OpenAI e um frontend básico em HTML + JavaScript. Permite ao usuário fazer perguntas ao chatbot, receber respostas geradas pela IA e salvar o histórico das conversas em um banco SQLite.

## Funcionalidades

### Backend (FastAPI + SQLite)
- Rota POST `/chat`: recebe a pergunta do usuário, envia para a OpenAI, salva pergunta e resposta no banco de dados, e retorna a resposta.
- Rota GET `/logs`: retorna o histórico de conversas salvas no banco de dados.
- Banco SQLite para armazenar conversas com colunas: id, pergunta, resposta e data/hora.
- Tratamento básico de erros, como falha na API ou entrada vazia.

### Frontend (HTML + JavaScript)
- Formulário simples para o usuário digitar perguntas e enviar.
- Exibição da resposta da IA logo após o envio.
- Área para mostrar o histórico da conversa atual (opcional).
- Feedback visual durante o carregamento da resposta.

---

## Tecnologias usadas

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [OpenAI API](https://platform.openai.com/docs/)
- HTML5 e JavaScript (Vanilla)
- [python-dotenv](https://pypi.org/project/python-dotenv/) para variáveis de ambiente

---
