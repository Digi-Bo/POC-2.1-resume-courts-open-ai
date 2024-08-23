# config.py
"""
Ce fichier gère la configuration de l'application, y compris le chargement des variables d'environnement
et la définition des constantes globales.
"""

import os
from dotenv import load_dotenv

def load_config():
    """
    Charge la configuration de l'application à partir des variables d'environnement.
    
    :return: Un dictionnaire contenant la configuration
    """
    # Chargement des variables d'environnement depuis le fichier .env
    load_dotenv()
    
    # Création d'un dictionnaire de configuration
    config = {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "SUMMARY_LENGTH": int(os.getenv("SUMMARY_LENGTH", 150)),  # Longueur par défaut du résumé
        "MAX_TRANSCRIPT_LENGTH": int(os.getenv("MAX_TRANSCRIPT_LENGTH", 10000)),  # Longueur maximale du transcript à traiter
        "DEBUG_MODE": os.getenv("DEBUG_MODE", "False").lower() == "true",
        "STREAMLIT_THEME": os.getenv("STREAMLIT_THEME", "light"),
        # Ajoutez d'autres variables de configuration selon les besoins
    }
    
    return config

def get_openai_model():
    """
    Retourne le modèle OpenAI à utiliser, avec une valeur par défaut.
    
    :return: Le nom du modèle OpenAI
    """
    return os.getenv("OPENAI_MODEL", "OPENAI_MODEL")

# Vous pouvez ajouter d'autres fonctions de configuration si nécessaire