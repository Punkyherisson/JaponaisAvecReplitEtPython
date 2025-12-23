import romkan

print("=" * 50)
print("DÉMONSTRATION DE ROMKAN")
print("=" * 50)

print("\n1. ROMAJI → HIRAGANA")
print("-" * 30)
mots = ["konnichiwa", "arigatou", "sayounara", "ninja", "samurai", "sushi", "tokyo", "osaka"]
for mot in mots:
    print(f"  {mot:15} → {romkan.to_hiragana(mot)}")

print("\n2. ROMAJI → KATAKANA")
print("-" * 30)
mots_katakana = ["koohii", "pasokon", "terebi", "anime", "manga", "ramen"]
for mot in mots_katakana:
    print(f"  {mot:15} → {romkan.to_katakana(mot)}")

print("\n3. HIRAGANA → ROMAJI (style Hepburn)")
print("-" * 30)
hiragana = ["にんじゃ", "さむらい", "すし", "おはよう", "こんにちは"]
for h in hiragana:
    print(f"  {h:10} → {romkan.to_roma(h)}")

print("\n4. KATAKANA → ROMAJI")
print("-" * 30)
katakana = ["コーヒー", "パソコン", "テレビ", "アニメ", "マンガ"]
for k in katakana:
    print(f"  {k:10} → {romkan.to_roma(k)}")

print("\n5. HIRAGANA ↔ KATAKANA")
print("-" * 30)
print("  Hiragana → Katakana:")
test_hira = "ありがとう"
print(f"    {test_hira} → {romkan.to_katakana(romkan.to_roma(test_hira))}")

print("\n  Katakana → Hiragana:")
test_kata = "アリガトウ"
print(f"    {test_kata} → {romkan.to_hiragana(romkan.to_roma(test_kata))}")

print("\n6. ROMANISATION KUNREI vs HEPBURN")
print("-" * 30)
exemples = ["ちゃ", "しゃ", "じゃ", "つ", "ふ"]
print(f"  {'Kana':8} {'Hepburn':12} {'Kunrei':12}")
for ex in exemples:
    hep = romkan.to_hepburn(ex)
    kun = romkan.to_kunrei(ex)
    print(f"  {ex:8} {hep:12} {kun:12}")

print("\n7. PHRASES COMPLÈTES")
print("-" * 30)
phrases = [
    "watashi wa nihongo wo benkyou shiteimasu",
    "hajimemashite douzo yoroshiku",
    "oishii desu ne"
]
for phrase in phrases:
    print(f"  Romaji:   {phrase}")
    print(f"  Hiragana: {romkan.to_hiragana(phrase)}")
    print()

print("=" * 50)
print("FIN DE LA DÉMONSTRATION")
print("=" * 50)
