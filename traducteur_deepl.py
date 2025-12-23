import os
import requests

DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY")

DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

def traduire_en_japonais(texte, format_sortie="hiragana"):
    """
    Traduit un texte en japonais via l'API DeepL.
    
    Args:
        texte: Le texte à traduire
        format_sortie: "normal" pour le japonais standard, 
                      "hiragana" pour afficher aussi la lecture
    
    Returns:
        Le texte traduit en japonais
    """
    if not DEEPL_API_KEY:
        print("ERREUR: Clé API DeepL non trouvée!")
        print("Ajoutez votre clé dans les Secrets de Replit avec le nom 'DEEPL_API_KEY'")
        return None
    
    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "text": [texte],
        "target_lang": "JA"
    }
    
    try:
        response = requests.post(DEEPL_API_URL, headers=headers, json=data)
        response.raise_for_status()
        
        resultat = response.json()
        traduction = resultat["translations"][0]["text"]
        return traduction
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            print("ERREUR: Clé API invalide ou quota dépassé")
        elif response.status_code == 456:
            print("ERREUR: Quota de caractères dépassé")
        else:
            print(f"ERREUR HTTP: {e}")
        return None
    except Exception as e:
        print(f"ERREUR: {e}")
        return None


def demo():
    """Démonstration de la traduction"""
    print("=" * 60)
    print("TRADUCTEUR DEEPL → JAPONAIS")
    print("=" * 60)
    
    exemples = [
        "Hello, how are you?",
        "I love sushi",
        "The weather is nice today",
        "Thank you very much"
    ]
    
    print("\nExemples de traduction:")
    print("-" * 40)
    
    for texte in exemples:
        traduction = traduire_en_japonais(texte)
        if traduction:
            print(f"  {texte}")
            print(f"  → {traduction}")
            print()


def mode_interactif():
    """Mode interactif pour traduire vos propres textes"""
    print("\n" + "=" * 60)
    print("MODE INTERACTIF - Tapez votre texte (en anglais ou français)")
    print("Tapez 'q' pour quitter")
    print("=" * 60)
    
    while True:
        texte = input("\nTexte à traduire: ").strip()
        
        if texte.lower() == 'q':
            print("Au revoir!")
            break
        
        if not texte:
            continue
        
        traduction = traduire_en_japonais(texte)
        if traduction:
            print(f"\n  Japonais: {traduction}")


if __name__ == "__main__":
    if not DEEPL_API_KEY:
        print("=" * 60)
        print("CONFIGURATION REQUISE")
        print("=" * 60)
        print("\nPour utiliser ce script, vous devez:")
        print("1. Aller dans l'onglet 'Secrets' de Replit (icône cadenas)")
        print("2. Créer un nouveau secret avec:")
        print("   - Clé: DEEPL_API_KEY")
        print("   - Valeur: votre clé API DeepL")
        print("3. Relancer le script")
        print("\nVotre clé sera chiffrée et jamais visible dans le code!")
    else:
        demo()
        mode_interactif()
