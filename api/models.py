from pydantic import BaseModel
from typing import Optional

class Adresse(BaseModel):
    rue: str
    ville: str
    code_postal: str
    pays: str

class Commande(BaseModel):
    id: Optional[int] = None
    adresse_depart: Adresse
    adresse_arrivee: Adresse
    type_marchandises: str
    poids: float
    volume: float
    client_id: int  # Identifiant du client
    statut: str = "en attente"  # Statut par défaut