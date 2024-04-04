importar os
importar solicitudes
de dotenv importar load_dotenv
importar jinja2

load_dotenv()

DOMINIO = os.getenv("MAILGUN_DOMAIN")
cargador_de_plantilla = jinja2.FileSystemLoader("plantillas")
entorno_de_plantilla = jinja2.Environment(cargador=cargador_de_plantilla)


def renderizar_plantilla(nombre_de_archivo_de_plantilla, **contexto):
    return entorno_de_plantilla.get_template(nombre_de_archivo_de_plantilla).render(**contexto)


def enviar_mensaje_sencillo(para, asunto, cuerpo, html):
    return solicitudes.post(
        f"https://api.mailgun.net/v3/{DOMINIO}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={
            "from": f"Jose Salvatierra <mailgun@{DOMINIO}>",
            "to": [para],
            "subject": asunto,
            "text": cuerpo,
            "html": html,
        },
    )


def enviar_correo_electronico_de_registro_de_usuario(correo_electronico, nombre_de_usuario):
    return enviar_mensaje_sencillo(
        correo_electronico,
        "Registro exitoso",
        f"¡Hola {nombre_de_usuario}! Te has registrado correctamente en la API REST de Stores.",
        renderizar_plantilla("email/registro.html", username=nombre_de_usuario),
    )
