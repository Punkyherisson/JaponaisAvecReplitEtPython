"""
Lecteur de texte japonais (Text-to-Speech)
-------------------------------------------
Ce module utilise gTTS (Google Text-to-Speech) pour convertir
du texte japonais en audio parlé.

Fonctionnalités:
- Saisie en romaji avec conversion automatique
- Prévisualisation du texte japonais avant génération
- Lecture de texte japonais avec prononciation naturelle
- Sauvegarde des fichiers audio en MP3

Dépendances:
- gtts : Google Text-to-Speech API
- romkan : Conversion romaji vers kana
"""

from gtts import gTTS
import romkan
import os

# Dossier où sauvegarder les fichiers audio
DOSSIER_AUDIO = "audio_japonais"


def creer_dossier_audio():
    """
    Crée le dossier de sauvegarde des fichiers audio s'il n'existe pas.
    """
    if not os.path.exists(DOSSIER_AUDIO):
        os.makedirs(DOSSIER_AUDIO)
        print(f"  Dossier '{DOSSIER_AUDIO}/' créé.")


def generer_nom_fichier(texte):
    """
    Génère un nom de fichier basé sur le texte (les 10 premiers caractères).
    
    Args:
        texte: Le texte japonais à convertir
        
    Returns:
        Un nom de fichier unique avec extension .mp3
    """
    # Prendre les premiers caractères du texte pour le nom
    base = texte[:10].replace(" ", "_").replace("/", "_")
    # Compter les fichiers existants pour éviter les doublons
    compteur = len([f for f in os.listdir(DOSSIER_AUDIO) if f.endswith('.mp3')]) + 1
    return f"{compteur:03d}_{base}.mp3"


def lire_texte_japonais(texte, sauvegarder=True):
    """
    Convertit un texte japonais en audio avec gTTS.
    
    Cette fonction utilise l'API Google Text-to-Speech pour générer
    un fichier audio MP3 à partir du texte japonais fourni.
    
    Args:
        texte: Le texte japonais à lire (peut contenir kanji, hiragana, katakana)
        sauvegarder: Si True, sauvegarde le fichier dans le dossier audio
        
    Returns:
        Le chemin du fichier audio créé, ou None en cas d'erreur
    """
    try:
        # Créer l'objet TTS avec la langue japonaise
        # lang="ja" indique à Google d'utiliser la voix japonaise
        tts = gTTS(text=texte, lang="ja")
        
        # Déterminer le chemin du fichier
        if sauvegarder:
            creer_dossier_audio()
            nom_fichier = generer_nom_fichier(texte)
            chemin = os.path.join(DOSSIER_AUDIO, nom_fichier)
        else:
            chemin = "temp_audio.mp3"
        
        # Sauvegarder le fichier audio
        tts.save(chemin)
        
        return chemin
        
    except Exception as e:
        print(f"  ERREUR: {e}")
        return None


def afficher_demo():
    """
    Démonstration du lecteur avec des exemples de phrases japonaises.
    """
    print("=" * 60)
    print("   LECTEUR JAPONAIS - Text-to-Speech avec gTTS")
    print("=" * 60)
    print("\nCe module convertit du texte japonais en audio parlé.")
    print("Les fichiers sont sauvegardés dans le dossier 'audio_japonais/'")
    print("-" * 60)
    
    # Exemples de phrases à lire (2 exemples seulement)
    exemples = [
        ("こんにちは", "Bonjour"),
        ("ありがとうございます", "Merci beaucoup"),
    ]
    
    print("\nExemples de génération audio:")
    print("-" * 60)
    
    for japonais, francais in exemples:
        print(f"\n  Texte: {japonais}")
        print(f"  Sens:  {francais}")
        
        # Générer l'audio
        chemin = lire_texte_japonais(japonais)
        
        if chemin:
            print(f"  Audio: {chemin}")
    
    print("\n" + "=" * 60)
    print(f"Les fichiers audio ont été sauvegardés dans '{DOSSIER_AUDIO}/'")
    print("Vous pouvez les télécharger et les écouter sur votre appareil.")
    print("=" * 60)


