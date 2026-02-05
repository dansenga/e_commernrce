from django.db import models

# Create your models here.

class Role(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    # Django crée automatiquement un champ id comme clé primaire
    def __str__(self):
        return self.nom


class Operation(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nom} ({self.code})"


class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    email = models.EmailField(unique=True)
    matricule = models.CharField(max_length=50, unique=True)

    # Relations
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")
    operations = models.ManyToManyField(Operation, related_name="users")

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.matricule}"
