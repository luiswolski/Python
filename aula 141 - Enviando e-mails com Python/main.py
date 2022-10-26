from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

"""
PARA PERMITIR O ENVIO DE EMAIL NO GMAIL FAÇA OS SEGUINTES PASSOS:
VÁ NO SEU PERFIL EM CONFIGURAÇÕES AVANÇADAS
EM SEGURANÇA VOCÊ DEVE TER O LOGIN EM DUAS ETAPAS ATIVADO
E APOS ISSO VC GERA UMA SENHA DE APP
A SENHA DE APP DEVE SER UTILIZADA EM SUA_SENHA
"""

meu_email = 'SEU_EMAIL@gmail.com'
minha_senha = 'SUA_SENHA'


with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Luis', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'SEU NOME'
msg['to'] = meu_email
msg['subject'] = 'ASSUNTO'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)
    print('Email enviado com sucesso')
