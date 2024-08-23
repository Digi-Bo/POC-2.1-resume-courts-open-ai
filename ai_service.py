# ai_service.py
"""
Interface avec les services d'IA pour la génération de résumés.
"""

import openai
from config import load_config

config = load_config()
openai.api_key = config['OPENAI_API_KEY']

def get_ai_summary(prompt):
    """
    Génère un résumé en utilisant l'API OpenAI.
    
    :param prompt: Le prompt pour générer le résumé
    :return: Le résumé généré par l'IA
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise Exception(f"Erreur lors de l'appel à l'API OpenAI : {str(e)}")