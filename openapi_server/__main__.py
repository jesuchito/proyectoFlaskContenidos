#!/usr/bin/env python3

import connexion
from openapi_server import encoder
from flask_sqlalchemy import SQLAlchemy
from openapi_server.controllers.contenido_controller import import_db_controller
from openapi_server.models.contenido import import_db_model

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': 'Microservicio de Contenidos de una aplicación de tipo Netflix'},
            pythonic_params=True)

app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/Contenidos'
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app.app)

import_db_controller(db)
import_db_model(db)

app.run(port=8080)