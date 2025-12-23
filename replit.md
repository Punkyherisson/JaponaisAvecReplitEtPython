# Projet Romkan - Conversion Japonais

## Vue d'ensemble
Démonstration de la bibliothèque Python `romkan` pour la conversion entre romaji (caractères latins) et les écritures japonaises (hiragana/katakana).

## Structure du projet
- `demo_romkan.py` - Script de démonstration des fonctionnalités de romkan
- `ime_japonais.py` - Simulateur d'IME japonais (frappe lettre par lettre)
- `traducteur_deepl.py` - Traducteur vers le japonais via API DeepL

## Dépendances
- Python 3.11
- romkan (conversion romaji/kana)
- requests (appels API)

## Secrets requis
- `DEEPL_API_KEY` - Clé API DeepL (stockée de façon sécurisée)

## Fonctionnalités
1. Romaji → Hiragana/Katakana
2. Hiragana/Katakana → Romaji
3. Mode IME interactif (frappe lettre par lettre)
4. Traduction vers le japonais via DeepL

## Exécution
```bash
python demo_romkan.py      # Démo romkan
python ime_japonais.py     # IME interactif
python traducteur_deepl.py # Traducteur DeepL
```
