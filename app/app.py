# Importamos Flask para crear la aplicación web
# Importamos el Blueprint 'api' que contiene todas las rutas/endpoints
from flask import Flask
from app.routes import api

def create_app():
    """
    Función factory que crea y configura la aplicación Flask.
    Este patrón permite crear múltiples instancias de la app (útil para testing).
    """
    # Creamos una instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Registramos el Blueprint 'api' que contiene todas las rutas HTTP
    # Esto conecta todos los endpoints definidos en routes.py a esta aplicación
    app.register_blueprint(api)
    
    return app

# Este bloque solo se ejecuta si corremos este archivo directamente
# No se ejecuta cuando importamos este módulo desde otro lugar (como en los tests)
if __name__ == "__main__":
    # Creamos la aplicación
    app = create_app()
    
    # Iniciamos el servidor web en modo debug
    # debug=True: recarga automáticamente cuando hay cambios y muestra errores detallados
    app.run(debug=True)
