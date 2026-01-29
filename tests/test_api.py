# Importamos pytest, el framework de testing
import pytest
# Importamos la función que crea nuestra aplicación
from app.app import create_app

# ========== FIXTURE: Cliente de pruebas ==========
@pytest.fixture
def client():
    """
    Fixture que crea un cliente de pruebas para hacer peticiones HTTP.
    
    Un 'fixture' en pytest es una función que se ejecuta antes de cada test
    y proporciona recursos necesarios para las pruebas.
    
    Este fixture:
    1. Crea una instancia de la aplicación Flask
    2. La pone en modo testing (desactiva manejo de errores para ver excepciones)
    3. Devuelve un cliente de pruebas que simula peticiones HTTP sin levantar servidor
    """
    app = create_app()
    
    # testing=True hace que Flask lance excepciones en lugar de manejarlas silenciosamente
    app.testing = True
    
    # test_client() crea un cliente que puede hacer peticiones HTTP simuladas
    return app.test_client()

# ========== TEST 1: Obtener items (lista vacía inicialmente) ==========
def test_get_items(client):
    """
    Prueba que el endpoint GET /items funcione correctamente.
    
    Verifica:
    - Que responda con código 200 (éxito)
    - Que devuelva una lista vacía al inicio
    """
    # Hacemos una petición GET al endpoint /items
    response = client.get("/items")
    
    # Verificamos que el código de respuesta sea 200
    assert response.status_code == 200
    
    # Verificamos que el JSON de respuesta sea una lista vacía
    assert response.json == []

# ========== TEST 2: Crear un item ==========
def test_create_item(client):
    """
    Prueba que el endpoint POST /items cree un item correctamente.
    
    Verifica:
    - Que responda con código 201 (recurso creado)
    - Que el mensaje de confirmación sea correcto
    """
    # Hacemos una petición POST enviando datos JSON
    response = client.post("/items", json={"name": "Laptop"})
    
    # Verificamos código 201 (creado)
    assert response.status_code == 201
    
    # Verificamos que el mensaje de respuesta sea el esperado
    assert response.json["message"] == "Item created"

# ========== TEST 3: Actualizar un item ==========
def test_update_item(client):
    """
    Prueba que el endpoint PUT /items/<index> actualice un item.
    
    Pasos:
    1. Primero crea un item (Phone)
    2. Luego lo actualiza a (Tablet)
    3. Verifica que la actualización sea exitosa (código 200)
    """
    # Primero creamos un item para tener algo que actualizar
    client.post("/items", json={"name": "Phone"})
    
    # Actualizamos el item en la posición 0
    response = client.put("/items/0", json={"name": "Tablet"})
    
    # Verificamos que la actualización sea exitosa
    assert response.status_code == 200

# ========== TEST 4: Eliminar un item ==========
def test_delete_item(client):
    """
    Prueba que el endpoint DELETE /items/<index> elimine un item.
    
    Pasos:
    1. Primero crea un item (Mouse)
    2. Luego lo elimina
    3. Verifica que la eliminación sea exitosa (código 200)
    """
    # Primero creamos un item para tener algo que eliminar
    client.post("/items", json={"name": "Mouse"})
    
    # Eliminamos el item en la posición 0
    response = client.delete("/items/0")
    
    # Verificamos que la eliminación sea exitosa
    assert response.status_code == 200
