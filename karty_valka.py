# popis - program vytvori balicek karet s cislem 1-20, tyto karty rozdeli pro dva hrace. pote kazdy hrac vylozi jednu kartu a vyssi bere.
# vyhrava ten kdo ma vsechny karty. smycka while - omezeno podminkou na 5000 kol

import random

vyhra = "ne"
pokus = 0
balicek_karet = [cislo for cislo in range(1, 21)]
hrac1_balicek = []
hrac2_balicek = []

for rozdeleni in range(1, 11):
    hodnota1 = random.choice(balicek_karet)
    balicek_karet.remove(hodnota1)
    hrac1_balicek.append(hodnota1)

    hodnota2 = random.choice(balicek_karet)
    balicek_karet.remove(hodnota2)
    hrac2_balicek.append(hodnota2)
    print(balicek_karet)

while vyhra != "ano":
    karta_hrac1 = hrac1_balicek[0]
    hrac1_balicek.remove(karta_hrac1)
    karta_hrac2 = hrac2_balicek[0]
    hrac2_balicek.remove(karta_hrac2)

    if karta_hrac1 > karta_hrac2:
        hrac1_balicek.append(karta_hrac1)
        hrac1_balicek.append(karta_hrac2)
    else:
        hrac2_balicek.append(karta_hrac1)
        hrac2_balicek.append(karta_hrac2)

    pocet_karet1 = len(hrac1_balicek)
    pocet_karet2 = len(hrac2_balicek)

    if pocet_karet1 == 0:
        vyhra = "ano"
    if pocet_karet2 == 0:
        vyhra = "ano"
    pokus = pokus + 1
    print(hrac1_balicek)
    print(hrac2_balicek)
    print(pocet_karet1)
    print(pocet_karet2)
    if pokus > 5000:
        vyhra = "ano"
