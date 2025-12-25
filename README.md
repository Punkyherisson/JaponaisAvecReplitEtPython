# Faire du Japonais avec Replit et Python

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Made with Replit](https://img.shields.io/badge/Made%20with-Replit-orange.svg)](https://replit.com)

Une suite complète d'outils Python pour apprendre et pratiquer le japonais. Conversion romaji-kana, lecture des kanji, dictionnaire japonais-anglais et traduction automatique.

![Demo](https://img.shields.io/badge/Demo-Try%20on%20Replit-blueviolet)

---

## Fonctionnalités

| Outil | Description |
|-------|-------------|
| **Romkan** | Convertir romaji ↔ hiragana/katakana |
| **IME Japonais** | Taper du japonais avec un clavier français |
| **Pykakasi** | Obtenir la lecture (pronunciation) des kanji |
| **Jamdict** | Dictionnaire japonais-anglais (200 000+ mots) |
| **DeepL** | Traduire des phrases en japonais |
| **Lecteur** | Écouter du texte japonais (text-to-speech) |

---

## Installation

### Option 1 : Sur Replit (recommandé)

1. Forkez ce projet sur Replit
2. Ajoutez votre clé API DeepL dans les Secrets (optionnel)
3. Cliquez sur "Run"

### Option 2 : Installation locale

```bash
# Cloner le dépôt
git clone https://github.com/Punkyherisson/JaponaisAvecReplitEtPython.git
cd JaponaisAvecReplitEtPython

# Installer les dépendances
pip install -r requirements.txt

# Lancer le menu
python menu.py
```

---

## Utilisation

Lancez le menu principal :

```bash
python menu.py
```

Vous verrez :

```
=======================================================
   FAIRE DU JAPONAIS AVEC REPLIT ET PYTHON
=======================================================

  1. Demo Romkan (conversions romaji/kana)
  2. IME Japonais (clavier japonais)
  3. Pykakasi (lecture des kanji)
  4. Jamdict (dictionnaire japonais)
  5. Traducteur DeepL (traduction vers japonais)
  6. Lecteur japonais (text-to-speech)
  7. Quitter
```

### Commandes universelles

- `:q!` - Revenir au menu principal (dans tous les outils)
- `:h` - Mode hiragana (dans l'IME)
- `:k` - Mode katakana (dans l'IME)

---

## Exemples de code

### Conversion Romaji → Kana avec Romkan

```python
import romkan

# Romaji vers Hiragana
print(romkan.to_hiragana("konnichiwa"))  # こんにちは
print(romkan.to_hiragana("arigatou"))    # ありがとう

# Romaji vers Katakana
print(romkan.to_katakana("koohii"))      # コーヒー
print(romkan.to_katakana("anime"))       # アニメ

# Kana vers Romaji
print(romkan.to_roma("にんじゃ"))         # ninja
print(romkan.to_roma("すし"))             # sushi
```

### Lecture des Kanji avec Pykakasi

```python
import pykakasi

kks = pykakasi.kakasi()
result = kks.convert("東京に行きたい")

for item in result:
    print(f"{item['orig']} → {item['hira']} ({item['hepburn']})")

# 東京 → とうきょう (toukyou)
# に → に (ni)
# 行きたい → いきたい (ikitai)
```

### Dictionnaire avec Jamdict

```python
from jamdict import Jamdict

jam = Jamdict()
result = jam.lookup("食べる")

for entry in result.entries:
    print(f"Mot: {entry.kanji_forms[0]} ({entry.kana_forms[0]})")
    for sense in entry.senses:
        print(f"  - {', '.join(str(g) for g in sense.gloss)}")

# Mot: 食べる (たべる)
#   - to eat
```

### Text-to-Speech avec gTTS

```python
from gtts import gTTS

# Créer un fichier audio à partir de texte japonais
tts = gTTS("こんにちは、今日はいい天気ですね", lang="ja")
tts.save("bonjour.mp3")

# Le fichier MP3 peut être téléchargé et écouté
```

### Adaptation des noms européens

Le projet inclut une fonction pour adapter les noms européens au système phonétique japonais :

```python
# Exemples d'adaptation automatique
"Philippe" → "firippu" → フィリップ
"William"  → "uiriamu" → ウィリアム
"Camille"  → "kamiru"  → カミル
```

---

## Configuration API DeepL

Pour utiliser le traducteur DeepL :

1. Créez un compte gratuit sur [DeepL API](https://www.deepl.com/pro-api)
2. Récupérez votre clé API
3. Sur Replit : ajoutez-la dans **Secrets** avec le nom `DEEPL_API_KEY`
4. En local : créez un fichier `.env` avec `DEEPL_API_KEY=votre_clé`

---

## Dépendances

| Package | Version | Description |
|---------|---------|-------------|
| `romkan` | >= 0.2.1 | Conversion romaji ↔ kana |
| `pykakasi` | >= 2.2.1 | Lecture des kanji |
| `jamdict` | >= 0.1a11 | Interface dictionnaire JMdict |
| `jamdict-data` | >= 1.5 | Données JMdict (200k+ entrées) |
| `requests` | >= 2.28 | Appels API HTTP |
| `gtts` | >= 2.5.0 | Google Text-to-Speech |

---

## Structure du projet

```
├── menu.py              # Menu principal (point d'entrée)
├── demo_romkan.py       # Conversion romaji/kana
├── ime_japonais.py      # Clavier japonais interactif
├── demo_pykakasi.py     # Lecture des kanji
├── demo_jamdict.py      # Dictionnaire japonais
├── traducteur_deepl.py  # Traduction via API DeepL
├── lecteur_japonais.py  # Text-to-speech avec gTTS
├── audio_japonais/      # Fichiers audio générés
├── requirements.txt     # Dépendances Python
└── README.md            # Ce fichier
```

---

## Ressources pour apprendre le japonais

- [Minna no Nihongo](https://www.3anet.co.jp/np/en/books/2300/) - Manuel de référence
- [Jisho.org](https://jisho.org/) - Dictionnaire en ligne
- [WaniKani](https://www.wanikani.com/) - Apprentissage des kanji
- [Tae Kim's Guide](https://guidetojapanese.org/) - Grammaire japonaise

---

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout de fonctionnalité'`)
4. Push la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

---

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Auteur

Créé avec passion pour l'apprentissage du japonais.

頑張って！ (Ganbatte! - Bon courage !)
