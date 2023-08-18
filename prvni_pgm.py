print("Dobry den, vyplnte dotaznik")
print()
jmeno = input("zadej jmeno:")
prijmeni = input("zadej prijmeni: ")
print("-----------------------")
vek = int(input("zadej vek:"))
telefon = input("zadej telefon: ")
print("-----------------------")
print("-----------------------")
print("dekuji za vlozena data")
print("-----------------------")
print("Vase jmeno a prijmeni je: " + jmeno, prijmeni + " !")
print("Jste stary :" + str(vek))
print("Soubor bude odeslan na tel. c.:" + telefon + "")
print("-----------------------")
cislo = int(input("zadej cislo int: \n"))  # int - je cele cislo
cislo2 = float(input("zadej cislo float: \n"))  # float - je desetine cislo
print("-----------------------")
print("int je :" + str(cislo))  # +str - je prevede cislo na datovy retezec!!
print("float je :" + str(cislo2))
vysledek = cislo / cislo2
print(vysledek)  # vydledek je float. deleni cisla int/float
print("-----------------------")
if vek == 40:  # vysledek je tip Boolean True / False
    print("ano je ti 40 let")
elif vek == 41:
    print("ano je ti 41 let")
elif vek == 28 and vek == 29:  # and - musi splnovat 28 i 29 pak true
    print("je ti 28 i 29 let")
elif vek == 28 or vek == 29:  # or - musi splnovat bud 28 nebo 29 pak true
    print("je ti 28 nebo 29 let")
else:
    print("neni ti 40 let")
print("---------------------")
chyba = int(0)  # nastaveni promenne pocet chyb je nula
seznamchyb = []
mesto = input("zadej hlavni mesto cr :")  # zadani mesta
while mesto != "praha":  # podminka while :se opakuje tak dlouho nez odpovime spravne
    chyba = chyba + 1  # jestlize se odpoved neshoduje provede prikazy odskocene
    seznamchyb.append(mesto)  # ulozi chybu do seznamu - seznamchyb! pomoci .append
    print("ne to neni hlavni mesto, pocet chyb :" + str(chyba))
    mesto = input("zadej hlavni mesto cr :")  # znovu zadat mesto
print("spravne - chyb bylo:" + str(chyba))
print("---------------------")

anone = input("chces vypsat chyby ano/ne :")
if anone == "ano":  # jestlize odpovime ano
    for tisk in seznamchyb:  # vypise spatne odpovedi
        print(tisk)

print("---------------------")

for hodnota in range(
    1, 10
):  # vypise cisla 1-9 mohu ale zadat i slova "jedna","tri","slon"
    print(hodnota)  # v tomto pripade bude hodnota jednou jedna,tri nekonec slon!

# vytvoreni seznamu
seznam = ["maslo", "cokolada", "bombony", "sadlo"]
neco = seznam[
    1
]  # promene neco priradi prvni hodnotu ze seznamu - cislo v zavorce pozice
for (
    aaa
) in seznam:  # kdyz pouziju -1 priradi posledni. zaporna cisla berou seznam odzadu!
    print("Co mame v lednici :" + aaa)  # tato smycka vypise co mame v lednici
if "sadlo" in seznam:  # tato podminka zjisti zda je sadlo v seznamu
    print("ano je v seznamu!")

# pridani polozky do seznamu "uz pouzito hore" pomoci append "seznam.append("polozka")
# odstraneni polozky pomoci remove "seznam.remove("polozka")" odstrani prvni nalezenou
# v pripade ze je v seznamu vicekrat
# zmena polozky - seznam[cislo polozky v seznamu] = "maslo"
# zjisteni poctu polozek v seznamu

seznam2 = ["maslo", "sadlo", "cokolada", "brambory", "kucup"]  # seznam polozek
pocet = len(seznam2)  # pomoci len ze seznamu2 do promene pocet zjisti pocet polozek
print(pocet)

# vyrezy
slovo = "martin"  # nastaveni promene
cast = slovo[0:3]  # promena cast bude osazene znakem 0,1,2 tedy "mar" zacina nulou
print(cast)  # stejnym zpusobem mohu vytvaret vyrez i ze seznamu

heslo = "123456789"
print(len(heslo))  # zjisti pocet znaku v retezci / heslu

jmeno = "Martin"
print(jmeno.upper())  # vytiskne jmeno ale velkymi pismeny

jmeno_male = jmeno.lower()  # vytvori pronebou j_m z promene jmeno malina pismenama
print(jmeno_male)  # .upper a .lower

jmeno = "Martin"
print("Ahoj " + jmeno + "!")  # napise ahoj martin!  stary zapis
print(f"Ahoj {jmeno}!")  # napise ahoj martin!  novy zapis
