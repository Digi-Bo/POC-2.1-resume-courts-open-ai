# utils.py
"""
Ce fichier contient des fonctions utilitaires génériques utilisées dans différentes parties de l'application.
"""

import re

def extract_video_id(url):
    """
    Extrait l'ID de la vidéo à partir d'une URL YouTube.
    
    :param url: L'URL de la vidéo YouTube
    :return: L'ID de la vidéo
    :raises ValueError: Si l'ID de la vidéo n'est pas trouvé dans l'URL
    """
    # Patterns pour différents formats d'URL YouTube
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',  # URLs standards et embed
        r'(?:vi?=|v%3D|youtu\.be\/|\/v\/|\/embed\/|\/shorts\/)([0-9A-Za-z_-]{11})',  # Autres formats
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    raise ValueError("ID de vidéo non trouvé dans l'URL fournie")

def truncate_text(text, max_length):
    """
    Tronque un texte à une longueur maximale donnée, en évitant de couper au milieu d'un mot.
    
    :param text: Le texte à tronquer
    :param max_length: La longueur maximale souhaitée
    :return: Le texte tronqué
    """
    if len(text) <= max_length:
        return text
    
    truncated = text[:max_length]
    last_space = truncated.rfind(' ')
    
    if last_space != -1:
        return truncated[:last_space] + '...'
    else:
        return truncated + '...'

def format_duration(seconds):
    """
    Formate une durée en secondes en une chaîne lisible (HH:MM:SS).
    
    :param seconds: Le nombre de secondes
    :return: La durée formatée
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if hours:
        return f'{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}'
    else:
        return f'{int(minutes):02d}:{int(seconds):02d}'

# Ajoutez d'autres fonctions utilitaires selon les besoins de votre application