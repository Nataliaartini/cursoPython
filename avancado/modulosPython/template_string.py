from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

with open ("template_email.html", "r") as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    corpo_msg = template.safe_substitute(nome = "Mago Supremo", data = data_atual)
print(corpo_msg)

