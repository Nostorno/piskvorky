from data import knihovna
import random


# f: generator_uctu - vygeneruje nahodny ucet z knihovny
def generator_uctu(list_knihovny):
    nahodny_ucet = random.randint(0, 10)
    return list_knihovny[nahodny_ucet]


# f:vypsani - zobrazi informace z uctu 1 a 2
def vypsani(u1, u2):
    print(f"Porovnej A: {u1['name']},{u1['description']},{u1['country']}")
    print(f"Porovnej B: {u2['name']},{u2['description']},{u2['country']}")


# f:hra - hra samotna
def hra():
    ucet_1 = generator_uctu(knihovna)  # nastaveni uctu1 pomoci f: generator uctu
    ucet_2 = generator_uctu(knihovna)
    spravna_odpoved = ""
    score = 0
    pokracovat = True

    while pokracovat:
        vypsani(ucet_1, ucet_2)
        odpoved = input("Kdo ma vice sledujicich na instagramu? A nebo B. ")
        if ucet_1["follower_count"] > ucet_2["follower_count"]:
            spravna_odpoved = "A"
            ucet_1 = ucet_2
        else:
            spravna_odpoved = "B"
            ucet_1 = ucet_2

        if odpoved == spravna_odpoved:
            score += 1
            print(f"Spravne! Vase score je {score}")
            ucet_2 = generator_uctu(knihovna)
        else:
            print(f"To je spatne. Tve score je {score}")
            pokracovat = False


hra()
