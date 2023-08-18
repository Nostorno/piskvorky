# stupnice
# 91 - 100 = "excelentni"
# 81 - 90 = "vynikajici"
# 71 - 80 = "splneno"
# mene jak  71 = "nesplneno"

studenti = {
    "Martin": 85,
    "Marta": 71,
    "Nikolka": 98,
    "Sofinka": 69,
    "Petr": 88,
    "Marketa": 79,
    "Bobr": 49,
}

hodnoceni = {}

# vytvori new slovnik a priradi hodnoceni
for klic in studenti:
    aaa = studenti[klic]
    if aaa < 71:
        hodnoceni[klic] = "nesplneno"
    elif aaa > 70 and aaa < 81:
        hodnoceni[klic] = "splneno"
    elif aaa > 80 and aaa < 91:
        hodnoceni[klic] = "vynikajici"
    elif aaa > 90:
        hodnoceni[klic] = "excelentni"

print(hodnoceni)

# vypise new slovnik s hodnocenim a body z puvodniho sl.
for klic in hodnoceni:
    print(klic + " " + hodnoceni[klic] + " " + str(studenti[klic]))

# vypise slovni a seradi od nejlepsi po nejhorsi

sl_serazeny = {}

for bbb in range(100, -1, -1):
    for ccc in studenti:
        if studenti[ccc] == bbb:
            sl_serazeny[ccc] = +int(bbb)

for ddd in sl_serazeny:
    print(str(sl_serazeny[ddd]) + "-" + (ddd))
