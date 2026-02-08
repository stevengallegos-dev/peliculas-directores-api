### Backend – API REST de Películas y Directores
Descripción del Proyecto

Este proyecto corresponde al backend de una aplicación Full-Stack desarrollado con Django y Django REST Framework.
Su objetivo es proveer una API REST segura para la gestión de Directores y Películas.

El backend no renderiza vistas HTML. Su única responsabilidad es exponer endpoints REST, gestionar la autenticación mediante OAuth 2.0 y servir como proveedor de datos para el frontend desarrollado en React.

### Objetivos del Proyecto

Aplicar los conceptos de Programación Orientada a Objetos (POO) mediante el uso de modelos en Django.
Implementar un backend basado en API REST.
Gestionar relaciones entre entidades usando una base de datos relacional.
Implementar seguridad mediante OAuth 2.0.
Probar el funcionamiento del backend utilizando Postman, tal como se trabajó durante el semestre.

### Tecnologías Utilizadas

Python 3.x.
Django.
Django REST Framework.
Django OAuth Toolkit.
SQLite / PostgreSQL.
Postman para pruebas de la API.

### Entidades del Sistema

El sistema maneja dos entidades principales.

Director

La entidad Director contiene los siguientes atributos: nombre, nacionalidad y fecha_nacimiento.

Película

La entidad Película contiene los siguientes atributos: titulo, genero, fecha_estreno, duracion_min y director.

Relación

La relación entre las entidades es de uno a muchos, donde un director puede tener muchas películas y cada película pertenece a un único director.

### Funcionalidades (CRUD)

La API implementa las operaciones CRUD completas.
Se permite listar y obtener registros, crear nuevos registros, actualizar información existente y eliminar registros.
Todas las respuestas del sistema se entregan en formato JSON.

### Endpoints Principales
Autenticación (OAuth 2.0)

El sistema expone el endpoint POST /o/token/ para la obtención del token de acceso.
El token debe enviarse en las peticiones protegidas mediante el header Authorization con el esquema Bearer.

### Directores

GET /api/directores/
POST /api/directores/
PUT /api/directores/{id}/
DELETE /api/directores/{id}/

### Películas

GET /api/peliculas/
POST /api/peliculas/
PUT /api/peliculas/{id}/
DELETE /api/peliculas/{id}/

Todos los endpoints bajo la ruta /api/ están protegidos mediante OAuth 2.0.

### Autenticación y Seguridad

La autenticación se implementó mediante OAuth 2.0 utilizando Django OAuth Toolkit.
El flujo de autenticación consiste en la solicitud de un access_token, el envío del token en las peticiones protegidas y la validación del token por parte del backend para autorizar o rechazar el acceso a los recursos.

Pruebas

Las funcionalidades del backend fueron probadas utilizando Postman.
Durante las pruebas se validó la obtención del token OAuth 2.0, el acceso a endpoints protegidos con Bearer Token, la ejecución de las operaciones CRUD completas, la correcta relación entre Directores y Películas y las respuestas en formato JSON.

### Instalación del Ambiente
Requisitos

Python 3.10 o superior.
Gestor de entornos virtuales.
Base de datos SQLite o PostgreSQL.

### Configuración del entorno (Windows)

### Creación del entorno virtual:

py -m venv venv


### Activación del entorno:

venv\Scripts\activate


### Instalación de dependencias:

pip install -r requirements.txt

### Ejecución del Proyecto

El servidor de desarrollo se inicia con el siguiente comando:

python manage.py runserver


### El backend estará disponible en la dirección:

http://127.0.0.1:8000/

### Estado del Proyecto

El backend se encuentra completamente funcional, con el CRUD implementado, seguridad OAuth 2.0 operativa, pruebas realizadas con Postman y listo para ser consumido por el frontend desarrollado en React.

### Autor

- Steven Gallegos
- Ingeniería de Software – UISEK

### Nota Final

Este backend corresponde a la primera parte del proyecto Full-Stack, sobre la cual se integrará el frontend desarrollado en React.
