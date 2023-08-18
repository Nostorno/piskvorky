import random

pismena_seznam = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "y",
    "x",
    "z",
]
cisla_seznam = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
znaky_seznam = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "~",
    "?",
]

cisla = int(input("kolik chces cislel v heslu :"))
pismena = int(input("kolik chces pismen v hesllu :"))
znaky = int(input("kolik chces znaku :"))

heslo = 0
heslo_seznam = []
final_seznam = []

for aaa in range(cisla):
    promena_cislo = random.choice(cisla_seznam)
    heslo_seznam.append(promena_cislo)

for bbb in range(pismena):
    promena_pismena = random.choice(pismena_seznam)
    heslo_seznam.append(promena_pismena)

for ccc in range(znaky):
    promena_znak = random.choice(znaky_seznam)
    heslo_seznam.append(promena_znak)

pocet_znaku = len(heslo_seznam)

for ddd in range(pocet_znaku):
    hodnota2 = random.choice(heslo_seznam)
    heslo_seznam.remove(hodnota2)
    final_seznam.append(hodnota2)

# random.shuffle(final_seznam)  .... shuffle zamicha obsahem

print(final_seznam)

konec = ""
for eee in final_seznam:
    konec = konec + eee

print(konec)
