from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


meu_email = "digite o email que será usado para enviar o email"
senha = "digite a senha desse email"
email_recebe = "email do cliente"

with open ("template_email.html", "r") as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    corpo_msg = template.safe_substitute(nome = "Mago Supremo", data = data_atual)

msg = MIMEMultipart()
msg["from"] = "Natalia Artini Ferrandin"
msg["to"] = email_recebe
msg["subject"] = "EMAIL DE TESTES"

corpo = MIMEText(corpo_msg, "html")
msg.attach(corpo)
email = msg
with smtplib.SMTP(host= "smtp.gmail.com", port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, senha)
    smtp.send_message(msg)
    print("email enviado com sucesso")
