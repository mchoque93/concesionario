import os

from apiflask import APIFlask

from app.services.orm import start_mappers
from database import db

settings= os.getenv('APP_SETTINGS_MODULE')


def create_app(settings_module=settings):
    app = APIFlask(__name__)
    app.config.from_object(settings_module)

    # Inicializa las extensiones
    with app.app_context():
        db.init_app(app)
        start_mappers()
        db.create_all()

    # Captura todos los errores 404
    #Api(app, catch_all_404s=True)

    # Deshabilita el modo estricto de acabado de una URL con /
    #app.url_map.strict_slashes = False

    # Registra los blueprints
    #app.register_blueprint(pokemon_v1_0_bp)

    # Registra manejadores de errores personalizados
    #register_error_handlers(app)



    return app