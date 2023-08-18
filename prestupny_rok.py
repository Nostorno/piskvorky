rok = int(input("zadej rok :"))

if rok % 4 == 0 and rok % 100 > 0 and rok % 100 < 0:
    print("toto je prestupny rok")
elif rok % 4 == 0 and rok % 100 == 0 and rok % 400 == 0:
    print("toto je prestupny rok")
else:
    print("toto neni prestupny rok")
