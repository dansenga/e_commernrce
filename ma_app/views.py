from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RoleForm, OperationForm, UserForm


def index(request):
    return render(request, "ma_app/base.html")


def create_role(request):
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rôle ajouté avec succès.")
            return redirect("create_role")
    else:
        form = RoleForm()
    return render(request, "ma_app/role_form.html", {"form": form})


def create_operation(request):
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Opération ajoutée avec succès.")
            return redirect("create_operation")
    else:
        form = OperationForm()
    return render(request, "ma_app/operation_form.html", {"form": form})


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # Save instance without relying on form.save_m2m()
            user = form.save(commit=False)
            user.save()
            # Handle many-to-many explicitly
            operations = form.cleaned_data.get("operations")
            if operations is not None:
                user.operations.set(operations)
            messages.success(request, f"Utilisateur {user.nom} {user.prenom} créé avec succès.")
            return redirect("create_user")
    else:
        form = UserForm()
    return render(request, "ma_app/user_form.html", {"form": form})
