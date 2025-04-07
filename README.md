### 1. Installer les dépendances 

```
pip install -r requirements.txt
```

### 2. Créer les tables 

Valider que la base de données PostgresSQL est active et que le fichier .env contient DATABASE_URL:

DATABASE_URL=postgresql://<utilisateur>@localhost:<port>/coupe_du_monde_db


Exécuter :

```
python3 create_tables.py
```

### 3. Remplir la base de données 

Exécuter: 

```
python3 data_generator.py
```

### 4. Lancer Streamlit

```
streamlit run streamlit_app.py
```
