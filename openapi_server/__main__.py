#!/usr/bin/env python3

import connexion
from openapi_server import encoder
from flask_sqlalchemy import SQLAlchemy
from openapi_server.controllers.contenido_controller import import_db_controller
from openapi_server.models.contenido import import_db_cont
from openapi_server.models.episodios import import_db_ep
from openapi_server.models.temporadas import import_db_temp

from flask_cors import CORS

app = connexion.App(__name__, specification_dir='./openapi/')
CORS(app.app)
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Microservicio de Contenidos de una aplicación de tipo Netflix'},
            pythonic_params=True)

app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/Contenidos'
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app.app)

import_db_controller(db)
import_db_cont(db)
import_db_ep(db)
import_db_temp(db)

app.run(port=8080)