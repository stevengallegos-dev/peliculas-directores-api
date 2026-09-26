# 🎬 Películas y Directores — Backend API REST

API REST desarrollada con **Django y Django REST Framework** que forma parte de un proyecto **Full Stack** para la gestión de películas y directores.

El backend proporciona los servicios necesarios para consultar, registrar, editar y eliminar información, gestionar la relación entre películas y directores y proteger el acceso a los recursos mediante autenticación **OAuth 2.0**.

---

## 📌 Descripción del proyecto

Este proyecto corresponde al backend de la aplicación Full Stack **Películas y Directores**.

Su objetivo es proporcionar una **API REST** encargada de gestionar la información de películas y directores y servir como proveedor de datos para el frontend desarrollado con React.

El backend no renderiza la interfaz gráfica de la aplicación. Su responsabilidad principal es:

- Exponer endpoints REST.
- Gestionar la información almacenada.
- Implementar operaciones CRUD.
- Gestionar la relación entre películas y directores.
- Proteger los recursos mediante OAuth 2.0.
- Proporcionar respuestas en formato JSON.
- Comunicarse con el frontend desarrollado en React.

---

## 🎯 Objetivos del proyecto

- Aplicar conceptos de Programación Orientada a Objetos mediante modelos de Django.
- Desarrollar un backend basado en una arquitectura API REST.
- Implementar operaciones CRUD completas.
- Gestionar relaciones entre entidades utilizando una base de datos relacional.
- Implementar autenticación y autorización mediante OAuth 2.0.
- Proporcionar información al frontend mediante respuestas JSON.
- Probar los endpoints y la autenticación utilizando Postman.

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Django**
- **Django REST Framework**
- **Django OAuth Toolkit**
- **OAuth 2.0**
- **SQLite / PostgreSQL**
- **Postman**
- **PIP**

---

## 🗃️ Entidades del sistema

El sistema administra dos entidades principales: **Director** y **Película**.

### 🎥 Director

La entidad Director contiene información relacionada con los directores registrados en el sistema.

Principales atributos:

- `nombre`
- `nacionalidad`
- `fecha_nacimiento`

### 🎬 Película

La entidad Película almacena la información correspondiente a cada película.

Principales atributos:

- `titulo`
- `genero`
- `fecha_estreno`
- `duracion_min`
- `director`

---

## 🔗 Relación entre entidades

La relación entre **Director** y **Película** es de **uno a muchos (1:N)**.

```text
Director
   │
   │ 1
   │
   └─────────────── N
                    │
                 Película
```

Esto significa que:

- Un director puede estar relacionado con varias películas.
- Cada película pertenece a un único director.

Esta relación se gestiona mediante los modelos definidos en Django y la base de datos relacional.

---

## ✨ Funcionalidades implementadas

La API permite realizar operaciones CRUD completas sobre las entidades del sistema.

### Directores

- Listar directores.
- Consultar un director.
- Registrar nuevos directores.
- Actualizar información de un director.
- Eliminar directores.

### Películas

- Listar películas.
- Consultar una película.
- Registrar nuevas películas.
- Actualizar información de una película.
- Eliminar películas.
- Asociar películas con sus respectivos directores.

Todas las respuestas de la API se entregan en formato **JSON**.

---

## 🌐 Endpoints principales

### 🔐 Autenticación

Para obtener un token de acceso:

```http
POST /o/token/
```

El token obtenido debe enviarse en las peticiones protegidas mediante el encabezado:

```http
Authorization: Bearer <access_token>
```

---

### 🎥 Directores

#### Listar directores

```http
GET /api/directores/
```

#### Obtener un director

```http
GET /api/directores/{id}/
```

#### Crear un director

```http
POST /api/directores/
```

#### Actualizar un director

```http
PUT /api/directores/{id}/
```

#### Eliminar un director

```http
DELETE /api/directores/{id}/
```

---

### 🎬 Películas

#### Listar películas

```http
GET /api/peliculas/
```

#### Obtener una película

```http
GET /api/peliculas/{id}/
```

#### Crear una película

```http
POST /api/peliculas/
```

#### Actualizar una película

```http
PUT /api/peliculas/{id}/
```

#### Eliminar una película

```http
DELETE /api/peliculas/{id}/
```

Los endpoints protegidos requieren un token OAuth 2.0 válido para permitir el acceso a los recursos.

---

## 🔐 Autenticación y seguridad

La API utiliza **OAuth 2.0** mediante Django OAuth Toolkit para controlar el acceso a los recursos protegidos.

### Flujo de autenticación

El proceso general es:

1. El cliente envía una solicitud de autenticación.
2. El backend valida las credenciales.
3. El servidor genera un `access_token`.
4. El cliente recibe y almacena el token.
5. Las peticiones protegidas incluyen el token mediante el esquema `Bearer`.
6. Django OAuth Toolkit valida el token.
7. Si el token es válido, se permite el acceso al recurso solicitado.
8. Si el token no es válido, el servidor rechaza la solicitud.

