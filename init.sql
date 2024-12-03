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
('After Life', 'serie', 'Un hombre lucha por encontrar un propósito tras la muerte de su esposa.', 30, 'comedia', 'Ricky Gervais', 'Ricky Gervais, Kerry Godliman', 'after_life.jpg'),
('Apocalypse Now', 'pelicula', 'Un capitán busca a un coronel renegado en la guerra de Vietnam.', 153, 'drama', 'Francis Ford Coppola', 'Martin Sheen, Marlon Brando', 'apocalypse_now.jpg'),
('Breaking Bad', 'serie', 'Un profesor de química se convierte en fabricante de metanfetaminas.', 60, 'drama', 'Vince Gilligan', 'Bryan Cranston, Aaron Paul', 'breaking_bad.jpg'),
('La Casa de Papel', 'serie', 'Un grupo de delincuentes realiza un atraco a la Fábrica Nacional de Moneda y Timbre.', 50, 'aventura', 'Álex Pina', 'Úrsula Corberó, Álvaro Morte', 'casa_papel.jpg'),
('Destino Final', 'pelicula', 'Un grupo de jóvenes trata de burlar a la muerte tras predecir un accidente mortal.', 98, 'horror', 'James Wong', 'Devon Sawa, Ali Larter', 'destino_final.jpg'),
('Django Desencadenado', 'pelicula', 'Un esclavo liberado se une a un cazarrecompensas para rescatar a su esposa.', 165, 'aventura', 'Quentin Tarantino', 'Jamie Foxx, Christoph Waltz', 'django_desencadenado.jpg'),
('El Camino', 'pelicula', 'Jesse Pinkman busca libertad tras los eventos de Breaking Bad.', 122, 'drama', 'Vince Gilligan', 'Aaron Paul, Jesse Plemons', 'el_camino.jpg'),
('Friends', 'serie', 'Seis amigos navegan por la vida y el amor en Nueva York.', 22, 'comedia', 'David Crane, Marta Kauffman', 'Jennifer Aniston, Courteney Cox', 'friends.jpg'),
('Historia del Cosmos', 'documental', 'Un recorrido por el universo y sus misterios.', 60, 'aventura', 'Carl Sagan', NULL, 'historia_cosmos.jpg'),
('Inception', 'pelicula', 'Un ladrón roba secretos en sueños mientras cuestiona la realidad.', 148, 'ciencia ficcion', 'Christopher Nolan', 'Leonardo DiCaprio, Joseph Gordon-Levitt', 'inception.jpg'),
('Los Soprano', 'serie', 'La vida de un mafioso italoamericano mientras lidia con problemas familiares y criminales.', 55, 'drama', 'David Chase', 'James Gandolfini, Lorraine Bracco', 'los_soprano.jpg'),
('La Luz Eterna', 'corto', 'Un viaje onírico hacia el autodescubrimiento.', 12, 'fantasia', 'Sofia Gutierrez', 'Pedro López, Ana Ruiz', 'luz_eterna.jpg'),
('Maravillas de la Naturaleza', 'documental', 'Un viaje visual por los ecosistemas más increíbles del mundo.', 90, 'aventura', 'David Attenborough', NULL, 'maravillas_naturaleza.jpg'),
('Mind Hunter', 'serie', 'Agentes del FBI estudian la psicología de los asesinos en serie.', 60, 'thriller', 'Joe Penhall', 'Jonathan Groff, Holt McCallany', 'mind_hunter.jpg'),
('Prison Break', 'serie', 'Un hombre elabora un plan para liberar a su hermano de la cárcel.', 44, 'aventura', 'Paul Scheuring', 'Wentworth Miller, Dominic Purcell', 'prison_break.jpg'),
('Secretos del Pasado', 'pelicula', 'Un hombre descubre verdades ocultas sobre su familia.', 95, 'drama', 'Alberto Torres', 'Carlos Rivera, Ana Serradilla', 'secretos_pasado.jpg'),
('Squid Game', 'serie', 'Personas endeudadas participan en juegos mortales para ganar dinero.', 60, 'thriller', 'Hwang Dong-hyuk', 'Lee Jung-jae, Park Hae-soo', 'squid_games.jpg'),
('Terrifier', 'pelicula', 'Un payaso maniático aterroriza a dos jóvenes en Halloween.', 82, 'horror', 'Damien Leone', 'Jenna Kanell, David Howard Thornton', 'terrifier.jpg'),
('The Bear', 'serie', 'Un joven chef regresa a Chicago para dirigir el restaurante familiar.', 30, 'drama', 'Christopher Storer', 'Jeremy Allen White, Ebon Moss-Bachrach', 'the_bear.jpg'),
('The Office', 'serie', 'La vida diaria de los empleados de una oficina de Scranton.', 22, 'comedia', 'Greg Daniels', 'Steve Carell, Rainn Wilson', 'the_office.jpg'),
('Tierra de Noche', 'documental', 'Explora el mundo natural bajo la luz de la luna.', 60, 'aventura', 'Emma Napper', NULL, 'tierra_noche.jpg'),
('True Detective', 'serie', 'Detectives enfrentan casos complejos mientras lidian con sus propios demonios.', 55, 'thriller', 'Nic Pizzolatto', 'Matthew McConaughey, Woody Harrelson', 'true_detective.jpg');

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
