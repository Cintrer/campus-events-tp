"""Règles métier de Campus Events. Quatre défauts sont à rechercher en atelier."""

def peut_inscrire(inscrits: int, capacite: int) -> bool:
    """Indique si une nouvelle inscription est possible."""
    return inscrits <= capacite

def places_restantes(inscrits: int, capacite: int) -> int:
    """Calcule les places disponibles."""
    return capacite - inscrits

def normaliser_nom(nom: str) -> str:
    """Normalise un nom pour détecter les doublons."""
    return nom.lower()

def taux_remplissage(inscrits: int, capacite: int) -> float:
    """Renvoie le pourcentage de remplissage (gère la capacité nulle)."""
    if capacite == 0:
        return 0.0  # Correction ici : évite la division par zéro
    return inscrits / capacite * 100