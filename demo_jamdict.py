from jamdict import Jamdict

jam = Jamdict()

def afficher_demo():
    print("=" * 55)
    print("   JAMDICT - Dictionnaire Japonais-Anglais")
    print("=" * 55)
    print("\nJamdict donne acces a JMdict (200 000+ mots)")
    print("avec definitions, lectures et infos sur les kanji.")
    print("-" * 55)
    
    exemples = ["食べる", "日本", "学生", "愛"]
    
    print("\nExemples de recherche:")
    print("-" * 55)
    
    for mot in exemples:
        chercher_mot(mot)

def chercher_mot(mot):
    result = jam.lookup(mot)
    
    if result.entries:
        entry = result.entries[0]
        print(f"\n  {mot}")
        
        if entry.kana_forms:
            print(f"  Lecture: {entry.kana_forms[0]}")
        
        for i, sense in enumerate(entry.senses[:3], 1):
            gloss_list = [str(g) for g in sense.gloss]
            print(f"  {i}. {', '.join(gloss_list)}")
    
    if result.chars:
        print(f"\n  Kanji dans '{mot}':")
        for char in result.chars[:3]:
            meanings = char.meanings(english_only=True)[:3]
            print(f"    {char.literal} ({char.stroke_count} traits): {', '.join(meanings)}")

def mode_interactif():
    print("\n" + "=" * 55)
    print("MODE INTERACTIF")
    print("-" * 55)
    print("Entrez un mot japonais ou anglais pour chercher")
    print("Tapez :q! pour revenir au menu principal")
    print("-" * 55)
    
    while True:
        texte = input("\nRecherche: ").strip()
        
        if texte == ":q!":
            print("Retour au menu...")
            break
        
        if not texte:
            continue
        
        result = jam.lookup(texte)
        
        if not result.entries and not result.chars:
            print("  Aucun resultat trouve.")
            continue
        
        if result.entries:
            print(f"\n  Resultats pour '{texte}':")
            print("-" * 40)
            
            for entry in result.entries[:5]:
                kanji = entry.kanji_forms[0] if entry.kanji_forms else ""
                kana = entry.kana_forms[0] if entry.kana_forms else ""
                
                if kanji:
                    print(f"\n  {kanji} ({kana})")
                else:
                    print(f"\n  {kana}")
                
                for i, sense in enumerate(entry.senses[:3], 1):
                    pos = sense.pos if sense.pos else []
                    gloss_list = [str(g) for g in sense.gloss]
                    print(f"    {i}. {', '.join(gloss_list)}")
        
        if result.chars:
            print(f"\n  Kanji trouves:")
            for char in result.chars[:5]:
                meanings = char.meanings(english_only=True)[:3]
                
                on_readings = []
                kun_readings = []
                if char.rm_groups:
                    rm = char.rm_groups[0]
                    on_readings = [str(r) for r in rm.on_readings[:2]] if rm.on_readings else []
                    kun_readings = [str(r) for r in rm.kun_readings[:2]] if rm.kun_readings else []
                
                print(f"\n    {char.literal} ({char.stroke_count} traits)")
                print(f"      Sens: {', '.join(meanings)}")
                if on_readings:
                    print(f"      On'yomi: {', '.join(on_readings)}")
                if kun_readings:
                    print(f"      Kun'yomi: {', '.join(kun_readings)}")

if __name__ == "__main__":
    afficher_demo()
    mode_interactif()
