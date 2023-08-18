hodnota = 0
pocet = 0
vysky = input("zadej vysky oddeluj carkou :")  # promena vysky
seznam_vysky = vysky.split(",")  # vytvori seznam z promene pomoci split
print(seznam_vysky)
pocet = len(seznam_vysky)  # pocet v seznamu
for aaa in seznam_vysky:  # cykl tolikrat kolik je polozek v seznamu
    hodnota = hodnota + int(aaa)  # scita polozky ze seznamu
prumer = hodnota / pocet  # vydeli poctem polozek v seznamu
print("prumerna vyska je: " + str(prumer))
