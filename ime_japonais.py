import romkan

class IMEJaponais:
    """Simulateur d'IME japonais - tape lettre par lettre comme sur un vrai clavier"""
    
    ROMAJI_PATTERNS = [
        'kya', 'kyu', 'kyo', 'sha', 'shu', 'sho', 'cha', 'chu', 'cho',
        'nya', 'nyu', 'nyo', 'hya', 'hyu', 'hyo', 'mya', 'myu', 'myo',
        'rya', 'ryu', 'ryo', 'gya', 'gyu', 'gyo', 'ja', 'ju', 'jo',
        'bya', 'byu', 'byo', 'pya', 'pyu', 'pyo',
        'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'si', 'su', 'se', 'so',
        'ta', 'ti', 'tu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no',
        'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo',
        'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo',
        'ga', 'gi', 'gu', 'ge', 'go', 'za', 'zi', 'zu', 'ze', 'zo',
        'da', 'di', 'du', 'de', 'do', 'ba', 'bi', 'bu', 'be', 'bo',
        'pa', 'pi', 'pu', 'pe', 'po', 'shi', 'chi', 'tsu',
        'a', 'i', 'u', 'e', 'o', 'n'
    ]
    
    def __init__(self):
        self.buffer = ""
        self.output = ""
    
    def peut_etre_complete(self, texte):
        """Vérifie si le texte pourrait devenir un pattern valide"""
        for pattern in self.ROMAJI_PATTERNS:
            if pattern.startswith(texte):
                return True
        return False
    
    def est_pattern_complet(self, texte):
        """Vérifie si le texte est un pattern romaji complet"""
        return texte in self.ROMAJI_PATTERNS
    
    def traiter_touche(self, char):
        """Traite une touche tapée et retourne l'état actuel"""
        char = char.lower()
        
        if char == ' ':
            if self.buffer:
                try:
                    self.output += romkan.to_hiragana(self.buffer)
                except:
                    self.output += self.buffer
                self.buffer = ""
            self.output += " "
            return self.output, ""
        
        nouveau_buffer = self.buffer + char
        
        if self.est_pattern_complet(nouveau_buffer):
            hiragana = romkan.to_hiragana(nouveau_buffer)
            self.output += hiragana
            self.buffer = ""
            return self.output, ""
        
        elif self.peut_etre_complete(nouveau_buffer):
            self.buffer = nouveau_buffer
            return self.output, self.buffer
        
        else:
            if self.buffer:
                if self.buffer == 'n' and char not in 'aiueoy':
                    self.output += 'ん'
                    self.buffer = char if self.peut_etre_complete(char) else ""
                    if not self.peut_etre_complete(char):
                        self.output += char
                else:
                    try:
                        self.output += romkan.to_hiragana(self.buffer)
                    except:
                        self.output += self.buffer
                    self.buffer = char if self.peut_etre_complete(char) else ""
                    if not self.peut_etre_complete(char):
                        self.output += char
            else:
                self.buffer = char if self.peut_etre_complete(char) else ""
                if not self.peut_etre_complete(char):
                    self.output += char
            
            return self.output, self.buffer
    
    def finaliser(self):
        """Finalise la conversion du buffer restant"""
        if self.buffer:
            try:
                self.output += romkan.to_hiragana(self.buffer)
            except:
                self.output += self.buffer
            self.buffer = ""
        return self.output
    
    def reset(self):
        """Remet à zéro l'IME"""
        self.buffer = ""
        self.output = ""


def demo_ime():
    """Démonstration de l'IME lettre par lettre"""
    print("=" * 60)
    print("DÉMONSTRATION IME JAPONAIS - Frappe lettre par lettre")
    print("=" * 60)
    
    exemples = [
        "konnichiwa",
        "arigatou",
        "nihongo",
        "samurai",
        "sushi"
    ]
    
    for mot in exemples:
        print(f"\nMot: {mot}")
        print("-" * 40)
        ime = IMEJaponais()
        
        for i, char in enumerate(mot):
            sortie, buffer = ime.traiter_touche(char)
            buffer_display = f"[{buffer}]" if buffer else ""
            print(f"  Touche '{char}' → {sortie}{buffer_display}")
        
        resultat_final = ime.finaliser()
        print(f"  Résultat final: {resultat_final}")


def mode_interactif():
    """Mode interactif où l'utilisateur tape"""
    print("\n" + "=" * 60)
    print("MODE INTERACTIF - Tapez du romaji (Entrée pour valider, 'q' pour quitter)")
    print("=" * 60)
    print("\nGuide de frappe avec clavier français/européen:")
    print("  a, i, u, e, o → あ, い, う, え, お")
    print("  ka, ki, ku, ke, ko → か, き, く, け, こ")
    print("  sa, shi, su, se, so → さ, し, す, せ, そ")
    print("  ta, chi, tsu, te, to → た, ち, つ, て, と")
    print("  na, ni, nu, ne, no → な, に, ぬ, ね, の")
    print("  ha, hi, fu, he, ho → は, ひ, ふ, へ, ほ")
    print("  ma, mi, mu, me, mo → ま, み, む, め, も")
    print("  ya, yu, yo → や, ゆ, よ")
    print("  ra, ri, ru, re, ro → ら, り, る, れ, ろ")
    print("  wa, wo, n → わ, を, ん")
    print("\nAstuce: Pour 'ん', tapez 'nn' ou 'n' suivi d'une consonne")
    print("-" * 60)
    
    while True:
        texte = input("\nEntrez du romaji: ").strip()
        if texte.lower() == 'q':
            print("Au revoir!")
            break
        
        if not texte:
            continue
        
        ime = IMEJaponais()
        print("\nConversion lettre par lettre:")
        
        for char in texte:
            sortie, buffer = ime.traiter_touche(char)
            buffer_display = f" [buffer: {buffer}]" if buffer else ""
            print(f"  '{char}' → {sortie}{buffer_display}")
        
        resultat = ime.finaliser()
        print(f"\n  Résultat: {resultat}")
        print(f"  Katakana: {romkan.to_katakana(texte)}")


if __name__ == "__main__":
    demo_ime()
    mode_interactif()
