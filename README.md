# Sillage — Blog de Perfumería

Sillage es una aplicación web desarrollada con Python y Django que permite a los usuarios compartir reseñas, opiniones y experiencias sobre perfumes.

El proyecto fue desarrollado como entrega final del curso de Python, aplicando conceptos de programación orientada a objetos, bases de datos, desarrollo web, autenticación de usuarios y operaciones CRUD.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Pillow
- python-decouple
- Git y GitHub

## Funcionalidades principales

### Gestión de publicaciones

- Listar todas las publicaciones.
- Visualizar el detalle de cada reseña.
- Crear, editar y eliminar publicaciones desde la interfaz web.
- Cargar imágenes de perfumes.
- Mostrar correctamente publicaciones sin imagen.
- Clasificar perfumes en categorías: diseñador, árabe y nicho.

### Usuarios y autenticación

- Registro de nuevos usuarios.
- Inicio y cierre de sesión.
- Identificación de usuarios autenticados y visitantes anónimos.
- Protección de las rutas de creación, edición y eliminación.
- Permisos para que cada usuario solamente pueda modificar o eliminar sus propias publicaciones.

### Búsqueda y filtros

- Búsqueda de publicaciones por título o contenido.
- Filtros por categoría.
- Combinación de búsqueda y filtros.
- Mensajes cuando no existen resultados.

### Interfaz

- Diseño oscuro con detalles dorados.
- Interfaz responsive mediante Bootstrap.
- Navegación adaptada al estado de autenticación del usuario.

## Instalación y ejecución

### 1. Requisitos previos

Tener instalados Python, pip y Git.

### 2. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/sillage-blog.git
cd sillage-blog
```

Reemplazar `TU-USUARIO` por el nombre de usuario correspondiente de GitHub.

### 3. Crear el entorno virtual

En Windows:

```powershell
py -m venv venv
```

Activarlo desde PowerShell, si está permitido:

```powershell
.\venv\Scripts\Activate.ps1
```

También es posible ejecutar directamente `.\venv\Scripts\python.exe` sin activar el entorno.

### 4. Instalar dependencias

Con el entorno virtual activado:

```bash
python -m pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Copiar el archivo `.env.example` y renombrar la copia a `.env`.

En el archivo `.env`, configurar las siguientes variables:

```dotenv
SECRET_KEY=TU_CLAVE_SECRETA
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Para generar una clave secreta nueva:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Reemplazar `TU_CLAVE_SECRETA` por el valor generado.

El archivo `.env` contiene configuraciones privadas y no debe subirse al repositorio.

### 6. Aplicar las migraciones

```bash
python manage.py migrate
```

Este comando crea las tablas necesarias en la base de datos SQLite.

### 7. Iniciar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Crear un superusuario

Para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

Completar el nombre de usuario, correo electrónico y contraseña solicitados.

Después de iniciar el servidor, ingresar a:

http://127.0.0.1:8000/admin/

## Uso del blog

Al ingresar a Sillage, cualquier visitante puede consultar las publicaciones y utilizar el buscador.

Para crear una reseña, primero debe registrarse o iniciar sesión.

Los usuarios autenticados pueden crear publicaciones con título, contenido, categoría e imagen opcional.

Cada autor puede editar o eliminar sus propias publicaciones. Las publicaciones de otros usuarios solamente pueden consultarse.

## Base de datos e imágenes

El repositorio no incluye `db.sqlite3` ni la carpeta `media/`, ya que se excluyen mediante `.gitignore`.

Para reconstruir la base de datos, ejecutar:

```bash
python manage.py migrate
```

Después se puede crear una cuenta desde `/registro/` y añadir publicaciones desde la interfaz web.

Las imágenes se almacenan automáticamente en `media/posts/` cuando se cargan desde el formulario de publicaciones. Esta carpeta se crea cuando es necesaria.

## Estructura del proyecto

```text
sillage-blog/
├── config/
├── posts/
│   ├── migrations/
│   ├── static/
│   │   └── posts/
│   │       └── css/
│   │           └── styles.css
│   ├── templates/
│   │   └── posts/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── usuarios/
│   ├── migrations/
│   ├── templates/
│   │   └── usuarios/
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── .env.example
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Seguridad

- Las operaciones de creación, edición y eliminación requieren autenticación.
- Los permisos de autor se comprueban en las vistas de Django.
- Los formularios incluyen protección CSRF.
- Las contraseñas se gestionan mediante el sistema de autenticación de Django.
- Las variables privadas se almacenan fuera del código fuente mediante `.env`.

El proyecto está configurado para desarrollo y ejecución local. No incluye una configuración completa para despliegue en producción.

## Autor

**Agustín Molinari**

Proyecto final de Python y Django.