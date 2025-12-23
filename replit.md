# Faire du Japonais avec Replit et Python

## Vue d'ensemble
Une suite d'outils Python pour apprendre et pratiquer le japonais. Ce projet rassemble plusieurs bibliothèques pour la conversion de caractères, la lecture des kanji, la traduction et l'utilisation d'un dictionnaire japonais-anglais.

## Structure du projet
- `menu.py` - Menu principal (point d'entrée)
- `demo_romkan.py` - Conversion romaji vers hiragana/katakana
- `ime_japonais.py` - Clavier japonais (taper en romaji, obtenir des kana)
- `demo_pykakasi.py` - Lecture des kanji (conversion kanji vers romaji)
- `demo_jamdict.py` - Dictionnaire japonais-anglais (200 000+ mots)
- `traducteur_deepl.py` - Traducteur vers le japonais via API DeepL

## Fonctionnalités

| Option | Outil | Description |
|--------|-------|-------------|
| 1 | Romkan | Convertir romaji en hiragana/katakana et vice versa |
| 2 | IME Japonais | Taper du japonais avec un clavier français |
| 3 | Pykakasi | Lire les kanji (obtenir la prononciation) |
| 4 | Jamdict | Dictionnaire japonais-anglais avec definitions |
| 5 | DeepL | Traduire des phrases en japonais |

## Dépendances
- Python 3.11
- romkan (conversion romaji/kana)
- pykakasi (lecture des kanji)
- jamdict + jamdict-data (dictionnaire japonais)
- requests (appels API)

## Secrets requis
- `DEEPL_API_KEY` - Clé API DeepL (stockée de façon sécurisée)

## Exécution
```bash
python menu.py
```

## Commandes utiles dans les outils
- `:q!` - Revenir au menu principal
- `:h` - Mode hiragana (dans l'IME)
- `:k` - Mode katakana (dans l'IME)
