![Alt text](https://github.com/molly-muffin/P11_OC_Gudlft/blob/QA/Python_Testing-master/images/logo.png)

# Améliorez une application Web Python par des tests et du débogage

## Contexte du projet : 
Il s'agit d'un projet de preuve de concept (POC) pour montrer une version allégée de la plateforme de réservation de compétition. L'objectif est de garder les choses aussi légères que possible et d'utiliser les commentaires des utilisateurs.

### Le site permet  :
La reservation de places pour des compétitions.
L'application est alimentée par des fichiers JSON. Il s'agit de contourner le fait d'avoir une base de données jusqu'à ce que nous en ayons réellement besoin. Les principaux sont :
    - competitions.json - liste des compétitions
    - clubs.json - liste des clubs avec des informations pertinentes


### Environnement de développement :
`Python` & `Flask`


### Instruction d’installation et d’utilisation :
- Prérequis et installation
    - Dans le terminal, aller dans le dossier ou vous souhaitez placer le projet et cloner le projet 
    ```bash
    git clone https://github.com/molly-muffin/P11_OC_Gudlft
    ```
    - Aller dans ce dossier
    ```bash
    cd P11_OC_Gudlft/Python_Testing-master/
    ```
    - Créer un environnement virtuel
    ```bash
    python -m venv env
    ```
    - Activer le script
    
    **Windows :**
    ```bash
    .\env\Scripts\activate
    ```
    **Linux :**
    ```bash
    source env\bin\activate
    ```
    - Installer les packages dans le requirements.txt
    ```bash
    pip install -r requirements.txt
    ```

- Lancement
    - Lancer le  **serveur**, avec la commande
    ```bash
    set FLASK_APP=server.py
    flask run 
    ```
    - Puis rendez vous sur http://127.0.0.1:5000/ et accéder à la page d'accès de l'application.


- Utilisation
    - Si vous souhaitez avoir accès à l'application, il faut être pré-enregistré par l'administrateur, la liste des emails autorisés à acceder à l'application sont dans le fichier [clubs.json](https://github.com/molly-muffin/P11_OC_Gudlft/blob/QA/Python_Testing-master/clubs.json).


### Vérification du code
- Contrôle du code avec **flake8** :
```bash
flake8 --max-line-length 130 --format=html --htmldir=flake-report
```
- Performance du code avec **locust** :
```bash
locust -f locustfile.py
```
--> puis rendez-vous sur : http://http://localhost:8089/

> Laureenda Demeule
> OpenClassroom
