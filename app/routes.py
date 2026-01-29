# Importamos las herramientas necesarias de Flask
from flask import Blueprint, request, jsonify

# Creamos un Blueprint llamado "api"
# Un Blueprint es como un módulo que agrupa rutas relacionadas
# Permite organizar mejor el código cuando la aplicación crece
api = Blueprint("api", __name__)

# Simulación de base de datos en memoria
# Esta lista guardará los items temporalmente mientras la app esté corriendo
# NOTA: Los datos se pierden cuando se reinicia el servidor, ya que no hay persistencia y 
# no usamos una base de datos real en este ejemplo
items = []

# ========== ENDPOINT 1: Obtener todos los items ==========
@api.route("/items", methods=["GET"])
def get_items():
    """
    GET /items
    Devuelve la lista completa de items en formato JSON.
    Código 200 = éxito
    """
    # jsonify() convierte la lista de Python a formato JSON
    return jsonify(items), 200

# ========== ENDPOINT 2: Crear un nuevo item ==========
@api.route("/items", methods=["POST"])
def create_item():
    """
    POST /items
    Crea un nuevo item con los datos enviados en el body de la petición.
    Código 201 = recurso creado exitosamente
    """
    # request.json extrae los datos JSON del body de la petición HTTP
    data = request.json
    
    # Agregamos el nuevo item a nuestra "base de datos"
    items.append(data)
    
    # Devolvemos un mensaje de confirmación
    # 201 es el código estándar para "recurso creado"
    return jsonify({"message": "Item created"}), 201

# ========== ENDPOINT 3: Actualizar un item existente ==========
@api.route("/items/<int:index>", methods=["PUT"])
def update_item(index):
    """
    PUT /items/<index>
    Actualiza el item en la posición 'index' con nuevos datos.
    
    Parámetros:
        index (int): La posición del item en la lista (empieza en 0)
    
    Retorna:
        200 si se actualiza correctamente
        404 si el índice no existe
    """
    # Validamos que el índice exista en nuestra lista
    if index >= len(items):
        # Si el índice es mayor que el tamaño de la lista, el item no existe
        return jsonify({"error": "Item not found"}), 404

    # Reemplazamos el item existente con los nuevos datos
    items[index] = request.json
    
    # Devolvemos confirmación de éxito
    return jsonify({"message": "Item updated"}), 200

# ========== ENDPOINT 4: Eliminar un item ==========
@api.route("/items/<int:index>", methods=["DELETE"])
def delete_item(index):
    """
    DELETE /items/<index>
    Elimina el item en la posición 'index'.
    
    Parámetros:
        index (int): La posición del item en la lista (empieza en 0)
    
    Retorna:
        200 si se elimina correctamente
        404 si el índice no existe
    """
    # Validamos que el índice exista
    if index >= len(items):
        return jsonify({"error": "Item not found"}), 404

    # Eliminamos el item de la lista
    # pop() remueve y retorna el elemento en la posición especificada
    items.pop(index)
    
    # Confirmamos la eliminación
    return jsonify({"message": "Item deleted"}), 200
