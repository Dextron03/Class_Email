import os
import smtplib
import mimetypes
from email.message import EmailMessage
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader


class Email:
    def __init__(self, sender:str, receptor:str, password:str=None):
        """
        Inicializa una instancia de la clase Email.

        :param sender: str, Dirección de correo electrónico del remitente.
        :param receptor: str, Dirección de correo electrónico del receptor.
        :param password: str, Contraseña de applicacion.
        """
        self.sender = sender
        self.receptor = receptor
        self._password_application : str = password
        self.smtp_port = 587
        self.smtp_server = "smtp.gmail.com"
        self.msg = EmailMessage()
        
    def get_password_application(self):
        """
        Obtiene la contraseña de la aplicación para el servidor SMTP.

        :return: str, La contraseña de la aplicación almacenada.
        """
        return self._password_application
    
    def set_password_application(self, password:str):
        """
        Establece la contraseña de la aplicación para el servidor SMTP.

        :param password: str, Contraseña de la aplicación.
        """
        self._password_application = password
     
    def connect_to_server(self, message:EmailMessage):
        """
        Conecta al servidor SMTP y envía el mensaje.

        :param message: EmailMessage, El mensaje de correo que se enviará.
        """
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Inicia la conexión segura
                server.login(self.sender, self.get_password_application())  # Inicia sesión
                server.send_message(message)  # Envía el mensaje
        except smtplib.SMTPException as e:
            print(f"Error en el envío de correo: {e}")
            raise e
        print("Correo enviado con éxito.")
            
    def send_simple_message(self, subject:str, message:str):
        """
        Envía un correo electrónico sencillo con contenido de texto.

        :param subject: str, El asunto del correo.
        :param message: str, El contenido del mensaje (cuerpo del correo).
        """
        simple_msg = self.msg
        simple_msg.set_content(MIMEText(message))
        simple_msg['From'] = self.sender
        simple_msg['To'] = self.receptor
        simple_msg['Subject'] = subject
        
        self.connect_to_server(simple_msg)
    
    def send_templates_html(self, subject:str, message:str, context:dict, path_template_dir:str, path:str):
        """
        Envía un correo electrónico con una plantilla HTML renderizada.

        :param subject: str, El asunto del correo.
        :param message: str, Un mensaje de texto que se incluirá en el correo.
        :param context: dict, Diccionario que contiene los valores para rellenar las variables dentro de la plantilla HTML.
        :param path_template_dir: str, Ruta del directorio donde se encuentra la plantilla HTML.
        :param path: str, Nombre del archivo de la plantilla HTML.
        """
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
