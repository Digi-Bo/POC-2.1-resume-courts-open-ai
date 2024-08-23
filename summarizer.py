# summarizer.py
"""
Gestion de la génération de résumés courts à partir des transcripts.
"""

from ai_service import get_ai_summary

def generate_summary(transcript, max_length=150):
    """
    Génère un résumé court à partir du transcript.
    
    :param transcript: Le transcript à résumer
    :param max_length: La longueur maximale du résumé en mots
    :return: Le résumé généré
    """
    prompt = f"Résumez le texte suivant en environ {max_length} mots :\n\n{transcript}"
    
    try:
        summary = get_ai_summary(prompt)
        return summary
    except Exception as e:
        raise Exception(f"Erreur lors de la génération du résumé : {str(e)}")