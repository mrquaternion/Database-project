
# les équipes avec le plus grand nombres de cartons rouges dans l'histoire du coupe du monde entre 1986-2022
Query_1 = """SELECT equipe.nom_pays, COUNT(joueur.id_joueur) AS nombre_cartons_rouges
FROM joueur
JOIN equipe ON joueur.equipe_id = equipe.id_equipe
WHERE joueur.cartons_rouges >= 1
GROUP BY equipe.nom_pays
ORDER BY nombre_cartons_rouges DESC;"""

# Les arbitres qui ont arbitré le plus de parties
Query_2 = """SELECT arbitre.nom, arbitre.prenom, COUNT(arbitre_dans.partie_id) AS nombre_parties
FROM arbitre
JOIN arbitre_dans ON arbitre.id_arbitre = arbitre_dans.arbitre_id
GROUP BY arbitre.nom, arbitre.prenom
ORDER BY nombre_parties DESC;"""

# Les stades qui ont accueilli plus de 5 parties
Query_3 = """SELECT stade.nom, stade.ville, COUNT(partie.id_partie) AS nombre_parties
FROM stade
JOIN partie ON stade.id_stade = partie.stade_id
GROUP BY stade.nom, stade.ville
HAVING COUNT(partie.id_partie) >= 5;"""

# Les parties avec un score total supérieur à 6
Query_4 = """
SELECT partie.date_partie, partie.phase, equipe_receveur.nom_pays AS equipe_receveuse, partie.score_dom AS score_receveur, equipe_visiteur.nom_pays AS equipe_visiteuse, partie.score_ext AS score_visiteuse
FROM partie
JOIN equipe AS equipe_receveur ON partie.equipe_dom_id = equipe_receveur.id_equipe
JOIN equipe AS equipe_visiteur ON partie.equipe_ext_id = equipe_visiteur.id_equipe
WHERE (partie.score_dom + partie.score_ext) > 6;
"""