Flujo simplificado:

```text
Usuario
   ↓
Frontend React
   ↓
Solicitud de autenticación
   ↓
Django + OAuth 2.0
   ↓
Access Token
   ↓
Petición con Bearer Token
   ↓
API REST
   ↓
Respuesta JSON
```

---

## 🧪 Pruebas con Postman

Las funcionalidades del backend fueron probadas utilizando **Postman**.

Durante las pruebas se verificó:

- Obtención del token OAuth 2.0.
- Acceso a endpoints protegidos mediante Bearer Token.
- Listado de registros.
- Creación de registros.
- Actualización de registros.
- Eliminación de registros.
- Relación entre directores y películas.
- Respuestas de la API en formato JSON.

---

## 📋 Requisitos

Antes de ejecutar el proyecto es necesario contar con:

- **Python 3.10 o superior.**
- **PIP.**
- **Gestor de entornos virtuales de Python.**
- **SQLite o PostgreSQL.**
- **Postman** para realizar pruebas de la API.
- Dependencias definidas en `requirements.txt`.

---

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/stevengallegos-dev/peliculas-directores-api.git
```

### 2. Ingresar al proyecto

```bash
cd peliculas-directores-api
```

### 3. Crear el entorno virtual

En Windows:

```bash
py -m venv venv
```

### 4. Activar el entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

Una vez activado correctamente, normalmente aparecerá `(venv)` al inicio de la terminal.

---

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

### 6. Aplicar las migraciones

```bash
python manage.py migrate
```

Esto prepara las tablas necesarias de Django y las aplicaciones instaladas en la base de datos.

---

### 7. Crear un superusuario

Si se desea acceder al panel administrativo de Django:

```bash
python manage.py createsuperuser
```

Ingresar los datos solicitados por Django.

> No se deben publicar credenciales reales de usuarios o administradores dentro del repositorio.

---

### 8. Configurar OAuth 2.0

Para utilizar los endpoints protegidos es necesario configurar una aplicación OAuth 2.0 en el backend.

La configuración debe realizarse de acuerdo con los parámetros utilizados por el proyecto.

Las credenciales generadas para OAuth 2.0 deben mantenerse privadas y no deben publicarse directamente en el repositorio.

---

### 9. Ejecutar el servidor

```bash
python manage.py runserver
```

El backend estará disponible normalmente en:

```text
http://127.0.0.1:8000/
```

Los endpoints principales de la API estarán disponibles desde:

```text
http://127.0.0.1:8000/api/
```

---

## 🔄 Integración con el Frontend

Este backend trabaja en conjunto con el frontend desarrollado utilizando **React, Vite y Material UI**.

Repositorio del frontend:

**peliculas-directores-frontend**

El flujo general del proyecto es:

```text
Frontend React
      ↓
     Axios
      ↓
   API REST
      ↓
Django REST Framework
      ↓
Base de datos
```

El frontend realiza las solicitudes HTTP y el backend procesa las operaciones correspondientes antes de devolver las respuestas en formato JSON.

---

## 📂 Estructura del proyecto Full Stack

El proyecto completo está dividido en dos aplicaciones independientes:

```text
Películas y Directores
│
├── Frontend
│   ├── React
│   ├── Vite
│   ├── Material UI
│   └── Axios
│
└── Backend
    ├── Python
    ├── Django
    ├── Django REST Framework
    ├── OAuth 2.0
    └── Base de datos
```

Esta separación permite mantener desacoplada la interfaz de usuario de la lógica del servidor.

La comunicación entre ambas aplicaciones se realiza mediante una **API REST**.

---

## 📊 Estado del proyecto

- ✅ Backend funcional.
- ✅ API REST implementada.
- ✅ CRUD de películas.
- ✅ CRUD de directores.
- ✅ Relación entre películas y directores.
- ✅ Respuestas en formato JSON.
- ✅ Autenticación OAuth 2.0.
- ✅ Endpoints protegidos.
- ✅ Pruebas realizadas con Postman.
- ✅ Integración con frontend React.

---

## 👨‍💻 Autor

**Steven Gallegos**  
Estudiante de Ingeniería de Software — UISEK

---

## 📝 Nota final

Este repositorio corresponde al **backend** del proyecto Full Stack **Películas y Directores**.

La API fue desarrollada utilizando **Django y Django REST Framework** y proporciona los servicios necesarios para la gestión de películas y directores.

El backend trabaja en conjunto con un frontend desarrollado en **React**, manteniendo ambas aplicaciones desacopladas y comunicándose mediante una API REST protegida con autenticación OAuth 2.0.