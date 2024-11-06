from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def import_db_temp(database):
    global db
    db = database

class Temporadas(db.Model):
    tablename = 'temporadas'
    
    idtemporada = db.Column(db.Integer, primary_key=True)
    idcontenido = db.Column(db.Integer, db.ForeignKey('contenidos.idcontenido'), nullable=False)
    numerotemporada = db.Column(db.Integer, nullable=False)
    
    def repr(self):
        return f'<Temporada: {self.numerotemporada}>'
        
    def to_dict(self):
        return {
            "id_temporada": self.idtemporada,
            "id_contenido": self.idcontenido,
            "numero": self.numerotemporada
        }