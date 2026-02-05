# e_commerce

Projet Django minimal pour gérer `Role`, `Operation`, et `User` avec formulaires et interface.

Instructions rapides:

1. Créez un environnement virtuel et installez les dépendances:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Appliquez les migrations et lancez le serveur:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

3. Ouvrez http://127.0.0.1:8000/ pour accéder aux formulaires, et `/admin` pour l'admin.

Remarques:
- Le fichier `db.sqlite3` et le dossier `media/` sont ignorés par git (ajoutez au dépôt si vous le souhaitez).
- Pour pousser vers GitHub: créez un repo distant et exécutez `git remote add origin <url>` puis `git push -u origin main`.
