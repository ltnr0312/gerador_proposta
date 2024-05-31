# Gerador de Propostas de Gestão de Tráfego Pago

Este é um aplicativo de Streamlit para gerar propostas de gestão de tráfego pago, permitindo que os usuários insiram informações personalizadas, gerem um PDF e enviem a proposta por e-mail.

## Funcionalidades

- Formulário para entrada de dados do cliente e da proposta.
- Geração de conteúdo HTML personalizado para a proposta.
- Conversão do conteúdo HTML em PDF.
- Download do PDF gerado.
- Envio de e-mails com a proposta anexada.

## Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/)
- [pdfkit](https://pypi.org/project/pdfkit/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [MIME](https://docs.python.org/3/library/email.mime.html)

## Instalação

1. Clone o repositório para a sua máquina local:
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```

4. Instale o `wkhtmltopdf`:
    - **Windows**: Baixe e instale o `wkhtmltopdf` [aqui](https://github.com/wkhtmltopdf/packaging/releases).
    - **macOS**: Instale via Homebrew:
        ```sh
        brew install wkhtmltopdf
        ```
    - **Linux**: Instale via apt:
        ```sh
        sudo apt-get install wkhtmltopdf
        ```

## Uso

1. Execute o aplicativo Streamlit:
    ```sh
    streamlit run app.py
    ```

2. Preencha o formulário com os dados do cliente e da proposta.

3. Clique em "Gerar Proposta" para criar o conteúdo HTML da proposta.

4. Use os botões para gerar o PDF e fazer o download ou enviar o e-mail com a proposta anexada.

## Configuração de E-mail

Para enviar e-mails, o aplicativo pedirá suas credenciais de e-mail diretamente na interface. Certifique-se de que seu provedor de e-mail permite o login via aplicativos de terceiros.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Abra uma issue ou envie um pull request com melhorias.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Lucas Teixeira - [contato@creativebox.com.br](mailto:contato@creativebox.com.br)