import connexion

from openapi_server.models.contenido import Contenidos
from openapi_server.models.episodios import Episodios
from openapi_server.models.temporadas import Temporadas

from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, render_template, make_response

db = SQLAlchemy()

def import_db_controller(database):
    global db
    db = database


def add_contenido():  # noqa: E501
    """Añadir un nuevo contenido a la aplicación

    Crea un nuevo producto multimedia que estará disponible en la aplicación para los usuarios # noqa: E501

    :param contenido: 
    :type contenido: dict | bytes

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """       
    try:
    # Obtener los datos de la solicitud JSON
        data = connexion.request.get_json()
        if not data:
            return {"error": "No data provided"}, 400  # Código 400: No se proporcionaron datos
    
    # Verificar que todos los campos requeridos están presentes
        required_fields = ['titulo', 'tipo', 'sinopsis', 'duracion', 'genero', 'director', 'elenco', 'imagen']
        for field in required_fields:
            if field not in data:
                return {"error": f"Missing field: {field}"}, 422  # Código 422: Falta un campo requerido

    # Validar los valores de 'tipo' y 'genero' (comprobamos si son válidos)
        valid_types = ['serie', 'pelicula', 'corto', 'documental']
        if data['tipo'] not in valid_types:
            return {"error": "Invalid tipo. Valid types are: serie, pelicula, corto, documental"}, 422  # Código 422: Tipo no válido

        valid_genres = ['horror', 'aventura', 'comedia', 'thriller', 'drama', 'romance', 'fantasia', 'ciencia ficcion']
        if data['genero'] not in valid_genres:
            return {"error": "Invalid genero. Valid genres are: horror, aventura, comedia, thriller, drama, romance, fantasia, ciencia ficcion"}, 422  # Código 422: Género no válido

        # Asignar los valores de los campos
        titulo = data['titulo']
        tipo = data['tipo']
        sinopsis = data['sinopsis']
        duracion = data['duracion']
        genero = data['genero']
        director = data['director']
        elenco = data['elenco']
        imagen = data['imagen']

        # Crear el nuevo contenido
        new_contenido = Contenidos(
            titulo=titulo, 
            tipo=tipo, 
            sinopsis=sinopsis, 
            duracion=duracion, 
            genero=genero, 
            director=director, 
            elenco=elenco,
            imagen= imagen,
            )

    # Guardar el contenido en la base de datos
        db.session.add(new_contenido)
        db.session.commit()

    # Retornar el contenido creado como diccionario
        return new_contenido.to_dict(), 200  # Código 200: Contenido creado exitosamente

    except Exception as e:
    # En caso de error, retornar un mensaje con detalles
        return {"error": f"An error occurred: {str(e)}"}, 500  # Código 500: Error del servidor


def add_episodio(id_contenido, numero_temporada):  # noqa: E501
    """Añadir un nuevo episodio a una determinada temporada de una serie por su ID

    Añade un nuevo episodio a la temporada especificada por su número de una serie en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido al que se le añadirá un nuevo episodio
    :type id_contenido: int
    :param numero_temporada: número de la temporada a la que se le añadirá un nuevo episodio
    :type numero_temporada: int
    :param get_temporadas200_response_inner_episodios_inner: 
    :type get_temporadas200_response_inner_episodios_inner: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:
        # Validar si la solicitud contiene datos JSON válidos
        if not connexion.request.is_json:
            return jsonify({"error": "Los datos enviados no están en formato JSON válido."}), 400

        # Obtener los datos del episodio desde la solicitud JSON
        data = connexion.request.get_json()

        # Validar si la temporada existe y está relacionada con el contenido
        temporada =  db.session.query(Temporadas).filter_by(idcontenido=id_contenido, numerotemporada=numero_temporada).first()
        if not temporada:
            return jsonify({"error": "La temporada especificada no existe o no está relacionada con el contenido."}), 404

        # Validar que los campos obligatorios estén presentes
        campos_requeridos = ['numero', 'titulo', 'duracion']
        for campo in campos_requeridos:
            if campo not in data:
                return jsonify({'error': f'Falta el campo {campo} en la solicitud'}), 400

        # Extraer datos del JSON
        numero = data['numero']
        titulo = data['titulo']
        duracion = data['duracion']

        # Verificar si ya existe un episodio con el mismo número en esta temporada
        if db.session.query(Episodios).filter_by(numeroepisodio=numero, idtemporada=temporada.idtemporada).first():
            return jsonify({"error": "Ya existe un episodio con este número para esta temporada."}), 400

        # Crear el nuevo episodio
        new_episodio = Episodios(
            idtemporada=temporada.idtemporada,
            numeroepisodio=numero,
            tituloepisodio=titulo,
            duracionepisodio=duracion
        )

        # Agregar y guardar en la base de datos
        db.session.add(new_episodio)
        db.session.commit()

        # Devolver la respuesta en formato JSON
        return jsonify(new_episodio.to_dict()), 201
    except KeyError as e:
        # Manejar errores si faltan campos en la solicitud JSON
        return jsonify({'error': f'Falta el campo {e} en la solicitud'}), 400
    except Exception as e:
        # Manejar otros errores
        return jsonify({'error': str(e)}), 500
    

def add_temporada(id_contenido):  # noqa: E501
    """Añadir una nueva temporada a una serie por su ID

    Añade una nueva temporada a una serie en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido al que se le añadirá una nueva temporada
    :type id_contenido: int
    :param get_temporadas200_response_inner: 
    :type get_temporadas200_response_inner: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    # Obtener el número de temporada desde el JSON de la solicitud
    temporada = connexion.request.json.get('Temporada')
   
    # Validar que el contenido existe
    contenido = db.session.query(Contenidos).get(id_contenido)
    
    # Verificar que el contenido es una serie
    if contenido.tipo != 'serie':
        return jsonify({"error": "El contenido no es una serie."}), 400

    # Validar que el número de temporada esté presente y sea un entero
    if not temporada or not isinstance(temporada, int):
        return jsonify({"error": "El campo 'Temporada' es obligatorio y debe ser un número entero válido."}), 400

    # Verificar si ya existe una temporada con el mismo número para este contenido
    if db.session.query(Temporadas).filter_by(idcontenido=id_contenido, numerotemporada=temporada).first():
        return jsonify({"error": "Ya existe esta temporada con este número para este contenido."}), 400

    try:
        # Crear la nueva temporada
        new_temporada = Temporadas(idcontenido=id_contenido, numerotemporada=temporada)
        
        # Agregar la temporada a la base de datos
        db.session.add(new_temporada)
        db.session.commit()

        # Respuesta exitosa
        return jsonify({"message": "Temporada añadida exitosamente"}), 201
    
    except Exception as e:
        # Manejo de errores, asegurando que si algo falla se revierte la transacción
        db.session.rollback()
        return jsonify({"error": f"Error al crear la temporada: {str(e)}"}), 500



