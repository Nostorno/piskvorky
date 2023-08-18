slovnik = [
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

slovo = input("zadej text ke kodovani :")
posunuti = int(input("o kolik znaku posunout :"))
sifra = ""
xxx = 0

for a in range(len(slovo)):  # tolikrat kolik je v zadanem slove pismen
    for b in range(0, 26):  # pro kazde znak ve slovniku
        if slovo[a] == slovnik[b]:  # znak slova je stejny se znakem ze slovniku
            if b + posunuti > 25:  # posunuti nedostaneme ze slovniku
                xxx = (
                    b + posunuti
                ) - 26  # ano - (pozice ve slovniku + posunuti) - 26 : zacina znovu na zacatku
                sifra = sifra + slovnik[xxx]  # zapise pismeno do sifry
            else:  # ne - neni posunuto mimo slovnik
                sifra = (
                    sifra + slovnik[b + posunuti]
                )  # muze zapsat do sifry bez dopoctu posunuti
print(sifra)

eee = "j"
pokus = slovnik.index(
    eee
)  # index najde pismeno j ve slovniku a ulozi pozici do promene pokus
print(pokus)
