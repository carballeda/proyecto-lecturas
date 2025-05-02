# Lecturas Django

Este proyecto es una aplicación web desarrollada con Django para gestionar una base de datos personal de libros leídos.

## Características

- Registro de libros leídos con información de: título, autor, ISBN, número de páginas, año de publicación, formato (ebook, tapa blanda, tapa dura o audiolibro), fecha de inicio de lectura, fecha de fin de lectura, calificación (de una a cinco estrellas), espacio para escribir notas sobre la lectura y citas, género del libro, el estado (leído, quiero leer y abandonado), y etiquetas personalizables.
Todos los campos son opcionales excepto título y autor.
- Interfaz de administración con filtros y búsqueda.
- Carga inicial de datos desde un archivo CSV exportado de otra aplicación de gestión de lecturas.
- Página pública (opcional) con listado de libros.

## Requisitos

- Python 3.x
- Django 5.x
- Entorno virtual (recomendado)

## Instalación

1. Clona el repositorio o descarga los archivos.
2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # En macOS/Linux: source venv/bin/activate
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4. Aplica las migraciones:
    ```bash
    python manage.py migrate
    ```
5. Crea un superusuario para acceder al admin:
    ```bash
    python manage.py createsuperuser
    ```
6. Ejecuta el servidor:
    ```bash
    python manage.py runserver
    ```

## Uso

Accede a `http://127.0.0.1:8000/admin/` para gestionar tu base de datos de lecturas.

## Estructura

- `libros/`: Contiene el modelo `Libro` y la configuración de la app.
- `templates/`: Plantillas HTML para la vista pública opcional.
- `management/commands/importar_lecturas.py`: Script para importar libros desde un archivo CSV.

## Licencia

Este proyecto es de uso personal y no tiene una licencia específica.
