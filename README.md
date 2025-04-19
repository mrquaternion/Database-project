## 🐳 Pré-requis : Docker et Docker Compose

Ce projet est entièrement contené avec Docker. Vous n’avez **rien d’autre à installer** que Docker.

### 🔧 Installer Docker

#### ▶️ Windows 10/11

1. Télécharger Docker Desktop :https://www.docker.com/products/docker-desktop/
2. Suivre les instructions d'installation, puis redémarrer l'ordinateur si nécessaire.

#### 🍎 macOS (Intel ou Apple Silicon)

1. Télécharger Docker Desktop pour Mac :https://www.docker.com/products/docker-desktop/
2. Ouvrir l’image `.dmg` téléchargée, puis glisser Docker dans Applications.

#### 🐧 Linux (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo systemctl enable docker
```

#### 🚀 Lancer le projet

Cloner ce dépôt :

```bash
git clone <lien_du_repository>
cd coupe_du_monde
```

Lancer l'application :

````bash
docker-compose up --build
````

Cela :

1. démarre une base PostgreSQL
2. crée les tables
3. insère des données fictives
4. lance l’application Streamlit
5. Ouvrir l’application dans le navigateur :
   📍 http://localhost:8501


#### 🌐 Ouvrir automatiquement le navigateur (facultatif)

💻 macOS :
````
open http://localhost:8501
````
🐧 Linux :
````
xdg-open http://localhost:8501
````
🪟 Windows (PowerShell) :
````
start http://localhost:8501
````

#### 🧪 Dépannage

#### 🔍 Vérifier si Docker fonctionne :
````
docker --version
docker-compose --version
````
#### 🐘 Erreur : base de données inaccessible ?
Attendez quelques secondes : le conteneur attend automatiquement que PostgreSQL soit prêt avant de démarrer.

#### ❌ Si un conteneur est figé :
````
docker-compose down
docker-compose up --build
````

