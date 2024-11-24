import os
import smtplib
import mimetypes
from email.message import EmailMessage
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader


class Email:
    def __init__(self, sender:str, receptor:str):
        self.sender = sender,
        self.receptor = receptor,
        self._password_application,
        self.smtp_port = 587,
        self.smtp_server = "smtp.gmail.com",
        self.msg = EmailMessage()
        
    def get_password_application(self):
        return self._password_application
    
    def set_password_application(self, password:str):
        self._password_application = password
     
    def connect_to_server(self, message:EmailMessage):
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Inicia la conexión segura
                server.login(self.sender, self.get_password_application())  # Inicia sesión
                server.send_message(message)  # Envía el mensaje
        except smtplib.SMTPException as e:
            print(f"Error en el envío de correo: {e}")
            raise e
        print("Correo enviado con éxito.")
            
    def send_simple_message(self,subject:str, message:str):
        simple_msg = self.msg
        simple_msg.set_content(MIMEText(message))
        simple_msg['From'] = self.sender
        simple_msg['To'] = self.receptor
        simple_msg['Subject'] = subject
        
        self.connect_to_server(simple_msg)
    
    def send_templates_html(self, subject:str, message:str, context:dict, path_template_dir:str, path:str):
        msg_wfile = self.msg
        msg_wfile.set_content(MIMEText(message))
        msg_wfile['From'] = self.sender
        msg_wfile['To'] = self.receptor
        msg_wfile['Subject'] = subject
        
        # Cargar y renderizar la plantilla HTML usando Jinja2
        template_dir = os.path.abspath(path_template_dir)  # Carpeta donde tienes la plantilla
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(path)  # Nombre de tu archivo de plantilla
        
        # Renderizar la plantilla con el contexto
        html_content = template.render(context)
        
        # Establecer el contenido del correo como HTML
        msg_wfile.add_alternative(html_content, subtype='html')
        
        # Enviar el correo usando SMTP
        self.connect_to_server(msg_wfile)