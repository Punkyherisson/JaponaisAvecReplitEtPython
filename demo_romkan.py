import romkan

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
    print("Tapez un mot en romaji, hiragana ou katakana")
    print("Tapez :q! pour revenir au menu principal")
    print("-" * 50)
    
    while True:
        texte = input("\nVotre texte: ").strip()
        
        if texte == ":q!":
            print("Retour au menu...")
            break
        
        if not texte:
            continue
        
        print(f"\n  Hiragana: {romkan.to_hiragana(texte)}")
        print(f"  Katakana: {romkan.to_katakana(texte)}")
        print(f"  Romaji:   {romkan.to_roma(texte)}")

if __name__ == "__main__":
    afficher_demo()
    mode_interactif()
