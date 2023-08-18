pocet_delitelnosti = 0

print("tento program vyhodnoti zadane cislo zda je to prvcislo")
number = int(input("zadej cislo:"))

for aaa in range(1, number + 1):  # cyklus probehne od 1 do zadaneho cisla + 1
    if number % aaa == 0:  # podminka zda zadane cislo je delitelne hodnotou z cyklu
        pocet_delitelnosti = (
            pocet_delitelnosti + 1
        )  # jestlize ano prida k delitelnosti 1

if pocet_delitelnosti == 2:
    print("toto cislo je prvoscilo")
else:
    print("toto cislo neni prvcislo a je delitelne: " + str(pocet_delitelnosti) + "X")
