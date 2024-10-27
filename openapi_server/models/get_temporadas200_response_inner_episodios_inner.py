from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class GetTemporadas200ResponseInnerEpisodiosInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, numero_episodio=None, titulo_episodio=None, duracion_episodio=None):  # noqa: E501
        """GetTemporadas200ResponseInnerEpisodiosInner - a model defined in OpenAPI

        :param numero_episodio: The numero_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.  # noqa: E501
        :type numero_episodio: int
        :param titulo_episodio: The titulo_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.  # noqa: E501
        :type titulo_episodio: str
        :param duracion_episodio: The duracion_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.  # noqa: E501
        :type duracion_episodio: int
        """
        self.openapi_types = {
            'numero_episodio': int,
            'titulo_episodio': str,
            'duracion_episodio': int
        }

        self.attribute_map = {
            'numero_episodio': 'numeroEpisodio',
            'titulo_episodio': 'tituloEpisodio',
            'duracion_episodio': 'duracionEpisodio'
        }

        self._numero_episodio = numero_episodio
        self._titulo_episodio = titulo_episodio
        self._duracion_episodio = duracion_episodio

    @classmethod
    def from_dict(cls, dikt) -> 'GetTemporadas200ResponseInnerEpisodiosInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The getTemporadas_200_response_inner_episodios_inner of this GetTemporadas200ResponseInnerEpisodiosInner.  # noqa: E501
        :rtype: GetTemporadas200ResponseInnerEpisodiosInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def numero_episodio(self) -> int:
        """Gets the numero_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.

        Identifica el número del episodio en la temporada a la que se está accediendo  # noqa: E501

        :return: The numero_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.
        :rtype: int
        """
        return self._numero_episodio

    @numero_episodio.setter
    def numero_episodio(self, numero_episodio: int):
        """Sets the numero_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.

        Identifica el número del episodio en la temporada a la que se está accediendo  # noqa: E501

        :param numero_episodio: The numero_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.
        :type numero_episodio: int
        """

        self._numero_episodio = numero_episodio

    @property
    def titulo_episodio(self) -> str:
        """Gets the titulo_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.

        Nombre del episodio  # noqa: E501

        :return: The titulo_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.
        :rtype: str
        """
        return self._titulo_episodio

    @titulo_episodio.setter
    def titulo_episodio(self, titulo_episodio: str):
        """Sets the titulo_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.

        Nombre del episodio  # noqa: E501

        :param titulo_episodio: The titulo_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.
        :type titulo_episodio: str
        """

        self._titulo_episodio = titulo_episodio

    @property
    def duracion_episodio(self) -> int:
        """Gets the duracion_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.

        Intervalo de tiempo en minutos que transcurre entre el comienzo y el fin del episodio  # noqa: E501

        :return: The duracion_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.
        :rtype: int
        """
        return self._duracion_episodio

    @duracion_episodio.setter
    def duracion_episodio(self, duracion_episodio: int):
        """Sets the duracion_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.

        Intervalo de tiempo en minutos que transcurre entre el comienzo y el fin del episodio  # noqa: E501

        :param duracion_episodio: The duracion_episodio of this GetTemporadas200ResponseInnerEpisodiosInner.
        :type duracion_episodio: int
        """

        self._duracion_episodio = duracion_episodio
