# Dental Appointments

Este proyecto es una aplicación web para el registro de citas médicas, especialmente diseñada para odontólogos. Permite a los pacientes programar, ver y gestionar sus citas, así como a los odontólogos administrar su agenda.

## Estructura del Proyecto

```
dental-appointments
├── app
│   ├── manage.py                # Punto de entrada de la aplicación Django
│   ├── config                   # Configuración del proyecto
│   ├── appointments              # Aplicación para gestionar citas médicas
│   ├── users                    # Aplicación para gestionar usuarios
│   ├── templates                # Plantillas HTML
│   └── static                   # Archivos estáticos (CSS, JS)
├── tests                        # Pruebas del proyecto
├── .gitignore                   # Archivos y directorios a ignorar por Git
├── pyproject.toml              # Configuración del proyecto para Poetry
├── poetry.lock                  # Bloqueo de versiones de dependencias
└── render.yaml                  # Configuración para despliegue en Render
```

## Requisitos

- Python 3.8 o superior
- Django 3.2 o superior
- Poetry para la gestión de dependencias

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd dental-appointments
   ```

2. Instala las dependencias:
   ```
   poetry install
   ```

3. Configura la base de datos en `app/config/settings.py`.

4. Realiza las migraciones:
   ```
   poetry run python manage.py migrate
   ```

5. Crea un superusuario para acceder al panel de administración:
   ```
   poetry run python manage.py createsuperuser
   ```

6. Inicia el servidor de desarrollo:
   ```
   poetry run python manage.py runserver
   ```

## Uso

- Accede a la aplicación en `http://127.0.0.1:8000/`.
- Utiliza el panel de administración en `http://127.0.0.1:8000/admin/` para gestionar usuarios y citas.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir cambios.

## Licencia

Este proyecto está bajo la Licencia MIT.