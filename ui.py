# ui.py
"""
Gestion des composants de l'interface utilisateur Streamlit pour l'application
d'extraction de transcripts YouTube et de génération de résumés.
"""

import streamlit as st

def create_ui():
    """
    Crée l'interface utilisateur principale de l'application.
    
    :return: L'URL de la vidéo YouTube entrée par l'utilisateur
    """
    st.title("Extracteur de Transcripts YouTube et Générateur de Résumés")
    
    url = st.text_input("Entrez l'URL de la vidéo YouTube:")
    
    if st.button("Extraire et résumer"):
        if url:
            return url
        else:
            st.warning("Veuillez entrer une URL valide.")
    
    return None

def display_results(transcript, summary, language):
    """
    Affiche le transcript original et le résumé généré côte à côte.
    
    :param transcript: Le transcript original
    :param summary: Le résumé généré
    :param language: La langue du transcript
    """
    st.success(f"Transcript extrait et résumé généré avec succès en {language}!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Transcript original")
        st.text_area("", value=transcript, height=300)
    
    with col2:
        st.subheader("Résumé généré")
        st.text_area("", value=summary, height=300)