# API-CRUD

### Bootcamp de DevOps. Entrega Sprint10. Parte 1 - Creación de un entorno local de desarrollo.

Este es un proyecto de una API RESTful construida con Flask, que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un modelo de datos. El proyecto está configurado para pruebas unitarias utilizando `pytest` y tiene cobertura de código mediante `coverage`.

## Características

- **Flask** para la creación de la API.
- **SQLAlchemy** para la gestión de la base de datos.
- **Pruebas automatizadas** utilizando `pytest`.
- **Cobertura de código** con `coverage`.
- **Configuración de pruebas** utilizando un entorno aislado con un `virtualenv` o con **Docker**.

## Requisitos

- Python 3.12 o superior
- Docker 
- Flask
- Flask-SQLAlchemy
- pytest
- coverage
- Werkzeug
- SQLAlchemy

## Instalación

### Paso 1: Instalación y ejecución en entorno local

1. Clona este repositorio:

   ```bash
   git clone https://github.com/xegaca/API-CRUD.git
   cd API-CRUD
   ```

2.	Crea un entorno virtual e instálalo:

    ```bash
    python -m venv .venv
    .venv\Scripts\activate 
    ```

3.	Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4.	Establece las variables de entorno necesarias para ejecutar la aplicación:
	•	Para la base de datos en pruebas, asegúrate de tener configurada la variable de entorno PYTHONPATH:

    ```bash
    set PYTHONPATH=%CD%  
    $env:PYTHONPATH = (Get-Location).Path
    ```

5.	Ejecutar la API:

    Para ejecutar la API en modo desarrollo:

    ```bash
    flask run
    ```

    La API estará disponible en `http://127.0.0.1:5000`.

6.	Ejecutar pruebas:

    Para correr las pruebas unitarias:

    ```bash
    pytest --cov=app
    ```

    Esto ejecutará todas las pruebas y generará un informe de cobertura.

### Paso 2: Instalación y ejecución con Docker

Para simular la ejecución en un entorno real, se utiliza Docker para ejecutar el entorno de pruebas, sigue estos pasos:

1.	Construir la imagen de Docker:

    En el directorio raíz del proyecto, ejecuta el siguiente comando para construir la imagen de Docker:

    ```bash
    docker build -t api-crud .
    ```

2.	Ejecutar los contenedores:

    Una vez que la imagen esté construida, ejecuta el siguiente comando para levantar los contenedores necesarios (esto incluirá el entorno de la aplicación y la base de datos):

    ```bash
    docker-compose up
    ```

    Esto levantará los contenedores de la aplicación y la base de datos (si se ha configurado adecuadamente en el archivo docker-compose.yml).

3.	Acceder a la API:

    La API debería estar accesible en `http://localhost:5000`.

4.	Ejecutar las pruebas en Docker:

    Para ejecutar las pruebas dentro de Docker, puedes ejecutar los siguientes comandos:

    ```bash
    docker-compose exec app pytest --cov=app
    ```

    Esto ejecutará `pytest` dentro del contenedor de la aplicación y mostrará los resultados de las pruebas, así como la cobertura del código.

5.	Detener los contenedores:

    Para detener los contenedores una vez que hayas terminado, puedes usar:

    ```bash
    docker-compose down
    ```

## Rutas disponibles

### POST /data

Inserta un nuevo dato en la base de datos.

**Entrada:**
    
```json
{
  "name": "Test Name"
}
 ```

**Salida:**
	    
- `201 Created`: Si los datos fueron insertados correctamente.
- `409 Conflict`: Si los datos ya existen.

### GET /data

Obtiene todos los datos almacenados.

**Salida:**

```json
[
  {
    "id": 1,
    "name": "Test 1"
  },
  {
    "id": 2,
    "name": "Test 2"
  }
]
```

### DELETE /data/<id>

Elimina un dato por su ID.

**Entrada:**

ID del dato a eliminar.

**Salida:**

- `200 OK`: Si el dato fue eliminado con éxito.
- `404 Not Found`: Si el dato no existe.

### Desarrollo

1.	Estructura del proyecto:

    ```
    API-CRUD/
    ├── app/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── models.py
    │   └── routes.py
    ├── tests/
    │   ├── test_models.py
    │   └── test_routes.py
    ├── .venv/
    ├── docker-compose.yml
    ├── Dockerfile
    ├── requirements.txt
    └── README.md
    ```

2.	Pruebas y cobertura:
Para ver un informe de cobertura de código:

    ```bash
    pytest --cov=app --cov-report=term
    ```

    El informe de cobertura mostrará el porcentaje de código cubierto por las pruebas.

## Licencia

Este proyecto está licenciado bajo la `MIT License`.

## Autor

Jesús Gallego

