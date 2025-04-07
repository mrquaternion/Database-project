CREATE TABLE coupe_du_monde (
    id SERIAL PRIMARY KEY,
    edition VARCHAR(50) NOT NULL,
    pays_hote VARCHAR(50) NOT NULL,
    nombre_equipes INTEGER NOT NULL,
    vainqueur VARCHAR(50)
);

CREATE TABLE equipe (
    id SERIAL PRIMARY KEY,
    nom_pays VARCHAR(50) NOT NULL,
    FOREIGN KEY(coupe_du_monde_id) REFERENCES coupe_du_monde (id)
);

CREATE TABLE joueur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE NOT NULL,
    numero INTEGER NOT NULL,
    position VARCHAR(50) NOT NULL,
    carton_jaune INTEGER NOT NULL DEFAULT 0,
    carton_rouge INTEGER NOT NULL DEFAULT 0,
    equipe_id INTEGER NOT NULL, 
    FOREIGN KEY(equipe_id) REFERENCES equipe (id)
);

CREATE TABLE personnel (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE NOT NULL,
    role VARCHAR(50) NOT NULL,
    equipe_id INTEGER REFERENCES equipe(id)
    FOREIGN KEY(equipe_id) REFERENCES equipe (id)
);

CREATE TABLE stade (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    ville VARCHAR(50) NOT NULL
);

CREATE TABLE partie (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    phase VARCHAR(50) NOT NULL,
    stade_id INTEGER REFERENCES stade(id),
    equipe_recevante_id INTEGER REFERENCES equipe(id),
    equipe_visiteuse_id INTEGER REFERENCES equipe(id),
    score_recevante INTEGER,
    score_visiteuse INTEGER
);

CREATE TABLE arbitre (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    date_naissance DATE NOT NULL,
    nationalite VARCHAR(50) NOT NULL
);

CREATE TABLE arbitre_dans (
    partie_id INTEGER REFERENCES partie(id),
    arbitre_id INTEGER REFERENCES arbitre(id),
    role VARCHAR(20) NOT NULL,
    PRIMARY KEY (partie_id, arbitre_id)
);
