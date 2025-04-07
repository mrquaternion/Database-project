## TODO 
# les équipes avec le plus grand nombres de cartons rouges dans l'histoire du coupe du monde entre 1986-2022
Query_1 = """SELECT equipe.nom_pays, COUNT(joueur.id) AS nombre_cartons_rouges
FROM joueur
JOIN equipe ON joueur.equipe_id = equipe.id
WHERE joueur.carton_rouge >= 1
GROUP BY equipe.nom_pays
ORDER BY nombre_cartons_rouges DESC ;"""

# les arbitres qui ont arbitré le plus de parties
Query_2 = """SELECT arbitre.nom, arbitre.prenom, COUNT(arbitre_dans.partie_id) AS nombre_parties
FROM arbitre
JOIN arbitre_dans ON arbitre.id = arbitre_dans.arbitre_id
GROUP BY arbitre.nom, arbitre.prenom
ORDER BY nombre_parties DESC;"""

# les stades qui ont accueilli plus de 5 parties
Query_3 = """SELECT stade.nom, stade.ville, COUNT(partie.id) AS nombre_parties
FROM stade
JOIN partie ON stade.id = partie.stade_id
GROUP BY stade.nom, stade.ville
HAVING COUNT(partie.id) >= 5;"""

# les parties avec un score total supérieur à 6
Query_4 = """SELECT partie.date, partie.phase, equipe_recevante.nom_pays AS equipe_recevante, partie.score_recevante, equipe_visiteuse.nom_pays AS equipe_visiteuse, partie.score_visiteuse
FROM partie
JOIN equipe AS equipe_recevante ON partie.equipe_recevante_id = equipe_recevante.id
JOIN equipe AS equipe_visiteuse ON partie.equipe_visiteuse_id = equipe_visiteuse.id
WHERE (partie.score_recevante + partie.score_visiteuse) > 6;"""