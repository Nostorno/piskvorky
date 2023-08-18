import os  # import funkce os - os.system("cls") vycisti obrzovku

os.system("cls")

seznam = {}
max = ""
vyherce = ""
dalsi = "ano"

print("toto je ticha aukce")
print("-------------------")


def ulozeni():  # def - vlozi data do slovniku a preda promenou dalsi
    jmeno = input("zadej jmeno :")
    cena = input("kolik das $ :")
    dalsi = input("nekdo dalsi ano/ne :")
    seznam[jmeno] = cena
    return dalsi


while dalsi == "ano":  # kdyz ano dalsi prihazujici
    dalsi = ulozeni()
    os.system("cls")

for aaa in seznam:  # najde nejvyssi sumu
    if seznam[aaa] > max:
        max = seznam[aaa]
        vyherce = aaa

print("aukci vyhral pan: " + (vyherce) + " s cenou :" + (seznam[vyherce]) + "$")
