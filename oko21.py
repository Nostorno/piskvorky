import random

seznam_barvy = ["srdce", "piky", "krize", "listy"]
seznam_znaky = ["spodek", "dama", "kral", "eso"]
balicek_karet = []
balicek_hrac1 = []
balicek_hrac2 = []
suma1 = 0
pocet_karet1 = 0
suma2 = 0
pocet_karet2 = 0


def karta(balicek_karet, pocet_karet1, suma1):
    hodnota1 = random.choice(balicek_karet)
    balicek_karet.remove(hodnota1)
    balicek_hrac1.append(hodnota1)
    pocet_karet1 = len(balicek_hrac1)

    for karta in [balicek_hrac1[-1]]:
        if "7" in karta:
            suma1 = suma1 + 7
        if "8" in karta:
            suma1 = suma1 + 8
        if "9" in karta:
            suma1 = suma1 + 9
        if "10" in karta:
            suma1 = suma1 + 10
        if "spodek" in karta:
            suma1 = suma1 + 1
        if "dama" in karta:
            suma1 = suma1 + 1
        if "kral" in karta:
            suma1 = suma1 + 1
        if "eso" in karta:
            suma1 = suma1 + 11
    return balicek_karet, pocet_karet1, suma1


def pocitac(balicek_karet, pocet_karet2, suma2):
    hodnota2 = random.choice(balicek_karet)
    balicek_karet.remove(hodnota2)
    balicek_hrac2.append(hodnota2)
    pocet_karet2 = len(balicek_hrac2)

    for karta in [balicek_hrac2[-1]]:
        if "7" in karta:
            suma2 = suma2 + 7
        if "8" in karta:
            suma2 = suma2 + 8
        if "9" in karta:
            suma2 = suma2 + 9
        if "10" in karta:
            suma2 = suma2 + 10
        if "spodek" in karta:
            suma2 = suma2 + 1
        if "dama" in karta:
            suma2 = suma2 + 1
        if "kral" in karta:
            suma2 = suma2 + 1
        if "eso" in karta:
            suma2 = suma2 + 11
    return balicek_karet, pocet_karet2, suma2


def tisk():
    print("tvuj balicek obsahuje:" + str(balicek_hrac1))
    print("karet mas :" + str(pocet_karet1))
    print("hodnota karet je :" + str(suma1))


for karta_barva in seznam_barvy:
    for karta_cislo in range(7, 11):
        nova_karta = karta_barva + "_" + str(karta_cislo)
        balicek_karet.append(nova_karta)

    for karta_znak in seznam_znaky:
        nova_karta = karta_barva + "_" + karta_znak
        balicek_karet.append(nova_karta)

print("Hra zacina - dostanes prvni kartu")

balicek_karet, pocet_karet1, suma1 = karta(balicek_karet, pocet_karet1, suma1)
tisk()

dalsi_karta = input("chces dalsi kartu y/n:")

while dalsi_karta != "n":
    balicek_karet, pocet_karet1, suma1 = karta(balicek_karet, pocet_karet1, suma1)
    tisk()
    if suma1 == 22 and pocet_karet1 == 2:
        print("mas kralovske oko")
        print("bede hrat pocitac")
        dalsi_karta = "n"
    if suma1 > 21:
        dalsi_karta = "n"
        print("prohral jsi - mas vic jak 21")
    else:
        dalsi_karta = input("chces dalsi kartu y/n:")

print("tvuj vysledek je :" + str(suma1))
print()
print("ted zacne hrat pocitac")

balicek_karet, pocet_karet2, suma2 = pocitac(balicek_karet, pocet_karet2, suma2)

while suma2 < 19:
    balicek_karet, pocet_karet2, suma2 = pocitac(balicek_karet, pocet_karet2, suma2)

print("pocitac ma karty:" + str(balicek_hrac2))
print("hodnota karet je :" + str(suma2))
print("-------------------------------------------------------------")
if suma2 == 22 and pocet_karet2 == 2:
    print("vyhral pocitac - kralovske oko!!")
elif suma2 <= 21 and suma1 > 21:
    print("vyhral pocitac :" + str(suma2) + "/" + str(suma1))
elif suma1 == suma2:
    print("remiza - pomerem :" + str(suma1) + "/" + str(suma2))
elif suma1 <= 21 and suma2 > 21:
    print("vyhral jis! :" + str(suma1) + "/" + str(suma2))
elif suma1 > 21 and suma2 > 21:
    print("nikdo nevyhral - vysledek :" + str(suma1) + "/" + str(suma2))
elif suma1 > suma2:
    print("vyhral jsi! :" + str(suma1) + "/" + str(suma2))
elif suma2 > suma1:
    print("vyhral pocitac" + str(suma2) + "/" + str(suma1))
