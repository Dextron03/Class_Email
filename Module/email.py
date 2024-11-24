import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText

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
            
    def send_simple_message(self,subject:str, message:str):
        simple_msg = self.msg
        simple_msg.set_content(MIMEText(message))
        simple_msg['From'] = self.sender
        simple_msg['To'] = self.receptor
        simple_msg['Subject'] = subject
        
        self.connect_to_server(simple_msg)
        