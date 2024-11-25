# Clase `Email`

La clase **`Email`** simplifica el envío de correos electrónicos en Python, soportando correos de texto plano y con plantillas HTML dinámicas. Actualmente, utiliza `smtplib` para conectarse a servidores SMTP y `jinja2` para la personalización de plantillas. Este proyecto seguirá evolucionando con nuevas funcionalidades en el futuro.

## Características actuales
1. **Envío de correos simples** con contenido en texto plano.
2. **Envío de correos HTML dinámicos** usando plantillas personalizables.
3. **Conexión segura a servidores SMTP**, actualmente configurado para Gmail.

---

## Instalación

### Paso 1: Clonar el repositorio
Clona el repositorio donde se encuentra la clase `Email`.

```bash
git clone https://github.com/Dextron03/Class_Email
cd repo-email
```

### Paso 2: Instalar las dependencias
Asegúrate de tener Python instalado y usa el archivo `requirements.txt` para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```
---

## Cómo usar la clase

### Inicialización
Crea una instancia de la clase `Email`, especificando el remitente, el receptor y, opcionalmente, la contraseña de la aplicación:

```python
from email_class import Email

email = Email(sender="tu_correo@gmail.com", receptor="destinatario@gmail.com")
email.set_password_application("contraseña")

```
> [!TIP]
> Para mayor seguridad, se recomienda utilizar variables de entorno al gestionar la contraseña de la aplicación, ya que esta es considerada información sensible.


### Métodos disponibles

#### `get_password_application()`
Obtiene la contraseña de la aplicación configurada.  

**Retorno:**  
- `str`: Contraseña de la aplicación.

---

#### `set_password_application(password:str)`
Permite configurar o actualizar la contraseña de la aplicación.  

**Argumentos:**  
- `password` (str): Nueva contraseña de la aplicación.
---

#### `connect_to_server(message:EmailMessage)`
Conecta al servidor SMTP y envía el mensaje proporcionado.  

**Argumentos:**  
- `message` (EmailMessage): Mensaje de correo a enviar.
---

#### `send_simple_message(subject:str, message:str)`
Envía un correo sencillo con contenido en texto plano.  

**Argumentos:**  
- `subject` (str): Asunto del correo.  
- `message` (str): Cuerpo del correo (en texto plano).

**Ejemplo:**
```python
email.send_simple_message("Prueba", "Este es un mensaje de prueba.")
```
---

#### `send_templates_html(subject:str, path_template_dir:str, path:str, context:dict)`
Envía un correo electrónico usando una plantilla HTML renderizada.  

**Argumentos:**  
- `subject` (str): Asunto del correo.  
- `path_template_dir` (str): Ruta del directorio que contiene la plantilla HTML.  
- `path` (str): Nombre del archivo de la plantilla HTML.  
- `context` (dict): Diccionario de datos para personalizar la plantilla.

**Ejemplo:**
```python
context = {"nombre": "Braily", "curso": "Python"}
email.send_templates_html(
    subject="Bienvenido",
    path_template_dir="./templates",
    path="bienvenida.html",
    context=context
)
```

---

## Funcionalidades futuras
- Soporte para archivos adjuntos.
- Envío a múltiples destinatarios.
- Compatibilidad con otros servicios SMTP (Outlook, Yahoo, etc.).
- Manejo avanzado de errores.
---

## Contribuciones
Se aceptan contribuciones para mejorar y extender la funcionalidad de la clase. Si tienes sugerencias, envía un pull request o abre un issue en el repositorio. 

¡El proyecto está en constante evolución! 🚀

