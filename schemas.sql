CREATE TABLE coupe_du_monde (
    id_cdm SERIAL PRIMARY KEY,
    annee INTEGER NOT NULL UNIQUE,
    pays_hote VARCHAR(100) NOT NULL,
    nb_equipes INTEGER NOT NULL,
    vainqueur VARCHAR(100) NOT NULL,
    FOREIGN KEY (vainqueur) REFERENCES equipe(nom_pays)        
);

CREATE TABLE equipe (
    id_equipe SERIAL PRIMARY KEY,
    coupe_id INTEGER NOT NULL,
    nom_pays VARCHAR(100) NOT NULL,
    nb_joueurs INTEGER NOT NULL,
    UNIQUE (coupe_id, nom_pays),
    FOREIGN KEY (coupe_id) REFERENCES coupe_du_monde(id_cdm)
);

CREATE TABLE stade (
    id_stade SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    pays VARCHAR(100) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    UNIQUE (nom, ville)
);

CREATE TABLE partie (
    id_partie SERIAL PRIMARY KEY,
    coupe_id INTEGER NOT NULL,
    date_partie DATE NOT NULL,
    phase VARCHAR(50) NOT NULL,
    stade_id INTEGER NOT NULL,
    equipe_dom_id INTEGER NOT NULL,
    equipe_ext_id INTEGER NOT NULL,
    score_dom INTEGER NOT NULL,
    score_ext INTEGER NOT NULL,
    FOREIGN KEY (coupe_id)      REFERENCES coupe_du_monde(id_cdm),
    FOREIGN KEY (stade_id)      REFERENCES stade(id_stade),
    FOREIGN KEY (equipe_dom_id) REFERENCES equipe(id_equipe),
    FOREIGN KEY (equipe_ext_id) REFERENCES equipe(id_equipe)
);

CREATE TABLE joueur (
    id_joueur SERIAL PRIMARY KEY,
    equipe_id INTEGER NOT NULL,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE NOT NULL,
    annee_deces INTEGER,
    numero INTEGER NOT NULL,
    position VARCHAR(50) NOT NULL,
    cartons_jaunes INTEGER DEFAULT 0,
    cartons_rouges INTEGER DEFAULT 0,
    UNIQUE (equipe_id, numero),
    FOREIGN KEY (equipe_id) REFERENCES equipe(id_equipe)
);

CREATE TABLE personnel (
    id_personnel SERIAL PRIMARY KEY,
    equipe_id INTEGER NOT NULL,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE NOT NULL,
    annee_deces INTEGER,
    role_principal VARCHAR(50) NOT NULL,
    FOREIGN KEY (equipe_id) REFERENCES equipe(id_equipe)
);

CREATE TABLE arbitre (
    id_arbitre SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE NOT NULL,
    annee_deces INTEGER,
    nationalite VARCHAR(50) NOT NULL
);

CREATE TABLE arbitre_dans (
    partie_id INTEGER NOT NULL,
    arbitre_id INTEGER NOT NULL,
    role_arbitre VARCHAR(50) NOT NULL,
    PRIMARY KEY (partie_id, arbitre_id),
    FOREIGN KEY (partie_id)  REFERENCES partie(id_partie),
    FOREIGN KEY (arbitre_id) REFERENCES arbitre(id_arbitre)
);