# Flask API - CRUD Simple

API RESTful básica construida con Flask que implementa operaciones CRUD (Create, Read, Update, Delete) para gestionar items.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

## Instalación y Configuración

### En Windows:

```powershell
# Clonar el repositorio
git clone https://github.com/IvanRA46/FlaskAPI_CRUD.git
cd flaskapi

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### En Ubuntu/Linux:

```bash
# Clonar el repositorio
git clone https://github.com/IvanRA46/FlaskAPI_CRUD.git
cd flaskapi

# Crear entorno virtual (opcional pero recomendado)
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecutar el Proyecto

### Iniciar el servidor:

**Windows:**
```powershell
python -m app.app
```

**Ubuntu/Linux:**
```bash
python3 -m app.app
```

El servidor se iniciará en `http://127.0.0.1:5000/`

## Ejecutar las Pruebas

### Ejecutar todos los tests:

**Windows:**
```powershell
python -m pytest tests/test_api.py -v
```

**Ubuntu/Linux:**
```bash
python3 -m pytest tests/test_api.py -v
```

### Ejecutar tests con reporte de cobertura:

**Windows:**
```powershell
python -m pytest tests/test_api.py --cov=app --cov-report=html --cov-report=term
```

**Ubuntu/Linux:**
```bash
python3 -m pytest tests/test_api.py --cov=app --cov-report=html --cov-report=term
```

Esto generará:
- Reporte en terminal
- Reporte HTML en la carpeta `htmlcov/` (abre `htmlcov/index.html` en tu navegador)

## Endpoints de la API

### 1. Obtener todos los items
```http
GET /items
```

**Respuesta exitosa (200):**
```json
[
  {"name": "Laptop"},
  {"name": "Mouse"}
]
```

### 2. Crear un nuevo item
```http
POST /items
Content-Type: application/json

{
  "name": "Laptop"
}
```

**Respuesta exitosa (201):**
```json
{
  "message": "Item created"
}
```

### 3. Actualizar un item
```http
PUT /items/0
Content-Type: application/json

{
  "name": "Desktop"
}
```

**Respuesta exitosa (200):**
```json
{
  "message": "Item updated"
}
```

**Error (404):**
```json
{
  "error": "Item not found"
}
```

### 4. Eliminar un item
```http
DELETE /items/0
```

**Respuesta exitosa (200):**
```json
{
  "message": "Item deleted"
}
```

**Error (404):**
```json
{
  "error": "Item not found"
}
```

## Ejemplos de Uso con cURL

### Windows PowerShell:
```powershell
# Obtener items
curl http://localhost:5000/items

# Crear item
curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d '{\"name\":\"Laptop\"}'

# Actualizar item
curl -X PUT http://localhost:5000/items/0 -H "Content-Type: application/json" -d '{\"name\":\"Desktop\"}'

# Eliminar item
curl -X DELETE http://localhost:5000/items/0
```

### Ubuntu/Linux:
```bash
# Obtener items
curl http://localhost:5000/items

# Crear item
curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d '{"name":"Laptop"}'

# Actualizar item
curl -X PUT http://localhost:5000/items/0 -H "Content-Type: application/json" -d '{"name":"Desktop"}'

# Eliminar item
curl -X DELETE http://localhost:5000/items/0
```

## Estructura del Proyecto

```
flaskapi/
├── .github/
│   └── workflows/
│       └── tests.yml        # Configuración de GitHub Actions para CI/CD
├── app/
│   ├── __init__.py          # Marca el directorio como paquete Python
│   ├── app.py               # Configuración y creación de la aplicación Flask
│   └── routes.py            # Definición de endpoints/rutas de la API
├── tests/
│   ├── __init__.py          # Marca el directorio como paquete Python
│   └── test_api.py          # Tests automatizados de la API
├── .gitignore               # Archivos ignorados por Git
├── requirements.txt         # Dependencias del proyecto
├── test_ubuntu.sh           # Script automatizado para probar en Ubuntu
└── README.md                # Este archivo - Documentación del proyecto
```

## Resultados de las Pruebas

Para ver los resultados de las pruebas más recientes, ejecuta:

```bash
python -m pytest tests/test_api.py -v --cov=app --cov-report=term
```

### Ejemplo de salida esperada:

```
tests/test_api.py::test_get_items PASSED       [ 25%]
tests/test_api.py::test_create_item PASSED     [ 50%]
tests/test_api.py::test_update_item PASSED     [ 75%]
tests/test_api.py::test_delete_item PASSED     [100%]

---------- coverage: platform linux, python 3.x.x ----------
Name              Stmts   Miss  Cover
-------------------------------------
app/__init__.py       0      0   100%
app/app.py           10      2    80%
app/routes.py        24      0   100%
-------------------------------------
TOTAL                34      2    94%
```

## Prueba Rápida en Ubuntu

Este proyecto incluye un script automatizado para Ubuntu que instalará dependencias y ejecutará todas las pruebas:

```bash
# Dar permisos de ejecución al script
chmod +x test_ubuntu.sh

# Ejecutar el script
./test_ubuntu.sh
```

El script realizará:
1. Verificación de Python
2. Instalación de dependencias
3. Ejecución de tests
4. Generación de reporte de cobertura
5. Opción para iniciar el servidor


## Notas Importantes

- Esta API utiliza almacenamiento en memoria, los datos se pierden al reiniciar el servidor
- El modo debug está activado para desarrollo, desactívalo en producción
- Los índices de los items comienzan en 0
- Cada test se ejecuta de forma aislada, por lo que la lista de items se reinicia entre tests

## Solución de Problemas

### Error: "Module not found"
```bash
# Asegúrate de estar en el directorio correcto y tener las dependencias instaladas
pip install -r requirements.txt
```

### Error: "Address already in use"
```bash
# El puerto 5000 está ocupado, detén el proceso anterior o cambia el puerto en app.py
```

### Tests fallan en Ubuntu
```bash
# Asegúrate de usar python3 en lugar de python
python3 -m pytest tests/test_api.py -v
```

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.

## 👨‍💻 Autor

Bryan Ivan Noe Ramirez Vivanco


