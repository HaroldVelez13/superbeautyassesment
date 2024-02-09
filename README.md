# Proyecto para Equipos

Aplicativo Django con docker, cuenta con los modelos Equipo y EquipoUsuario en la app inventario.

1. Se implemento Materialcss para el Administrador de Django.
2. Se implemento bootstrap para la view de equipos.
3. Se implemento paginacion para optimizar los tiempos de carga (Por ejemplo se dejo la paginacion en 1).
4. Se implementarion test Para EquipoModel y equipo_list view.
5. La aplicacion Dockerizo.

## Intalación con docker

```bash
docker compose up
```

## Intalación con Python

Instalar dependencias

```bash
pip install --no-cache-dir -r requirements.txt
```

Crear Migraciones

```bash
python manage.py makemigrations
```

Migrar

```bash
python manage.py migrate
```

Ejecutar test

```bash
python manage.py test
```

Levantar servidor

```bash
python manage.py runserver 0.0.0.0:8000
```