def delete_contenido(id_contenido):  # noqa: E501
    """Eliminar un contenido específico por su ID

    Elimina un contenido multimedia específico de la aplicación en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido a borrar
    :type id_contenido: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:
        # Asegurarse de que el ID proporcionado es un número entero
        id_contenido = int(id_contenido)
        
        # Buscar el contenido en la base de datos
        contenido = db.session.query(Contenidos).get(id_contenido)
        
        if contenido is None:
            # Si el contenido no se encuentra, devolver un error 404
            return jsonify({'error': 'Contenido no encontrado'}), 404

        # Eliminar el contenido de la sesión actual si estaba en otra sesión
        db.session.expunge(contenido)
        
        # Eliminar el contenido de la base de datos
        db.session.delete(contenido)
        db.session.commit()

        # Confirmar que el contenido fue eliminado correctamente
        return jsonify({'message': 'contenido eliminado correctamente'}), 200


    except ValueError:
        # Devolver un error 400 si el ID proporcionado no es un número entero
        return jsonify({'error': 'ID inválido, debe ser un número entero'}), 400

    except Exception as e:
        # Capturar cualquier otro error y devolver un error 500 con detalles adicionales
        return jsonify({'error': f'Error en el servidor: {str(e)}'}), 500


def get_all_contenido():  # noqa: E501
    """Obtener la lista de contenidos multimedia disponibles

    Retorna el conjunto de los productos multimedia disponibles en la aplicación para el usuario # noqa: E501


    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    
    contenidos = db.session.query(Contenidos)
    print(contenidos)
    contenidos_dict = [contenido.to_dict() for contenido in contenidos]

    return contenidos_dict


def get_contenido_by_id(id_contenido):  # noqa: E501
    """Obtener un contenido específico por su ID

    Retorna la información de un contenido multimedia en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido a devolver
    :type id_contenido: int

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """
    contenido = db.session.query(Contenidos).get(id_contenido)
    print(contenido)
    contenido = contenido.to_dict()

    return contenido


def get_contenidos_by_genero(genero):  # noqa: E501
    """Obtener una lista de contenidos de un genero especifico

    Retorna una lista de contenidos multimedia en función del género proporcionado # noqa: E501

    :param genero: genero de los contenidos por el que se va a filtrar
    :type genero: str

    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    contenidos = db.session.query(Contenidos).filter_by(genero=genero).all()
    print(contenidos)
    contenidos_dict = [contenido.to_dict() for contenido in contenidos]

    return contenidos_dict


def get_contenidos_by_tipo(tipo):  # noqa: E501
    """Obtener una lista de contenidos de un tipo especifico

    Retorna una lista de contenidos multimedia en función del tipo proporcionado # noqa: E501

    :param tipo: tipo de los contenidos por el que se va a filtrar
    :type tipo: str

    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    contenidos =  db.session.query(Contenidos).filter_by(tipo=tipo).all()
    
    print(contenidos)
    contenidos_dict = [contenido.to_dict() for contenido in contenidos]

    return contenidos_dict


