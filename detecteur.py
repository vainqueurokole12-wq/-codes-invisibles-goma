# Projet par OKOLE NTWALI VAINQUEUR - Goma
# Detecteur de codes invisibles

def detecter_codes_caches(texte):
    print("Analyse par VAINQUEUR de Goma...")
    trouves = []
    for i, c in enumerate(texte):
        if ord(c) < 32 or ord(c) > 126:
            trouves.append((i, ord(c)))
    if trouves:
        print(f"{len(trouves)} codes invisibles trouves!")
        for pos, code in trouves:
            print(f"Position {pos}: code {code}")
    else:
        print("Aucun code invisible")
    return trouves

if __name__ == "__main__":
    detecter_codes_caches("Bonjour Goma")