def est_japonais(texte):
    """
    Vérifie si le texte contient des caractères japonais.
    
    Args:
        texte: Le texte à vérifier
        
    Returns:
        True si le texte contient des hiragana, katakana ou kanji
    """
    for char in texte:
        # Hiragana: U+3040 - U+309F
        # Katakana: U+30A0 - U+30FF
        # Kanji: U+4E00 - U+9FFF
        if '\u3040' <= char <= '\u30ff' or '\u4e00' <= char <= '\u9fff':
            return True
    return False


def mode_interactif():
    """
    Mode interactif permettant à l'utilisateur de lire ses propres textes.
    
    L'utilisateur peut entrer:
    - Du texte japonais directement (hiragana, katakana, kanji)
    - Du romaji qui sera converti en hiragana avec confirmation
    
    Commandes spéciales:
    - :q! pour quitter
    - :list pour voir les fichiers générés
    - :h pour hiragana (défaut)
    - :k pour katakana
    """
    print("\nMODE INTERACTIF")
    print("-" * 60)
    print("Entrez du texte en romaji OU en japonais")
    print("Le romaji sera converti en kana avec confirmation")
    print()
    print("Commandes:")
    print("  :q!   - Revenir au menu principal")
    print("  :list - Voir les fichiers audio générés")
    print("  :h    - Mode hiragana (défaut)")
    print("  :k    - Mode katakana")
    print("-" * 60)
    
    # Mode de conversion par défaut
    mode_kana = "hiragana"
    
    while True:
        indicateur = "ひ" if mode_kana == "hiragana" else "カ"
        texte = input(f"\n[{indicateur}] Texte: ").strip()
        
        # Commande pour quitter
        if texte == ":q!":
            print("Retour au menu...")
            break
        
        # Commande pour lister les fichiers
        if texte == ":list":
            lister_fichiers_audio()
            continue
        
        # Commande pour changer de mode
        if texte == ":h":
            mode_kana = "hiragana"
            print("  Mode: Hiragana")
            continue
        
        if texte == ":k":
            mode_kana = "katakana"
            print("  Mode: Katakana")
            continue
        
        # Ignorer les entrées vides
        if not texte:
            continue
        
        # Déterminer si c'est du japonais ou du romaji
        if est_japonais(texte):
            # Le texte est déjà en japonais, utiliser directement
            texte_japonais = texte
            print(f"\n  Texte détecté: {texte_japonais}")
        else:
            # C'est du romaji, convertir en kana
            if mode_kana == "hiragana":
                texte_japonais = romkan.to_hiragana(texte)
            else:
                texte_japonais = romkan.to_katakana(texte)
            
            print(f"\n  Romaji:   {texte}")
            print(f"  Japonais: {texte_japonais}")
        
        # Demander confirmation avant de créer le fichier
        confirmation = input("\n  Créer le fichier audio? (o/n): ").strip().lower()
        
        if confirmation in ['o', 'oui', 'y', 'yes', '']:
            print("  Génération de l'audio...")
            chemin = lire_texte_japonais(texte_japonais)
            
            if chemin:
                print(f"  Fichier créé: {chemin}")
                print("  Téléchargez ce fichier pour l'écouter!")
        else:
            print("  Annulé.")


def lister_fichiers_audio():
    """
    Affiche la liste des fichiers audio générés.
    """
    if not os.path.exists(DOSSIER_AUDIO):
        print("\n  Aucun fichier audio généré pour le moment.")
        return
    
    fichiers = [f for f in os.listdir(DOSSIER_AUDIO) if f.endswith('.mp3')]
    
    if not fichiers:
        print("\n  Aucun fichier audio généré pour le moment.")
        return
    
    print(f"\n  Fichiers dans '{DOSSIER_AUDIO}/':")
    print("-" * 40)
    for f in sorted(fichiers):
        chemin = os.path.join(DOSSIER_AUDIO, f)
        taille = os.path.getsize(chemin) / 1024  # Taille en KB
        print(f"    {f} ({taille:.1f} KB)")


# Point d'entrée du script
if __name__ == "__main__":
    afficher_demo()
    mode_interactif()
