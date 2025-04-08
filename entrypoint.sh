#!/bin/bash

echo "⏳ Attente de la base de données..."
until pg_isready -h db -p 5432 -U yamira; do
  sleep 1
done

echo "Base de données disponible !"

# Créer les tables
echo "Création des tables..."
python create_tables.py

# Générer les données
echo "🧪 Remplissage de la base avec des données factices..."
python data_generator.py

# Lancer Streamlit
echo "🚀 Lancement de l'application Streamlit..."
streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0


