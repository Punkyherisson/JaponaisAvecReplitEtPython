import os
import sys

def afficher_menu():
    print("\n" + "=" * 50)
    print("   OUTILS JAPONAIS - MENU PRINCIPAL")
    print("=" * 50)
    print("\n  1. Demo Romkan (conversions romaji/kana)")
    print("  2. IME Japonais (frappe lettre par lettre)")
    print("  3. Traducteur DeepL (traduction vers japonais)")
    print("  4. Quitter")
    print("\n" + "-" * 50)

def main():
    while True:
        afficher_menu()
        choix = input("Votre choix (1-4): ").strip()
        
        if choix == "1":
            print("\n>>> Lancement de la demo Romkan...\n")
            exec(open("demo_romkan.py").read())
            input("\nAppuyez sur Entrée pour revenir au menu...")
            
        elif choix == "2":
            print("\n>>> Lancement de l'IME Japonais...\n")
            exec(open("ime_japonais.py").read())
            input("\nAppuyez sur Entrée pour revenir au menu...")
            
        elif choix == "3":
            print("\n>>> Lancement du Traducteur DeepL...\n")
            exec(open("traducteur_deepl.py").read())
            input("\nAppuyez sur Entrée pour revenir au menu...")
            
        elif choix == "4":
            print("\nAu revoir!")
            sys.exit(0)
            
        else:
            print("\nChoix invalide. Veuillez entrer 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