def get_contenidos_by_titulo(titulo):  # noqa: E501
    """Obtener una lista de contenidos por su titulo

    Retorna una lista de contenidos multimedia en función del título proporcionado # noqa: E501

    :param titulo: título de los contenidos por el que se va a filtrar
    :type titulo: str

    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    contenidos = db.session.query(Contenidos).filter_by(titulo=titulo).all()
    print(contenidos)
    contenidos_dict = [contenido.to_dict() for contenido in contenidos]
    
    return contenidos_dict


def get_episodio(id_contenido, numero_temporada, numero_episodio):  # noqa: E501
    """Obtener un determinado episodio de una determinada temporada de una serie por su ID

    Obtiene un episodio especificado por su número de la temporada especificada a su vez por su propio número de una serie en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido del que se obtendrá el episodio
    :type id_contenido: int
    :param numero_temporada: número de la temporada de la que se obtendrá el episodio
    :type numero_temporada: int
    :param numero_episodio: número del episodio que se obtendrá
    :type numero_episodio: int

    :rtype: Union[GetTemporadas200ResponseInnerEpisodiosInner, Tuple[GetTemporadas200ResponseInnerEpisodiosInner, int], Tuple[GetTemporadas200ResponseInnerEpisodiosInner, int, Dict[str, str]]
    """
    temporada =  db.session.query(Temporadas).filter_by(numerotemporada=numero_temporada, idcontenido=id_contenido).first()
    
    episodio = db.session.query(Episodios).filter_by(numeroepisodio=numero_episodio, idtemporada=temporada.idtemporada).first()
    

    return episodio.to_dict()


def get_episodios(id_contenido, numero_temporada):  # noqa: E501
    """Obtener el listado de episodios de una determinada temporada de una serie por su ID

    Retorna el conjunto de episodios de la temporada especificada por su número de una serie en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido del que se obtendrán sus episodios
    :type id_contenido: int
    :param numero_temporada: número de la temporada de la que se obtendrán sus episodios
    :type numero_temporada: int

    :rtype: Union[List[GetTemporadas200ResponseInnerEpisodiosInner], Tuple[List[GetTemporadas200ResponseInnerEpisodiosInner], int], Tuple[List[GetTemporadas200ResponseInnerEpisodiosInner], int, Dict[str, str]]
    """
    temporada = db.session.query(Temporadas).filter_by(numerotemporada=numero_temporada, idcontenido=id_contenido).first()

    episodios = db.session.query(Episodios).filter_by(idtemporada = temporada.idtemporada).all()
    
    episodios_dict = [episodio.to_dict() for episodio in episodios]
    
    return episodios_dict

def get_temporadas(id_contenido):  # noqa: E501
    """Obtener el listado de temporadas de una serie por su ID

    Retorna el conjunto de temporadas de una serie en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido del que se obtendrán sus temporadas
    :type id_contenido: int

    :rtype: Union[List[GetTemporadas200ResponseInner], Tuple[List[GetTemporadas200ResponseInner], int], Tuple[List[GetTemporadas200ResponseInner], int, Dict[str, str]]
    """
    temporadas = db.session.query(Temporadas).filter_by(idcontenido=id_contenido).all()
    
    temporadas_dict = [temporada.to_dict() for temporada in temporadas]
    
    return temporadas_dict


def update_contenido(id_contenido):  # noqa: E501
    """Actualizar un contenido específico por su ID

    Actualiza la información de un contenido multimedia en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido a actualizar
    :type id_contenido: int
    :param contenido: 
    :type contenido: dict | bytes

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """
    try:
        
        # Obtener los datos de la solicitud JSON
        data = connexion.request.get_json()
        if not data:
            return {"error": "No data provided"}, 400  # Código 400: No se proporcionaron datos
        
        # Buscar el contenido por ID
        cont = db.session.query(Contenidos).get(id_contenido)

        # Actualizar solo los campos que fueron enviados en el cuerpo de la solicitud
        if 'titulo' in data:
            cont.titulo = data['titulo']
        if 'tipo' in data:
            cont.tipo = data['tipo']
        if 'sinopsis' in data:
            cont.sinopsis = data['sinopsis']
        if 'duracion' in data:
            cont.duracion = data['duracion']
        if 'genero' in data:
            cont.genero = data['genero']  # Actualización solo si 'genero' está presente en los datos
        if 'director' in data:
            cont.director = data['director']
        if 'elenco' in data:
            cont.elenco = data['elenco']
        if 'imagen' in data:
            cont.imagen = data['imagen']

        # Guardar los cambios en la base de datos
        # Eliminar el contenido de la sesión actual si estaba en otra sesión
        db.session.expunge(cont)
        
        # Eliminar el contenido de la base de datos
        db.session.add(cont)
        db.session.commit()
        # Retornar el contenido actualizado como diccionario
        return cont.to_dict(), 200  # Código 200: Contenido actualizado exitosamente

    except Exception as e:
        # Otro tipo de error
        return {"error": f"An error occurred: {str(e)}"}, 500  # Código 500: Error del servidor
