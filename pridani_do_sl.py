denik_cest = [
    {
        "zeme": "ceska republika",
        "mesta": [
            "praha",
            "brno",
            "plzen",
            "kemenice",
        ],
        "navstev": 5,
    },
    {
        "zeme": "recko",
        "mesta": ["lefkada", "thassos", "kefalonie", "korfu"],
        "navstev": 6,
    },
]

print("vypln formular !")
zeme = input("zadej dalsi zemi :")
mesto = input("zadej mesta a oddeluj carkou :")
navstev = input("zadej pocet navstev :")


def pridani_polozky(zeme, mesto, navsev):
    nova_slozka = {}
    nova_slozka["zeme"] = zeme
    nova_slozka["mesta"] = mesto
    nova_slozka["navsev"] = navsev
    denik_cest.append(nova_slozka)


pridani_polozky(zeme, mesto, navstev)

print(denik_cest)
