import pykakasi

def afficher_demo():
    print("=" * 55)
    print("   PYKAKASI - Lecture des Kanji")
    print("=" * 55)
    print("\nPykakasi convertit le japonais (kanji inclus) en romaji.")
    print("Ideal pour apprendre a lire les kanji!")
    print("-" * 55)
    
    kks = pykakasi.kakasi()
    
    exemples = [
        ("日本語", "Langue japonaise"),
        ("東京", "Tokyo"),
        ("私は学生です", "Je suis etudiant"),
        ("食べ物", "Nourriture"),
        ("桜", "Cerisier"),
        ("新幹線", "Shinkansen"),
    ]
    
    print("\nExemples de conversion:")
    print("-" * 55)
    
    for kanji, sens in exemples:
        result = kks.convert(kanji)
        romaji = "".join([item['hepburn'] for item in result])
        hiragana = "".join([item['hira'] for item in result])
        
        print(f"\n  Kanji:    {kanji} ({sens})")
        print(f"  Hiragana: {hiragana}")
        print(f"  Romaji:   {romaji}")
    
    print("\n" + "=" * 55)

def mode_interactif():
    print("\nMODE INTERACTIF")
    print("-" * 55)
    print("Entrez du texte japonais (avec kanji) pour voir la lecture")
    print("Tapez :q! pour revenir au menu principal")
    print("-" * 55)
    
    kks = pykakasi.kakasi()
    
    while True:
        texte = input("\nTexte japonais: ").strip()
        
        if texte == ":q!":
            print("Retour au menu...")
            break
        
        if not texte:
            continue
        
        result = kks.convert(texte)
        
        print("\n  Detail par mot:")
        for item in result:
            if item['orig'] != item['hira']:
                print(f"    {item['orig']} → {item['hira']} ({item['hepburn']})")
        
        romaji = "".join([item['hepburn'] for item in result])
        hiragana = "".join([item['hira'] for item in result])
        katakana = "".join([item['kana'] for item in result])
        
        print(f"\n  Hiragana: {hiragana}")
        print(f"  Katakana: {katakana}")
        print(f"  Romaji:   {romaji}")

if __name__ == "__main__":
    afficher_demo()
    mode_interactif()
