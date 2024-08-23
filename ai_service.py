# ai_service.py
"""
Interface avec les services d'IA pour la génération de résumés.
"""

from openai import OpenAI
from config import load_config, get_openai_model

config = load_config()
client = OpenAI(api_key=config['OPENAI_API_KEY'])

def get_ai_summary(prompt):
    """
    Génère un résumé en utilisant l'API OpenAI.
    
    :param prompt: Le prompt pour générer le résumé
    :return: Le résumé généré par l'IA
    """
    try:
        response = client.chat.completions.create(
            model=get_openai_model(),
            messages=[
                {"role": "system", "content": "Vous êtes un assistant spécialisé dans la création de résumés concis et pertinents."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            n=1,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise Exception(f"Erreur lors de l'appel à l'API OpenAI : {str(e)}")