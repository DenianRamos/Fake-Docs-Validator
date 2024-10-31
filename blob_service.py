import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.config import Configuration

def store_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Configuration.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Configuration.CONTAINER_NAME, blob=file_name)
        blob_client.store_blob(file, overwrite=True)
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {ex}")
        return None