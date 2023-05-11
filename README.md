[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![GitHub last commit](https://img.shields.io/github/last-commit/ArianDervishaj/EcoTrivia.svg)](https://github.com/ArianDervishaj/EcoTrivia/commits/master)

# EcoTrivia - Jeu de Quiz sur le Changement Climatique

EcoTrivia est une application interactive de quiz et de questions-réponses conçue pour sensibiliser et éduquer les joueurs sur le changement climatique et les problématiques environnementales. Testez vos connaissances, apprenez de nouveaux faits et défiez vos amis pour devenir un champion de l'écologie !

## Fonctionnalités

- **Questions à choix multiples** : Plongez dans une expérience de trivia amusante et éducative avec une grande variété de questions à choix multiples sur le changement climatique, la durabilité, les énergies renouvelables et bien d'autres sujets.

- **Catégories et Niveaux de Difficulté** : Explorez différentes catégories et choisissez parmi différents niveaux de difficulté pour adapter le jeu à votre expertise et à vos objectifs d'apprentissage.

- **Classement** : Grimpez en haut du classement en répondant correctement et rapidement aux questions.

- **Informations Éducatives** : Obtenez des explications détaillées pour chaque question, vous permettant d'approfondir votre compréhension des sujets liés au changement climatique et à l'environnement.

## Technologies Utilisées

- Backend : Django (Python)
- Frontend : React (JavaScript)
- Base de données : MySQL

## Prise en Main

Pour exécuter EcoTrivia localement et contribuer au projet, suivez ces étapes :

1. Clonez le dépôt : `git clone https://github.com/ArianDervishaj/EcoTrivia.git`
2. Assurez-vous d'avoir Python et Node.js installés sur votre système.
3. Installez les dépendances pour le backend en utilisant pip : `pip install -r requirements.txt`
4. Installez les dépendances pour le frontend en utilisant npm : `cd frontend` puis `npm install`
5. Configurez les informations de la base de données dans le fichier `settings.py`.
6. Effectuez les migrations : `python manage.py migrate`
7. Démarrez le serveur de développement pour le backend : `python manage.py runserver`
8. Démarrez le serveur de développement pour le frontend : `cd frontend` puis `npm start`
9. Accédez à l'application dans votre navigateur à l'adresse `http://localhost:3000`.
