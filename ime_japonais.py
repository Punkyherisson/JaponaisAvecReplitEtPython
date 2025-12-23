import romkan

def afficher_guide():
    print("=" * 55)
    print("   CLAVIER JAPONAIS - Tapez en romaji")
    print("=" * 55)
    print("\nGuide de frappe:")
    print("-" * 55)
    print("  Voyelles: a→あ  i→い  u→う  e→え  o→お")
    print()
    print("  ka ki ku ke ko → か き く け こ")
    print("  sa shi su se so → さ し す せ そ")
    print("  ta chi tsu te to → た ち つ て と")
    print("  na ni nu ne no → な に ぬ ね の")
    print("  ha hi fu he ho → は ひ ふ へ ほ")
    print("  ma mi mu me mo → ま み む め も")
    print("  ya yu yo → や ゆ よ")
    print("  ra ri ru re ro → ら り る れ ろ")
    print("  wa wo → わ を")
    print("  n (ou nn) → ん")
    print()
    print("  Sons speciaux: sha→しゃ  chi→ち  tsu→つ")
    print("-" * 55)

def mode_interactif():
    afficher_guide()
    
    print("\nCommandes:")
    print("  :h  → Hiragana (defaut)")
    print("  :k  → Katakana")
    print("  :q! → Quitter")
    print("-" * 55)
    
    mode = "hiragana"
    
    while True:
        indicateur = "ひ" if mode == "hiragana" else "カ"
        texte = input(f"\n[{indicateur}] Romaji: ").strip()
        
        if texte == ":q!":
            print("Retour au menu...")
            break
        
        if not texte:
            continue
        
        mode_temp = mode
        if texte.startswith(":h "):
            mode_temp = "hiragana"
            texte = texte[3:]
        elif texte.startswith(":k "):
            mode_temp = "katakana"
            texte = texte[3:]
        elif texte == ":h":
            mode = "hiragana"
            print("  Mode: Hiragana")
            continue
        elif texte == ":k":
            mode = "katakana"
            print("  Mode: Katakana")
            continue
        
        if mode_temp == "hiragana":
            resultat = romkan.to_hiragana(texte)
        else:
            resultat = romkan.to_katakana(texte)
        
        print(f"  → {resultat}")

if __name__ == "__main__":
    mode_interactif()
