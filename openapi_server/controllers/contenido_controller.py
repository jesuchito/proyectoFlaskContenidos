import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.contenido import Contenidos  # noqa: E501
from openapi_server.models.get_temporadas200_response_inner import GetTemporadas200ResponseInner  # noqa: E501
from openapi_server.models.get_temporadas200_response_inner_episodios_inner import GetTemporadas200ResponseInnerEpisodiosInner  # noqa: E501
from openapi_server import util

from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request, render_template, make_response

# import psycopg2
# conn = psycopg2.connect(host='localhost',
#                         database='Contenidos',
#                         user='postgres',
#                         password='12345')

db = SQLAlchemy()

def import_db_controller(database):
    global db
    db = database

def add_contenido(contenido):  # noqa: E501
    """Añadir un nuevo contenido a la aplicación

    Crea un nuevo producto multimedia que estará disponible en la aplicación para los usuarios # noqa: E501

    :param contenido: 
    :type contenido: dict | bytes

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """       
    # name = connexion.request.form['name']
    # tipo = connexion.request.form['tipo']
    # sinopsis = connexion.request.form['sinopsis']
    # duracion = connexion.request.form['duracion']
    # print(name, tipo, sinopsis, duracion)
    # try:
    #     cur = conn.cursor()
    #     consulta = "INSERT INTO contenidos (titulo, tipo, sinopsis, duracion) VALUES(%s, %s, %s, %s) RETURNING idContenido"
    #     cur.execute(consulta, [name, tipo, sinopsis, duracion])
    #     conn.commit()
    #     cont_id = cur.fetchone()[0]
    #     cur.close()
    # except psycopg2.DatabaseError as error:
    #     print("Error. No se ha podido insertar el Servidor")
    #     print(error)
    # return ("insertado el id: "+str(cont_id))
    if connexion.request.is_json:
        contenido = Contenidos.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_episodio(id_contenido, numero_temporada, get_temporadas200_response_inner_episodios_inner):  # noqa: E501
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
    if connexion.request.is_json:
        get_temporadas200_response_inner_episodios_inner = GetTemporadas200ResponseInnerEpisodiosInner.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_temporada(id_contenido, get_temporadas200_response_inner):  # noqa: E501
    """Añadir una nueva temporada a una serie por su ID

    Añade una nueva temporada a una serie en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido al que se le añadirá una nueva temporada
    :type id_contenido: int
    :param get_temporadas200_response_inner: 
    :type get_temporadas200_response_inner: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        get_temporadas200_response_inner = GetTemporadas200ResponseInner.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_contenido(id_contenido):  # noqa: E501
    """Eliminar un contenido específico por su ID

    Elimina un contenido multimedia específico de la aplicación en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido a borrar
    :type id_contenido: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_contenido():  # noqa: E501
    """Obtener la lista de contenidos multimedia disponibles

    Retorna el conjunto de los productos multimedia disponibles en la aplicación para el usuario # noqa: E501


    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    
    contenidos = Contenidos.query.all()
    print(contenidos)
    contenidos_dict = [contenido.to_dict() for contenido in contenidos]
    
    response = make_response(render_template('index.html', contenidos=contenidos_dict))
    response.headers['Content-Type'] = 'text/html'
    return response


def get_contenido_by_id(id_contenido):  # noqa: E501
    """Obtener un contenido específico por su ID

    Retorna la información de un contenido multimedia en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido a devolver
    :type id_contenido: int

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """
    contenido = Contenidos.query.get_or_404(id_contenido)
    print(contenido)
    contenido = contenido.to_dict()
    
    response = make_response(render_template("cont_view.html", contenido=contenido, idCont=id_contenido))
    response.headers['Content-Type'] = 'text/html'
    return response


def get_contenidos_by_genero(genero):  # noqa: E501
    """Obtener una lista de contenidos de un genero especifico

    Retorna una lista de contenidos multimedia en función del género proporcionado # noqa: E501

    :param genero: genero de los contenidos por el que se va a filtrar
    :type genero: str

    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    contenidos = Contenidos.query.filter_by(genero=genero).all()
    print(contenidos)
    contenidos_dict = [contenido.to_dict() for contenido in contenidos]
    
    response = make_response(render_template('index.html', contenidos=contenidos_dict))
    response.headers['Content-Type'] = 'text/html'
    return response


def get_contenidos_by_tipo(tipo):  # noqa: E501
    """Obtener una lista de contenidos de un tipo especifico

    Retorna una lista de contenidos multimedia en función del tipo proporcionado # noqa: E501

    :param tipo: tipo de los contenidos por el que se va a filtrar
    :type tipo: str

    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    contenidos = Contenidos.query.filter_by(tipo=tipo).all()
    print(contenidos)
    contenidos_dict = [contenido.to_dict() for contenido in contenidos]
    
    response = make_response(render_template('index.html', contenidos=contenidos_dict))
    response.headers['Content-Type'] = 'text/html'
    return response


def get_contenidos_by_titulo(titulo):  # noqa: E501
    """Obtener una lista de contenidos por su titulo

    Retorna una lista de contenidos multimedia en función del título proporcionado # noqa: E501

    :param titulo: título de los contenidos por el que se va a filtrar
    :type titulo: str

    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    contenidos = Contenidos.query.filter_by(titulo=titulo).all()
    print(contenidos)
    contenidos_dict = [contenido.to_dict() for contenido in contenidos]
    
    response = make_response(render_template('index.html', contenidos=contenidos_dict))
    response.headers['Content-Type'] = 'text/html'
    return response


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
    return 'do some magic!'


def get_episodios(id_contenido, numero_temporada):  # noqa: E501
    """Obtener el listado de episodios de una determinada temporada de una serie por su ID

    Retorna el conjunto de episodios de la temporada especificada por su número de una serie en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido del que se obtendrán sus episodios
    :type id_contenido: int
    :param numero_temporada: número de la temporada de la que se obtendrán sus episodios
    :type numero_temporada: int

    :rtype: Union[List[GetTemporadas200ResponseInnerEpisodiosInner], Tuple[List[GetTemporadas200ResponseInnerEpisodiosInner], int], Tuple[List[GetTemporadas200ResponseInnerEpisodiosInner], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_temporadas(id_contenido):  # noqa: E501
    """Obtener el listado de temporadas de una serie por su ID

    Retorna el conjunto de temporadas de una serie en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido del que se obtendrán sus temporadas
    :type id_contenido: int

    :rtype: Union[List[GetTemporadas200ResponseInner], Tuple[List[GetTemporadas200ResponseInner], int], Tuple[List[GetTemporadas200ResponseInner], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_contenido(id_contenido, contenido):  # noqa: E501
    """Actualizar un contenido específico por su ID

    Actualiza la información de un contenido multimedia en función del identificador proporcionado # noqa: E501

    :param id_contenido: ID del contenido a actualizar
    :type id_contenido: int
    :param contenido: 
    :type contenido: dict | bytes

    :rtype: Union[Contenido, Tuple[Contenido, int], Tuple[Contenido, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        contenido = Contenidos.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
