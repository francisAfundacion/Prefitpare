# PrefitPare

## Índice

- [Introducción](#introducción)
- [Insignias](#insignias)
- [Acceso al proyecto](#acceso-al-proyecto)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Personas Desarrolladoras](#personas-desarrolladoras)
- [Funcionalidades](#funcionalidades)
- [Estado Del Proyecto](#estado-del-proyecto)

## Introducción

El proyecto en desarrollo **PrefitPare**, pretende crear un servicio API REST. El propósito de este servicio es funcionar de proxy entre el front-end para gestionar operaciones CRUD entre el front-end y la base de datos relacionada con el servicio de un gestor de comidas.

## Insignias

![Version](https://img.shields.io/badge/Version-Python%203.8.10-red?style=plastic&labelColor=black)
![Licence](https://img.shields.io/badge/licence-MIT-purple?style=plastic&labelColor=black)
![Release Date](https://img.shields.io/badge/ReleaseDate-16th%20June%202025-orange?style=plastic&labelColor=grey)
![Django Framework](https://img.shields.io/badge/Framework-Django-blue?style=plastic)

### Django
- ![Swagger](https://img.shields.io/badge/Swagger%20-drf_yasg-orange?style=plastic&labelColor=Grey)
- ![Authentication](https://img.shields.io/badge/Authentication-rest_framework.authtoken-green?style=plastic&labelColor=red)

## Estado Del Proyecto

![Status](https://img.shields.io/badge/Status-En%20Desarrolo-yellow)

## Funcionalidades

1. Gestión **CRUD** sobre las entidades categoria, plato, ingrediente y tipo de persona sin contemplar autenticación.

## Tecnologías Utilizadas

1. Python
2. Django
3. rest_framework
4. drf_yasg
5. Sqlite3
6. rest_framework.authToken
7. VirtualEnv

## Acceso al Proyecto

### Instalaciones necesarias para poder desarrollar con PrefitPare:

1. **Instalar Git**:

    ```bash
    sudo apt install git
    ```

2. **Configurar el nombre de usuario y correo electrónico**:

    ```bash
    git config --global user.name "UsuarioGithub"
    ```
    
   ```bash
   git config --global user.email "correoUsuario@Github.com"
   ```

3. **Crear la clave SSH**:

    ```bash
    ssh-keygen -t rsa -b 4096 -C "correoGithub"
    ```

    Luego, **copiar la clave pública** generada y pegarla en la sección de claves SSH de Github.

### Uso del entorno virtual:

1. **Crear entorno virtual** en la raíz del proyecto:

    ```bash
    python -m venv env
    ```

2. **Activar el entorno virtual**:

    - En **Windows**:
    ```bash
    .\env\Scripts\activate
    ```

    - En **Linux**:
    ```bash
    source env/bin/activate
    ```

3. **Instalar dependencias necesarias**:

    ```bash
    pip install django
    ```
     
   ```bash
   pip install djangorestframework
   ```
   ```bash
   pip install drf_yasg
   ```
      ```bash
   pip install djoser
   ```
   ### Comandos necesarios para trabajar con el proyecto:
 1. Para hacer uso de comandos durante el desarollo, se precisa posicionarse en la ruta dónde se halla el manage.py
    ```bash
     cd PrefitpareRestApi
    ```
2. Crear un **superusuario** para gestionar el administrador de Django:
    ```bash
    python manage.py createsuperuser
    ```
 3. Preparar los cambios contra la base de datos (se crean los archivos de migración):
    ```bash
    python manage.py makemigrations
    ```
4. Aplicar las migraciones (Se debe de hacer la primera vez que se baja el repostiorio)
    ```bash
    python manage.py migrate
    ```
5. Correr el servidor local por defecto de django
    ```bash
    python manage.py runserver
    ```

## Personas Desarrolladoras

### Francisco Gómez Segura
![Francisco Gómez](https://github.com/user-attachments/assets/177d09ae-c773-4833-b830-3cd9fa5db213)

## Licencia

**PrefitPare** utiliza licencia MIT. La documentación de PrefitPare que se guarda en la carpeta `doc` presenta la licencia **Creative Commons**.
