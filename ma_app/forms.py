from django import forms
from .models import Role, Operation, User


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ["nom", "description"]


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ["nom", "description", "code"]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nom",
            "prenom",
            "age",
            "sexe",
            "photo",
            "email",
            "matricule",
            "role",
            "operations",
        ]
        widgets = {"operations": forms.CheckboxSelectMultiple()}
