import os
from dotenv import load_dotenv

load_dotenv()

class Configuracao:
    ENDPOINT_DI = os.getenv('DI_ENDPOINT')
    CHAVE_DI = os.getenv('DI_KEY')
    CONEXAO_AZURE_STORAGE = os.getenv('STORAGE_CONNECTION')
    NOME_CONTAINER = os.getenv('CONTAINER_NAME')