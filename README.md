##### Outils :

* Docker et docker

#### Langugues et base de données:

* Python 3.12 avec les bibliothèques (voir requirements.txt):
  2.1 streamlit
  2.2 sqlalchemy
  2.3 psycopg2-binary
  2.4 pandas
  2.5 python-dotenv
  2.6 faker
* PostgresSQL15

#### Base de données

La base de données PostgresSQL est configurée automatiquement via Docker Compose. Les paramètres par défault sont définis dans le fichier .env

Lors du démarrage, les scripts suivnats osnt exécutés :

1. create_tables.py : Crée les tables dans la base de données
2. data_generator.py: Génère des données fictives

#### Utilisateur par défault:

* Utilisateur: postgres
* Mot de passe: postgres
* Base de données: coupe_du_monde
* Hote: localhost
* Port: 5432

#### Instructions d'exécution

1. Pour lancer l'application, lancer docker et exécuter la commande suivante dans le répertoire coupe_du_monde:

   ```
   docker-compose up --build 
   ```

Cela :

1. démarre une base PostgreSQL
2. crée les tables
3. insère des données fictives
4. lance l’application Streamlit
5. Ouvrir l’application dans le navigateur :
   📍 http://localhost:8501

#### Dépannage

#### Vérifier si Docker fonctionne :

````
docker --version
docker-compose --version
````

#### Erreur : base de données inaccessible ?

Attendez quelques secondes : le conteneur attend automatiquement que PostgreSQL soit prêt avant de démarrer.

#### Si un conteneur est figé :

````
docker-compose down -v 
docker-compose up --build
````
