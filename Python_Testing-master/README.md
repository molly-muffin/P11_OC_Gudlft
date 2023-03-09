### Installation :

-------------------------------------- WINDOWS --------------------------------------

* Tapez la commande WIN+R, tapez 'cmd' et Entrée puis rendez vous dans le dossier du clone

* Pour vous rendre dans le fichier du projet, tapez cd puis le chemin d'accès, 
ou aidez vous de la touche TABULATION 
  * Exemple:  
  ```C:\Users\Pierre> cd Desktop``` (Vous fera parvenir au bureau)

* Une fois dans le fichier du projet que vous avez téléchargé, créez un environnement virtuel avec la commande:  
```python -m venv virtualenv```

* Activez le ensuite avec la commande :  
```virtualenv\Scripts\activate.bat```

* Puis récupérez les packages Python de requirements.txt avec la commande suivante :  
```pip install -r requirements.txt```

* Enfin allumez le serveur en entrant : 
```
set FLASK_APP=server.py

flask run 
```
* Vous pouvez maintenant vous rendre sur le site dans un navigateur avec l'adresse http://127.0.0.1:5000/

* Pour arrêter le serveur, appuyez sur CTRL + C dans le terminal
