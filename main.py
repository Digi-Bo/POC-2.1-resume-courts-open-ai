# main.py
"""
Point d'entrée principal de l'application Streamlit pour l'extraction de transcripts YouTube
et la génération de résumés courts.
"""

import streamlit as st
from ui import create_ui, display_results
from youtube_transcript import extract_transcript
from summarizer import generate_summary
from config import load_config

def main():
    """Fonction principale gérant le flux de l'application."""
    # Chargement de la configuration
    config = load_config()
    
    # Création de l'interface utilisateur
    url = create_ui()
    
    # Si une URL est fournie, on extrait le transcript et génère le résumé
    if url:
        try:
            transcript, language = extract_transcript(url)
            summary = generate_summary(transcript, config['SUMMARY_LENGTH'])
            display_results(transcript, summary, language)
        except Exception as e:
            st.error(f"Erreur lors du traitement : {str(e)}")
            st.info("Assurez-vous que la vidéo dispose d'un transcript et que l'URL est valide.")

if __name__ == "__main__":
    main()