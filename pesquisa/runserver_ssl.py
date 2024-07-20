import os
import ssl
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seuprojeto.settings")

    # Certificados SSL
    cert_file = "/home/usuario/meuprojeto/cert.pem"
    key_file = "/home/usuario/meuprojeto/key.pem"

    # Iniciar o servidor com HTTPS
    import django.core.servers.basehttp
    django.core.servers.basehttp.get_internal_wsgi_application = (
        django.core.servers.basehttp.get_internal_wsgi_application
    )

    from django.core.management.commands.runserver import Command as runserver

    runserver.default_port = "8000"
    runserver.default_addr = "0.0.0.0"
    runserver.default_protocol = "https"
    runserver.key_file = key_file
    runserver.cert_file = cert_file

    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
