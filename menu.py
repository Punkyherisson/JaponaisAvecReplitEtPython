import os
import sys
import subprocess

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def afficher_menu():
    clear_screen()
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
            subprocess.run([sys.executable, "demo_romkan.py"])
            input("\nAppuyez sur Entrée pour revenir au menu...")
            
        elif choix == "2":
            print("\n>>> Lancement de l'IME Japonais...\n")
            subprocess.run([sys.executable, "ime_japonais.py"])
            input("\nAppuyez sur Entrée pour revenir au menu...")
            
        elif choix == "3":
            print("\n>>> Lancement du Traducteur DeepL...\n")
            subprocess.run([sys.executable, "traducteur_deepl.py"])
            input("\nAppuyez sur Entrée pour revenir au menu...")
            
        elif choix == "4":
            print("\nAu revoir!")
            sys.exit(0)
            
        else:
            print("\nChoix invalide. Veuillez entrer 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
