import unittest

from flask import json

from openapi_server.models.contenido import Contenido  # noqa: E501
from openapi_server.models.get_temporadas200_response_inner import GetTemporadas200ResponseInner  # noqa: E501
from openapi_server.models.get_temporadas200_response_inner_episodios_inner import GetTemporadas200ResponseInnerEpisodiosInner  # noqa: E501
from openapi_server.test import BaseTestCase


class TestContenidoController(BaseTestCase):
    """ContenidoController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_contenido(self):
        """Test case for add_contenido

        Añadir un nuevo contenido a la aplicación
        """
        contenido = {"tipo":"serie","temporadas":[{"episodios":[{"tituloEpisodio":"Celebration","numeroEpisodio":5,"duracionEpisodio":60},{"tituloEpisodio":"Celebration","numeroEpisodio":5,"duracionEpisodio":60}],"numeroTemporada":1},{"episodios":[{"tituloEpisodio":"Celebration","numeroEpisodio":5,"duracionEpisodio":60},{"tituloEpisodio":"Celebration","numeroEpisodio":5,"duracionEpisodio":60}],"numeroTemporada":1}],"idContenido":10,"director":"Mark Mylod","elenco":"Brian Cox, Jeremy Strong, Sarah Snook, Kieran Culkin, Hiam Abbass","genero":"drama","titulo":"Succession","duracion":120,"imagen":["imagen","imagen"],"sinopsis":"Familia de ricos"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/contenido',
            method='POST',
            headers=headers,
            data=json.dumps(contenido),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_episodio(self):
        """Test case for add_episodio

        Añadir un nuevo episodio a una determinada temporada de una serie por su ID
        """
        get_temporadas200_response_inner_episodios_inner = openapi_server.GetTemporadas200ResponseInnerEpisodiosInner()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/contenido/{id_contenido}/{numero_temporada}/ListaEpisodios'.format(id_contenido=56, numero_temporada=56),
            method='POST',
            headers=headers,
            data=json.dumps(get_temporadas200_response_inner_episodios_inner),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_temporada(self):
        """Test case for add_temporada

        Añadir una nueva temporada a una serie por su ID
        """
        get_temporadas200_response_inner = openapi_server.GetTemporadas200ResponseInner()
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/contenido/{id_contenido}/Temporadas'.format(id_contenido=56),
            method='POST',
            headers=headers,
            data=json.dumps(get_temporadas200_response_inner),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_contenido(self):
        """Test case for delete_contenido

        Eliminar un contenido específico por su ID
        """
        headers = { 
        }
        response = self.client.open(
            '/contenido/{id_contenido}'.format(id_contenido=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_contenido(self):
        """Test case for get_all_contenido

        Obtener la lista de contenidos multimedia disponibles
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contenido',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contenido_by_id(self):
        """Test case for get_contenido_by_id

        Obtener un contenido específico por su ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contenido/{id_contenido}'.format(id_contenido=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contenidos_by_genero(self):
        """Test case for get_contenidos_by_genero

        Obtener una lista de contenidos de un genero especifico
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contenido/findByGenero/{genero}'.format(genero=horror),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contenidos_by_tipo(self):
        """Test case for get_contenidos_by_tipo

        Obtener una lista de contenidos de un tipo especifico
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contenido/findByTipo/{tipo}'.format(tipo=serie),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contenidos_by_titulo(self):
        """Test case for get_contenidos_by_titulo

        Obtener una lista de contenidos por su titulo
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contenido/findByTitulo/{titulo}'.format(titulo='titulo_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_episodio(self):
        """Test case for get_episodio

        Obtener un determinado episodio de una determinada temporada de una serie por su ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contenido/{id_contenido}/{numero_temporada}/{numero_episodio}'.format(id_contenido=56, numero_temporada=56, numero_episodio=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_episodios(self):
        """Test case for get_episodios

        Obtener el listado de episodios de una determinada temporada de una serie por su ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contenido/{id_contenido}/{numero_temporada}/ListaEpisodios'.format(id_contenido=56, numero_temporada=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_temporadas(self):
        """Test case for get_temporadas

        Obtener el listado de temporadas de una serie por su ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/contenido/{id_contenido}/Temporadas'.format(id_contenido=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_update_contenido(self):
        """Test case for update_contenido

        Actualizar un contenido específico por su ID
        """
        contenido = {"tipo":"serie","temporadas":[{"episodios":[{"tituloEpisodio":"Celebration","numeroEpisodio":5,"duracionEpisodio":60},{"tituloEpisodio":"Celebration","numeroEpisodio":5,"duracionEpisodio":60}],"numeroTemporada":1},{"episodios":[{"tituloEpisodio":"Celebration","numeroEpisodio":5,"duracionEpisodio":60},{"tituloEpisodio":"Celebration","numeroEpisodio":5,"duracionEpisodio":60}],"numeroTemporada":1}],"idContenido":10,"director":"Mark Mylod","elenco":"Brian Cox, Jeremy Strong, Sarah Snook, Kieran Culkin, Hiam Abbass","genero":"drama","titulo":"Succession","duracion":120,"imagen":["imagen","imagen"],"sinopsis":"Familia de ricos"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/contenido/{id_contenido}'.format(id_contenido=56),
            method='PUT',
            headers=headers,
            data=json.dumps(contenido),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
