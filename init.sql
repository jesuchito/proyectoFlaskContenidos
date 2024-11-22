-- Creación de la tabla "contenidos"
CREATE TABLE contenidos (
    idContenido SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    tipo VARCHAR(20) NOT NULL CHECK (tipo IN ('serie', 'pelicula', 'corto', 'documental')),
    sinopsis TEXT,
    duracion INT,
    genero VARCHAR(20) CHECK (genero IN ('horror', 'aventura', 'comedia', 'thriller', 'drama', 'romance', 'fantasia', 'ciencia ficcion')),
    director VARCHAR(255),
    elenco TEXT,
    imagen TEXT
);

-- Inserción de datos en la tabla "contenidos"
INSERT INTO contenidos (titulo, tipo, sinopsis, duracion, genero, director, elenco, imagen)
VALUES
('Breaking Bad', 'serie', 'Un profesor de química se convierte en fabricante de metanfetaminas.', 60, 'drama', 'Vince Gilligan', 'Bryan Cranston, Aaron Paul', 'breaking_bad.jpg'),
('Inception', 'pelicula', 'Un ladrón roba secretos en sueños mientras cuestiona la realidad.', 148, 'ciencia ficcion', 'Christopher Nolan', 'Leonardo DiCaprio, Joseph Gordon-Levitt', 'inception.jpg'),
('Apocalypse Now', 'pelicula', 'Un capitán busca a un coronel renegado en la guerra de Vietnam.', 153, 'drama', 'Francis Ford Coppola', 'Martin Sheen, Marlon Brando', 'apocalypse_now.jpg'),
('Maravillas de la Naturaleza', 'documental', 'Un viaje visual por los ecosistemas más increíbles del mundo.', 90, 'aventura', 'David Attenborough', NULL, 'maravillas_naturaleza.jpg'),
('La Luz Eterna', 'corto', 'Un viaje onírico hacia el autodescubrimiento.', 12, 'fantasia', 'Sofia Gutierrez', 'Pedro López, Ana Ruiz', 'luz_eterna.jpg');

-- Creación de la tabla "temporadas"
CREATE TABLE temporadas (
    idTemporada SERIAL PRIMARY KEY,
    idContenido INT,
    numeroTemporada INT NOT NULL,
    CONSTRAINT fk_idContenido FOREIGN KEY (idContenido)
    REFERENCES contenidos(idContenido)
);

-- Creación de la tabla "episodios"
CREATE TABLE episodios (
    idEpisodio SERIAL PRIMARY KEY,
    idTemporada INT,
    numeroEpisodio INT NOT NULL,
    tituloEpisodio VARCHAR(255) NOT NULL,
    duracionEpisodio INT NOT NULL,
    CONSTRAINT fk_idTemporada FOREIGN KEY (idTemporada)
    REFERENCES temporadas(idTemporada)
);
