# Fake Docs Validator

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Streamlit](https://img.shields.io/badge/streamlit-0.84.0%2B-brightgreen)
![Azure](https://img.shields.io/badge/azure-blob%20storage-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Fake Docs Validator is a web application that allows users to upload credit card images, sends these images to Azure Blob Storage, and uses Azure Document Intelligence to analyze and validate the card information.

## Features

- Upload credit card images (supported formats: PNG, JPG, JPEG)
- Send images to Azure Blob Storage
- Analyze images using Azure Document Intelligence
- Display credit card information (cardholder name, card number, expiration date, issuing bank)
- Visual validation of the credit card

## Requirements

- Python 3.7+
- Azure account with access to Azure Blob Storage and Azure Document Intelligence
- `streamlit` library
- `azure-core` library
- `azure-ai-documentintelligence` library
- `azure-storage-blob` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/fake-docs-validator.git
    cd fake-docs-validator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add your Azure credentials:
    ```env
    DI-ENDPOINT=your-azure-endpoint
    DI-KEY=your-azure-key
    STORAGE-CONNECTION=your-azure-storage-connection-string
    CONTAINER-NAME=your-container-name
    ```

## Usage

1. Run the application:
    ```sh
    streamlit run app.py
    ```

2. Access the application in your browser at `http://localhost:8501`.

## Project Structure

- `app.py`: Main Streamlit application file.
- `blob_service.py`: Service for uploading files to Azure Blob Storage.
- `card_service.py`: Service for analyzing credit cards using Azure Document Intelligence.
- `config.py`: Project configuration, including Azure credentials.

## Contribution

Contributions are welcome! Feel free to open issues and pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
