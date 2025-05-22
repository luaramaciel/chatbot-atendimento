import os
from openai import OpenAI
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)  # Carrega o .env mesmo fora da raiz

api_key = os.getenv("OPENAI_API_KEY")
project_id = os.getenv("OPENAI_PROJECT_ID")
org_id = os.getenv("OPENAI_ORG_ID")

# Inicializa o cliente OpenAI moderno
client = OpenAI(
    api_key=api_key,
    organization=org_id,
    project=project_id
)

def chamar_openai(pergunta: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": pergunta}
        ]
    )
    return response.choices[0].message.content.strip()
