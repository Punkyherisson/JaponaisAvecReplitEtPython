import romkan
import re

def adapter_pour_japonais(texte):
    """Adapte un mot européen pour qu'il soit prononçable en japonais"""
    texte = texte.lower()
    
    adaptations = [
        ('mm', 'm'),
        ('nn', 'n'),
        ('ll', 'r'),
        ('l', 'ru'),
        ('v', 'b'),
        ('x', 'kusu'),
        ('q', 'ku'),
        ('c(?![hi])', 'k'),
        ('ti', 'chi'),
        ('tu', 'tsu'),
        ('si', 'shi'),
        ('hu', 'fu'),
        ('th', 's'),
        ('ph', 'f'),
    ]
    
    for pattern, remplacement in adaptations:
        texte = re.sub(pattern, remplacement, texte)
    
    if texte and texte[-1] in 'bcdfghjklmpqrstvwxz':
        voyelle = 'u'
        if texte[-1] in 'td':
            voyelle = 'o'
        texte = texte + voyelle
    
    return texte

def est_japonais(texte):
    """Vérifie si le texte contient des caractères japonais"""
    for char in texte:
        if '\u3040' <= char <= '\u30ff' or '\u4e00' <= char <= '\u9fff':
            return True
    return False

def afficher_demo():
    print("=" * 50)
    print("DÉMONSTRATION DE ROMKAN")
    print("=" * 50)

    print("\n1. ROMAJI → HIRAGANA")
    print("-" * 30)
    for mot in ["konnichiwa", "arigatou"]:
        print(f"  {mot:15} → {romkan.to_hiragana(mot)}")

    print("\n2. ROMAJI → KATAKANA")
    print("-" * 30)
    for mot in ["koohii", "anime"]:
        print(f"  {mot:15} → {romkan.to_katakana(mot)}")

    print("\n3. HIRAGANA → ROMAJI")
    print("-" * 30)
    for h in ["にんじゃ", "すし"]:
        print(f"  {h:10} → {romkan.to_roma(h)}")

    print("\n4. KATAKANA → ROMAJI")
    print("-" * 30)
    for k in ["コーヒー", "アニメ"]:
        print(f"  {k:10} → {romkan.to_roma(k)}")

    print("\n" + "=" * 50)

def mode_interactif():
    print("\nMODE INTERACTIF")
    print("-" * 50)
    print("Tapez un mot (romaji, nom europeen, ou japonais)")
    print("Les noms europeens seront adaptes au japonais")
    print("Tapez :q! pour revenir au menu principal")
    print("-" * 50)
    
    while True:
        texte = input("\nVotre texte: ").strip()
        
        if texte == ":q!":
            print("Retour au menu...")
            break
        
        if not texte:
            continue
        
        if est_japonais(texte):
            print(f"\n  Romaji:   {romkan.to_roma(texte)}")
        else:
            adapte = adapter_pour_japonais(texte)
            if adapte != texte.lower():
                print(f"\n  Adapte:   {texte} → {adapte}")
            print(f"  Hiragana: {romkan.to_hiragana(adapte)}")
            print(f"  Katakana: {romkan.to_katakana(adapte)}")

if __name__ == "__main__":
    afficher_demo()
    mode_interactif()
