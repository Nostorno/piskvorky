import random

spatne = 0
spravne = 0
seznam = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

pocet = int(input("zadej pocet prikladu:"))

for priklad in range(pocet):
    prvni = random.choice(seznam)
    if prvni <= 10:
        znamenko = "+"
    else:
        znamenko = "-"

    druhe = random.choice(seznam)

    if znamenko == "+":
        test = prvni + druhe
        while test > 20:
            prvni = random.choice(seznam)
            druhe = random.choice(seznam)
            test = prvni + druhe

        vysledek = int(
            input("spocitej priklad: " + str(prvni) + "+" + str(druhe) + "=")
        )

    elif znamenko == "-":
        test = prvni - druhe
        while test < 1:
            prvni = random.choice(seznam)
            druhe = random.choice(seznam)
            test = prvni - druhe

        vysledek = int(
            input("spocitej priklad: " + str(prvni) + "-" + str(druhe) + "=")
        )

    if test == vysledek:
        spravne = spravne + 1
        print("spravne")
    else:
        spatne = spatne + 1
        print("spatne")

print("spravne bylo :" + str(spravne))
print("spatne bylo :" + str(spatne))

dopocet = round((100 / pocet) * spravne)

if dopocet >= 95 and dopocet <= 100:
    print("tva znamka je 1")
elif dopocet >= 85 and dopocet <= 94:
    print("tva znamka je 1-")
elif dopocet >= 75 and dopocet <= 84:
    print("tva znamka je 2")
elif dopocet >= 65 and dopocet <= 75:
    print("tva znamka je 2-")
elif dopocet >= 55 and dopocet <= 64:
    print("tva znamka je 3")
elif dopocet >= 45 and dopocet <= 54:
    print("tva znamka je 3-")
elif dopocet >= 35 and dopocet <= 44:
    print("tva znamka je 4")
elif dopocet >= 25 and dopocet <= 34:
    print("tva znamka je 4-")
elif dopocet >= 15 and dopocet <= 24:
    print("tva znamka je 5")
