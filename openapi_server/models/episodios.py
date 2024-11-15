from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def import_db_ep(database):
    global db
    db = database
    
class Episodios(db.Model):
    tablename = 'episodios'
    
    idepisodio = db.Column(db.Integer, primary_key=True)
    idtemporada = db.Column(db.Integer, nullable=False)
    numeroepisodio = db.Column(db.Integer, nullable=False)
    tituloepisodio = db.Column(db.String(255), nullable=False)
    duracionepisodio = db.Column(db.Integer, nullable=False)
    
    def repr(self):
        return f'<Episodio: {self.tituloepisodio}>'
    
    def to_dict(self):
        return {
            "id_episodio": self.idepisodio,
            "temporada": self.idtemporada,
            "numero": self.numeroepisodio,
            "titulo": self.tituloepisodio,
            "duracion": self.duracionepisodio
        }