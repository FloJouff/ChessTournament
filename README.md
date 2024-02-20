## Etapes à suivre pour l'installation et l'utilisation du Programme des gestion des tournois d'échecs

### Etapes d'installation:

#### Installer Python 
    
L’installation de Python est très simple ! Rendez-vous sur [python.org](https://www.python.org/downloads/), choisissez votre système d’exploitation (Mac/Windows, etc.) et cliquez sur le bouton de téléchargement pour installer Python sur votre ordinateur. 

Si vous utilisez Windows, pensez à bien cocher la case "Add to path" pour ajouter Python aux variables d'environnement.

#### Faire une copie du repository.

A partir du lien GitHub: https://github.com/FloJouff/ChessTournament, créer un clone du projet en local sur votre ordinateur


#### Création de l'environnement virtuel 

Depuis votre terminal, à la racine du projet, créer un environnement virtuel, afin d'y installer uniquement les paquets Python nécessaires à l'exécution du script.

    $ python -m venv env

#### Activation de l'environnement virtuel

A partir du terminal, taper la commande suivante:

    $ source env/bin/activate (pour MacOs, Linux)
    $ env\scripts\activate (pour Windows)

#### Installation des paquets Python nécessaires à l'execution du code: 

Le fichier --requirements.txt-- a été cloné à partir du repository GitHub.
A partir du terminal, taper la commande suivante:
   
    $ pip install -r requirements.txt

Une fois l'installation terminée, taper la commande suivante pour vous assurer de l'installation correcte des modules requis:

    $ pip freeze



### Exécution du code d'application:

#### Lancer le script à partir du terminal: 

Vous pouvez enfin exécuter le script main.py correctement, à partir d'un terminal.
Ce fichier permet, une fois exécuté, de lancer la récolte des données sur l'intégralité du site.

    $ Python main.py


### Consultation des données:



