# youtube_transcript.py
"""
Gestion des opérations liées à l'extraction des transcripts YouTube.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from utils import extract_video_id

def get_best_transcript(video_id):
    """
    Récupère le meilleur transcript disponible pour une vidéo YouTube.
    
    :param video_id: L'ID de la vidéo YouTube
    :return: Le meilleur transcript disponible et sa langue
    """
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        for transcript in transcript_list:
            if not transcript.is_generated:
                return transcript.fetch(), transcript.language
        
        for transcript in transcript_list:
            if transcript.is_generated:
                return transcript.fetch(), transcript.language
        
        raise Exception("Aucun transcript disponible")
    except Exception as e:
        raise Exception(f"Erreur lors de la récupération du transcript : {str(e)}")

def extract_transcript(url):
    """
    Extrait le meilleur transcript disponible d'une vidéo YouTube à partir de son URL.
    
    :param url: L'URL de la vidéo YouTube
    :return: Le transcript sous forme de texte et la langue du transcript
    """
    try:
        video_id = extract_video_id(url)
        transcript, language = get_best_transcript(video_id)
        
        transcript_text = " ".join([entry['text'] for entry in transcript])
        
        return transcript_text, language
    except Exception as e:
        raise Exception(f"Erreur lors de l'extraction du transcript : {str(e)}")