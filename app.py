import streamlit as st
from datetime import date
import pdfkit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tempfile
import base64

# Função para gerar PDF e permitir o download
def gerar_pdf(html_content):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        pdfkit.from_string(html_content, tmpfile.name)
        return tmpfile.name

# Função para enviar email
def enviar_email(sender_email, password, destinatario, cc, assunto, corpo):
    receiver_email = destinatario

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Cc"] = cc
    message["Subject"] = assunto

    message.attach(MIMEText(corpo, "html"))

    with smtplib.SMTP_SSL("mail.creativebox.com.br", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, [receiver_email, cc], message.as_string())

# Função para gerar o conteúdo HTML da proposta
def gerar_conteudo_html(nome_completo, empresa, data, apresentacao, objetivo_principal, objetivo_secundario, publico_alvo):
    return f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Proposta de Gestão de Tráfego Pago</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                position: relative;
                color: #00327b;
            }}
            .header, .footer {{
                width: 100%;
                text-align: center;
            }}
            .header {{
                border-bottom: 2px solid #003366;
                padding-bottom: 10px;
            }}
            .footer {{
                border-top: 2px solid #003366;
                padding-top: 10px;
            }}
            .content {{
                margin-top: 20px;
                margin-bottom: 20px;
            }}
            h1 {{
                text-align: center;
                color: #003366;
            }}
            h2 {{
                color: #003366;
            }}
            .date-location {{
                text-align: center;
                font-style: italic;
            }}
            .contact {{
                font-weight: bold;
                color: #003366;
            }}
            .epigraph {{
                font-style: italic;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>

    <div class="header">
        <img src="https://creativebox.com.br/wp-content/uploads/2024/05/Logo_fundotransparente-1.png" alt="Logo" width="200">
    </div>

    <div class="content">
        <h1>Proposta de Gestão de Tráfego Pago para {nome_completo} - {empresa}</h1>
        <p class="date-location">{data}</p>
        <h2>Apresentação:</h2>
        <p>Prezado {nome_completo},</p>
        <p>{apresentacao}</p>
        <h2>Objetivo da Campanha:</h2>
        <p>{objetivo_principal}, destacando {objetivo_secundario}.</p>
        <h2>Serviços Oferecidos:</h2>
        <p><strong>1. Meta Ads:</strong></p>
        <ul>
            <li>Criação e gerenciamento de campanhas no Facebook e Instagram.</li>
            <li>Segmentação de público-alvo específico para homens e mulheres de Montenegro-RS até 60 anos, interessados em artes marciais, condicionamento físico e emagrecimento.</li>
            <li>Monitoramento e otimização contínua para maximizar os resultados.</li>
        </ul>
        <p><strong>2. Google Ads:</strong></p>
        <ul>
            <li>Criação e gerenciamento de campanhas no Google Search e Display.</li>
            <li>Uso de palavras-chave estratégicas para atrair potenciais alunos que buscam por aulas de artes marciais na região de Montenegro-RS.</li>
            <li>Monitoramento e otimização contínua para garantir o melhor retorno sobre o investimento.</li>
        </ul>
        <p><strong>3. Criação de Site e Landing Page:</strong></p>
        <ul>
            <li>Desenvolvimento de um site moderno e responsivo para {empresa}.</li>
            <li>Criação de uma landing page otimizada para conversões, destacando os benefícios das aulas e facilitando o processo de inscrição.</li>
            <li>Integração com ferramentas de análise para monitorar o desempenho e ajustar as estratégias conforme necessário.</li>
        </ul>
        <h2>Orçamento e Duração:</h2>
        <p>Orçamento inicial: R$ 100,00 para começar.</p>
        <p>A campanha será ajustada conforme a performance e continuará até o término do orçamento inicial.</p>
        <p>Recomendamos um acompanhamento contínuo para ajustes e otimizações conforme necessário.</p>
        <h2>Público-Alvo:</h2>
        <p>{publico_alvo}</p>
        <h2>Benefícios da Nossa Parceria:</h2>
        <p>Experiência e expertise em campanhas de Meta Ads e Google Ads.</p>
        <p>Foco em resultados mensuráveis e aumento no número de matrículas.</p>
        <p>Comunicação constante e transparente para garantir que as expectativas sejam atendidas e superadas.</p>
        <h2>Estrutura de Cobrança:</h2>
        <p><strong>1. Serviço Mínimo:</strong></p>
        <ul>
            <li>R$ 100,00 para iniciar a campanha.</li>
        </ul>
        <p><strong>2. Campanhas até R$ 1.000,00:</strong></p>
        <ul>
            <li>Cobrança de 50% do valor da campanha.</li>
        </ul>
        <p><strong>3. Campanhas acima de R$ 1.000,00:</strong></p>
        <ul>
            <li>Sem contrato: R$ 500,00 a R$ 1.000,00 por mês, dependendo do escopo.</li>
            <li>Contrato de 3 meses: R$ 700,00 por mês.</li>
            <li>Contrato de 6 meses: R$ 500,00 por mês.</li>
        </ul>
        <h2>Criação de Landing Pages e Sites:</h2>
        <p>Cada necessidade é avaliada através de uma consultoria gratuita, mas os valores giram em torno de R$ 497,00 a R$ 2.300,00 para landing pages e sites.</p>
        <h2>Próximos Passos:</h2>
        <p>Confirmação do orçamento disponível.</p>
        <p>Início do desenvolvimento das campanhas e da criação do site e landing page.</p>
        <p>Relatórios periódicos de desempenho e sugestões de ajustes para otimização contínua.</p>
        <p class="epigraph">"Porque sou eu que conheço os planos que tenho para vocês, diz o Senhor, planos de fazê-los prosperar e não de lhes causar dano, planos de dar-lhes esperança e um futuro." - Jeremias 29:11</p>
        <h2>Contato:</h2>
        <p>Estamos à disposição para quaisquer dúvidas ou para marcar uma reunião para discutir esta proposta em mais detalhes.</p>
        <p class="contact">Atenciosamente,<br>Lucas Teixeira<br>Creative Box<br>51 999781584<br>contato@creativebox.com.br</p>
    </div>

    <div class="footer">
        <img src="https://creativebox.com.br/wp-content/uploads/2024/05/Logo_fundotransparente-1.png" alt="Logo" width="200">
    </div>

    </body>
    </html>
    """

# Formulário para entrada de dados
with st.form("form_proposta"):
    nome_completo = st.text_input("Nome Completo")
    empresa = st.text_input("Empresa")
    apresentacao = st.text_area("Apresentação", "É com grande satisfação que apresentamos nossa proposta de serviços de gestão de tráfego pago para o Duo Fight Club. Nosso objetivo é alavancar suas matrículas através de estratégias eficientes de publicidade online, utilizando Meta Ads, Google Ads e a criação de um site e landing page atrativos.")
    objetivo_principal = st.text_input("Objetivo Principal", "Aumentar o número de matrículas")
    objetivo_secundario = st.text_input("Objetivo Secundário", "os benefícios das aulas de artes marciais, como aprendizado de novos estilos de luta, condicionamento físico e emagrecimento")
    publico_alvo = st.text_area("Público Alvo", "Homens e mulheres de Montenegro-RS, sem limite mínimo de idade, até 60 anos.\nInteressados em aprender um estilo de luta, condicionamento físico e emagrecimento.")
    
    submit = st.form_submit_button("Gerar Proposta")

if submit:
    data_atual = date.today().strftime('%d de %B de %Y')
    conteudo_html = gerar_conteudo_html(nome_completo, empresa, data_atual, apresentacao, objetivo_principal, objetivo_secundario, publico_alvo)
    st.session_state['conteudo_html'] = conteudo_html
    st.success("Proposta gerada com sucesso! Agora você pode gerar o PDF ou enviar o e-mail.")

if 'conteudo_html' in st.session_state:
    conteudo_html = st.session_state['conteudo_html']
    
    if st.button("Gerar PDF"):
        pdf_path = gerar_pdf(conteudo_html)
        with open(pdf_path, "rb") as pdf_file:
            b64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
        st.markdown(f"<a href='data:application/octet-stream;base64,{b64_pdf}' download='proposta.pdf'>Download do PDF</a>", unsafe_allow_html=True)
        st.success("PDF gerado com sucesso!")

    with st.form("form_envio_email"):
        st.write("Insira suas credenciais de e-mail")
        sender_email = st.text_input("Seu Email")
        password = st.text_input("Sua Senha", type="password")
        destinatario = st.text_input("Email do Destinatário", "cliente@example.com")
        cc = st.text_input("Cc", "contato@creativebox.com.br")
        assunto = "Proposta de Gestão de Tráfego Pago"
        enviar = st.form_submit_button("Enviar Email")
        
        if enviar:
            enviar_email(sender_email, password, destinatario, cc, assunto, conteudo_html)
            st.success("Email enviado com sucesso!")