from fastapi.testclient import TestClient
from app.api import routes
from app.api import models

client = TestClient(routes.router)

def test_creer_commande():
    commande_data = {
        "adresse_depart": {"rue": "Rue 1", "ville": "Ville 1", "code_postal": "12345", "pays": "Pays 1"},
        "adresse_arrivee": {"rue": "Rue 2", "ville": "Ville 2", "code_postal": "67890", "pays": "Pays 2"},
        "type_marchandises": "Colis",
        "poids": 10.5,
        "volume": 0.1,
        "client_id": 1
    }
    response = client.post("/commandes/", json=commande_data)
    assert response.status_code == 201
    commande = models.Commande(**response.json())
    assert commande.adresse_depart.rue == "Rue 1"

def test_lire_commandes():
    response = client.get("/commandes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_lire_commande():
    response = client.get("/commandes/1")
    assert response.status_code == 200
    commande = models.Commande(**response.json())
    assert commande.id == 1

def test_lire_commande_non_existante():
    response = client.get("/commandes/999")
    assert response.status_code == 404