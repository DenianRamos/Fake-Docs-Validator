import streamlit as st
from services.azure_blob_handler import store_blob
from services.card_service import process_credit_card

def configure_interface():
    st.title("Desafio de Upload de Documentos - Validador de Docs")
    arquivo_carregado = st.file_uploader("Selecione um arquivo", type=["png", "jpg", "jpeg"])

    if arquivo_carregado is not None:
        nome_do_documento = arquivo_carregado.name
        # Enviar para o armazenamento de blob
        url_blob_azure = store_blob(arquivo_carregado, nome_do_documento)
        if url_blob_azure:
            st.write(f"Arquivo {nome_do_documento} enviado com sucesso para o Azure Blob Storage!")
            detalhes_do_cartao = process_credit_card(url_blob_azure)
            mostrar_imagem_e_validacao(url_blob_azure, detalhes_do_cartao)
        else:
            st.write(f"Erro ao enviar o arquivo {nome_do_documento} para o Azure Blob Storage!")

def mostrar_imagem_e_validacao(url_blob_azure, detalhes_do_cartao):
    st.image(url_blob_azure, caption="Imagem Enviada", use_column_width=True)
    st.write("Resultado da Validação:")
    if detalhes_do_cartao and detalhes_do_cartao["nome_do_cartao"]:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {detalhes_do_cartao['nome_do_cartao']}")
        st.write(f"Banco Emissor: {detalhes_do_cartao['nome_do_banco']}")
        st.write(f"Data de Expiração: {detalhes_do_cartao['data_de_validade']}")
    else:
        st.markdown(f"<h1 style='color:blue;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("O Cartão não é valido!.")

if __name__ == "__main__":
    configure_interface()