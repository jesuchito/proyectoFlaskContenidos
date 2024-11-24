# Api Contenidos 

<img width="668" alt="image" src="https://github.com/user-attachments/assets/d68f6a52-cda4-4a7c-b3e1-677decdb2fa7">

## Descripción General

La API de contenidos es una interfaz que permite la gestión y acceso a los contenidos multimedia disponibles en la plataforma de tipo Netflix. A través de esta API, los usuarios pueden interactuar con una amplia variedad de contenido, incluyendo películas, series, documentales y otros formatos, permitiéndoles consumir estos elementos dentro de la aplicación.

El objetivo principal de esta API es garantizar una entrega eficiente y escalable de contenido a los usuarios, mientras mantiene la flexibilidad necesaria para adaptarse a nuevas funcionalidades o cambios en los requerimientos de negocio.

##  Endpoints de la API


- **Obtener lista de contenidos**  
  `GET /contenido`: Recupera todos los contenidos multimedia.

- **Añadir nuevo contenido**  
  `POST /contenido`: Crea un nuevo contenido multimedia.

- **Buscar por género**  
  `GET /contenido/findByGenero/{genero}`: Filtra contenidos por género.

- **Buscar por tipo**  
  `GET /contenido/findByTipo/{tipo}`: Filtra contenidos por tipo (serie, película, etc.).

- **Buscar por título**  
  `GET /contenido/findByTitulo/{titulo}`: Busca contenidos por título.

- **Obtener contenido por ID**  
  `GET /contenido/{idContenido}`: Obtiene un contenido específico por ID.

- **Actualizar contenido**  
  `PUT /contenido/{idContenido}`: Actualiza un contenido por ID.

- **Eliminar contenido**  
  `DELETE /contenido/{idContenido}`: Elimina un contenido por ID.

- **Obtener temporadas de una serie**  
  `GET /contenido/{idContenido}/Temporadas`: Lista las temporadas de una serie.

- **Añadir temporada a una serie**  
  `POST /contenido/{idContenido}/Temporadas`: Añade una temporada a una serie.

- **Obtener episodios de una temporada**  
  `GET /contenido/{idContenido}/{numeroTemporada}/ListaEpisodios`: Lista los episodios de una temporada.

## Tecnologías y Herramientas Usadas:

- Se utilizó **PostgreSQL** como base de datos SQL para almacenar y gestionar los datos de la API.

- **Postman** se utilizó para realizar pruebas de los endpoints de la API, asegurando que todas las solicitudes y respuestas fueran correctas.

- **GitHub Actions** se configuró para automatizar el proceso de integración continua, ejecutando pruebas y despliegues cada vez que se realizaba un push al repositorio.

- **Swagger** se usó para definir la arquitectura de la API, incluyendo los endpoints del microservicio. Esto proporcionó una documentación interactiva y permitió probar la API directamente desde la interfaz.

- **OpenAPI Generator** se empleó para generar el esqueleto del código de la API, lo que permitió comenzar rápidamente con una estructura base para los endpoints definidos en el archivo Swagger.

- El desarrollo se realizó en **Python**, utilizando el framework **Flask** para construir la API. Flask es ligero, fácil de usar y perfecto para construir microservicios.

- **Docker** se utilizó para crear contenedores tanto para la API como para la base de datos, permitiendo simular un entorno de despliegue real. Esto garantizó que la API funcionara correctamente tanto en desarrollo como en pruebas, aislando el entorno de ejecución.

- Se utilizó una **arquitectura modular**, separando el código en diferentes paquetes y clases. Esto permitió un orden claro y mantenible en el código. La separación en paquetes facilita el desarrollo y la extensión del sistema sin que otras partes se vean afectadas, favoreciendo la escalabilidad del proyecto.

- Se utilizaron las siguientes librerías:

    Flask-SQLAlchem: Para la integración con la base de datos PostgreSQL, gestionando las operaciones CRUD.

    Flask-CORS: Para habilitar el soporte de CORS, permitiendo que la API sea accesible desde diferentes dominios.


## Requisitos de la API
Python 3.5.2+

## Guía de Uso En el Directorio

### Despliegue en Directorio 

1. Instalación:
 * Asegúrate de tener Python 3.5.2 o superior instalado en tu máquina.

2. Configuración del entorno
 * Asegúrate de tener PostgreSQL corriendo y configurado en tu entorno local o usa un servicio en la nube .
 * Nombra tu base de datos como Contenidos 
 * Para inicializar las tablas la base de datos y el contenido de esta, asegúrate de ejecutar las query definidas en el archivo Init.sql para crear las tablas y estructuras necesaria

3. Para ejecutar la Api Contenidos , ejecute lo siguiente desde el directorio raíz
 * Instale los requerimientos 
    ```
    pip3 install -r requirements.txt
    pip3 install -r requeriments_sqlalchemy.txt
    ```
 * Ejecute la Api con el siguiente Comando
    ```
    python3 -m openapi_server
    ```
 * La Api debe estarse  ejecutando 

4. Definición de OpenAPI

Abre tu navegador y accede a la siguiente URL para ver la interfaz de usuario de la API:
```
http://localhost:8080/ui/
```

La definición de OpenAPI está disponible en formato JSON en:
```
http://localhost:8080/openapi.json
```


## Despliegue en Docker 

Este documento describe los pasos necesarios para desplegar una API dentro de un contenedor Docker utilizando `docker-compose`.

---

### Requisitos previos

1. **Docker**: Asegúrate de tener instalado Docker en tu sistema. Puedes descargarlo desde [Docker](https://www.docker.com/).
2. **docker-compose**: Comprueba que tienes instalado `docker-compose`. Si no, sigue las instrucciones de instalación [aquí](https://docs.docker.com/compose/install/).

---

### Pasos para el despliegue

### Paso 1: Crear una red en Docker

Antes de desplegar la API, necesitas crear una red específica para el proyecto. Esto permitirá que los contenedores se comuniquen entre sí.

Ejecuta el siguiente comando en la terminal:

```bash
docker network create flask_network
```

### Paso 2: Construir e iniciar la API

Para construir la imagen de Docker y poner en marcha los contenedores, sigue los pasos a continuación:

Desde el directorio donde se encuentra el archivo `docker-compose.yml`, ejecuta el siguiente comando para construir las imágenes y levantar los contenedores:

```bash
docker-compose up --build
```

### Paso 3. Verificar el despliegue
Una vez que los contenedores estén en funcionamiento, puedes verificar el estado de los servicios con el siguiente comando:

```bash
docker ps
```

## ¡Todo listo! 🚀

Tu API ahora está en funcionamiento dentro de un contenedor Docker, junto con su base de datos y otros servicios asociados.
