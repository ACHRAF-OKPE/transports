from fastapi import APIRouter, HTTPException
from typing import List
from . import models

router = APIRouter()

commandes = []  # Simule une base de données en mémoire (à remplacer par une vraie base de données)
commande_id_counter = 1

@router.post("/commandes/", response_model=models.Commande, status_code=201)
def creer_commande(commande: models.Commande):
    global commande_id_counter
    commande.id = commande_id_counter
    commandes.append(commande)
    commande_id_counter += 1
    return commande

@router.get("/commandes/", response_model=List[models.Commande])
def lire_commandes():
    return commandes

@router.get("/commandes/{commande_id}", response_model=models.Commande)
def lire_commande(commande_id: int):
    for commande in commandes:
        if commande.id == commande_id:
            return commande
    raise HTTPException(status_code=404, detail="Commande non trouvée")