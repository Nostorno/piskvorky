import os, random

os.system("cls")

hraci_pole_cele = []
hraci_pole_hodnoty = []
vyherce = ""
jedna_kombinace = ""
kombinace = []
start = "ano"
nyni_pocitac = 1
nyni_hrac = 0
hrac_posledni = 0
hrac_posledni2 = 0
nyni_posledni = 0
nenalezeno = 0
suoradnice_hrace = 0
tahy_hrace = []
vhodna_finalni = 0

for cislo in range(1, 11):
    rada = ["⬜️"] * 10
    hraci_pole_cele.append(rada)


for cislo in range(1, 11):
    rada = ["n"] * 10
    hraci_pole_hodnoty.append(rada)


def vykresleni_pole():
    for aaa in range(0, 10):
        for bbb in range(0, 10):
            if bbb < 9:
                print(hraci_pole_cele[aaa][bbb], end="")
            elif bbb == 9:
                print(hraci_pole_cele[aaa][bbb])


def vykresleni_hodnoty():
    for aaa in range(0, 10):
        for bbb in range(0, 10):
            if bbb < 9:
                print(hraci_pole_hodnoty[aaa][bbb], end="")
            elif bbb == 9:
                print(hraci_pole_hodnoty[aaa][bbb])


def pc_hrac():
    global posledni_hrac, souradnice_hrace, posledni_hrac2, nyni_hrac
    posledni_hrac2 = nyni_hrac
    if nyni_hrac >= 1:
        for fff in range(1, 250):
            pc_x = random.randint(0, 9)
            pc_y = random.randint(0, 9)
            pc_tah = hraci_pole_hodnoty[pc_y][pc_x]
            if pc_tah == "n":
                hraci_pole_hodnoty[pc_y][pc_x] = "z"
                vyhodnoceni()
                hraci_pole_hodnoty[pc_y][pc_x] = "n"
                if nyni_hrac > posledni_hrac2:
                    souradnice_hrace = str(pc_x) + str(pc_y)
                    print(pc_x, pc_y)
                    tahy_hrace.append(souradnice_hrace)

            nyni_hrac = posledni_hrac2
            print(tahy_hrace, nyni_hrac, posledni_hrac2)


def pocitac():
    global start, nyni_posledni, nenalezeno, nyni_pocitac, vhodna_finalni
    pocitac_odehral = "ne"
    nyni_posledni = nyni_pocitac
    while pocitac_odehral != "ano":
        if start == "ano":
            pc_x = random.randint(4, 5)
            pc_y = random.randint(4, 5)
            start = "ne"
            hraci_pole_cele[pc_y][pc_x] = "🟥"
            hraci_pole_hodnoty[pc_y][pc_x] = "c"
            pocitac_odehral = "ano"
            os.system("cls")
            vykresleni_hodnoty()
            print("hodnoty")
            vykresleni_pole()
            pocitac_odehral = "ano"

        else:
            pc_x = random.randint(0, 9)
            pc_y = random.randint(0, 9)
            vhodna_finalni = str(pc_x) + str(pc_y)
            pc_tah = hraci_pole_hodnoty[pc_y][pc_x]
            if pc_tah == "n":
                hraci_pole_cele[pc_y][pc_x] = "🟥"
                hraci_pole_hodnoty[pc_y][pc_x] = "c"
                print(kombinace, nenalezeno, nyni_pocitac, nyni_posledni, nyni_hrac)
                vyhodnoceni()

                if nyni_pocitac > nyni_posledni:
                    nyni_pocitac = nyni_pocitac - 1
                    if nenalezeno < 750:
                        if vhodna_finalni in tahy_hrace:
                            pocitac_odehral = "ano"
                            nenalezeno = 0
                            os.system("cls")
                            vykresleni_hodnoty()
                            print("hodnoty")
                            vykresleni_pole()

                        else:
                            pocitac_odehral = "ano"
                            nenalezeno = 0
                            os.system("cls")
                            vykresleni_hodnoty()
                            print("hodnoty")
                            vykresleni_pole()

                else:
                    hraci_pole_cele[pc_y][pc_x] = "⬜️"
                    hraci_pole_hodnoty[pc_y][pc_x] = "n"
                    nenalezeno = nenalezeno + 1
                    if nenalezeno > 1000:
                        nenalezeno = 0
                        nyni_pocitac = nyni_pocitac - 1
                        nyni_posledni = nyni_pocitac
                        pocitac_odehral = "ne"
            else:
                pocitac_odehral = "ne"
    return


def hrac():
    nevhodne_souradnice = "ano"
    while nevhodne_souradnice != "ne":
        pozicexy = input("zadej souradnice xy :")
        if len(pozicexy) != 2:
            os.system("cls")
            vykresleni_pole()
            print("hodnota neobsahuje dve osy! hraj znovu! " + str(pozicexy))
            nevhodne_souradnice = "ano"
        else:
            nevhodne_souradnice = "ne"
    x = int(pozicexy[0])
    y = int(pozicexy[1])
    tah = hraci_pole_hodnoty[y][x]
    if tah == "n":
        hraci_pole_cele[y][x] = "🟩"
        hraci_pole_hodnoty[y][x] = "z"
        vykresleni_pole()
    elif tah == "z" or tah == "c":
        vykresleni_pole()
        print("policko uz je obsazene! hraj znovu!")
        hrac()
    return


def vyhodnoceni():
    kombinace = []
    global vyherce, nyni_pocitac, nyni_hrac, hrac_posledni
    for ccc in range(0, 10):
        jedna_kombinace = "".join(hraci_pole_hodnoty[ccc][0:10])
        jedna_kombinace = "x" + jedna_kombinace + "x"
        kombinace.append(jedna_kombinace)
    for ddd in range(0, 10):
        jedna_kombinace = "".join([seznam[ddd] for seznam in hraci_pole_hodnoty])
        jedna_kombinace = "x" + jedna_kombinace + "x"
        kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[4][0]
        + hraci_pole_hodnoty[3][1]
        + hraci_pole_hodnoty[2][2]
        + hraci_pole_hodnoty[1][3]
        + hraci_pole_hodnoty[0][4]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[5][0]
        + hraci_pole_hodnoty[4][1]
        + hraci_pole_hodnoty[3][2]
        + hraci_pole_hodnoty[2][3]
        + hraci_pole_hodnoty[1][4]
        + hraci_pole_hodnoty[0][5]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[6][0]
        + hraci_pole_hodnoty[5][1]
        + hraci_pole_hodnoty[4][2]
        + hraci_pole_hodnoty[3][3]
        + hraci_pole_hodnoty[2][4]
        + hraci_pole_hodnoty[1][5]
        + hraci_pole_hodnoty[0][6]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[7][0]
        + hraci_pole_hodnoty[6][1]
        + hraci_pole_hodnoty[5][2]
        + hraci_pole_hodnoty[4][3]
        + hraci_pole_hodnoty[3][4]
        + hraci_pole_hodnoty[2][5]
        + hraci_pole_hodnoty[1][6]
        + hraci_pole_hodnoty[0][7]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[8][0]
        + hraci_pole_hodnoty[7][1]
        + hraci_pole_hodnoty[6][2]
        + hraci_pole_hodnoty[5][3]
        + hraci_pole_hodnoty[4][4]
        + hraci_pole_hodnoty[3][5]
        + hraci_pole_hodnoty[2][6]
        + hraci_pole_hodnoty[1][7]
        + hraci_pole_hodnoty[0][8]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[9][0]
        + hraci_pole_hodnoty[8][1]
        + hraci_pole_hodnoty[7][2]
        + hraci_pole_hodnoty[6][3]
        + hraci_pole_hodnoty[5][4]
        + hraci_pole_hodnoty[4][5]
        + hraci_pole_hodnoty[3][6]
        + hraci_pole_hodnoty[2][7]
        + hraci_pole_hodnoty[1][8]
        + hraci_pole_hodnoty[0][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[9][1]
        + hraci_pole_hodnoty[8][2]
        + hraci_pole_hodnoty[7][3]
        + hraci_pole_hodnoty[6][4]
        + hraci_pole_hodnoty[5][5]
        + hraci_pole_hodnoty[4][6]
        + hraci_pole_hodnoty[3][7]
        + hraci_pole_hodnoty[2][8]
        + hraci_pole_hodnoty[1][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[9][2]
        + hraci_pole_hodnoty[8][3]
        + hraci_pole_hodnoty[7][4]
        + hraci_pole_hodnoty[6][5]
        + hraci_pole_hodnoty[5][6]
        + hraci_pole_hodnoty[4][7]
        + hraci_pole_hodnoty[3][8]
        + hraci_pole_hodnoty[2][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[9][3]
        + hraci_pole_hodnoty[8][4]
        + hraci_pole_hodnoty[7][5]
        + hraci_pole_hodnoty[6][6]
        + hraci_pole_hodnoty[5][7]
        + hraci_pole_hodnoty[4][8]
        + hraci_pole_hodnoty[3][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[9][4]
        + hraci_pole_hodnoty[8][5]
        + hraci_pole_hodnoty[7][6]
        + hraci_pole_hodnoty[6][7]
        + hraci_pole_hodnoty[5][8]
        + hraci_pole_hodnoty[4][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[9][5]
        + hraci_pole_hodnoty[8][6]
        + hraci_pole_hodnoty[7][7]
        + hraci_pole_hodnoty[6][8]
        + hraci_pole_hodnoty[5][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[5][0]
        + hraci_pole_hodnoty[6][1]
        + hraci_pole_hodnoty[7][2]
        + hraci_pole_hodnoty[8][3]
        + hraci_pole_hodnoty[9][4]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[4][0]
        + hraci_pole_hodnoty[5][1]
        + hraci_pole_hodnoty[6][2]
        + hraci_pole_hodnoty[7][3]
        + hraci_pole_hodnoty[8][4]
        + hraci_pole_hodnoty[9][5]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[3][0]
        + hraci_pole_hodnoty[4][1]
        + hraci_pole_hodnoty[5][2]
        + hraci_pole_hodnoty[6][3]
        + hraci_pole_hodnoty[7][4]
        + hraci_pole_hodnoty[8][5]
        + hraci_pole_hodnoty[9][6]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[2][0]
        + hraci_pole_hodnoty[3][1]
        + hraci_pole_hodnoty[4][2]
        + hraci_pole_hodnoty[5][3]
        + hraci_pole_hodnoty[6][4]
        + hraci_pole_hodnoty[7][5]
        + hraci_pole_hodnoty[8][6]
        + hraci_pole_hodnoty[9][7]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[1][0]
        + hraci_pole_hodnoty[2][1]
        + hraci_pole_hodnoty[3][2]
        + hraci_pole_hodnoty[4][3]
        + hraci_pole_hodnoty[5][4]
        + hraci_pole_hodnoty[6][5]
        + hraci_pole_hodnoty[7][6]
        + hraci_pole_hodnoty[8][7]
        + hraci_pole_hodnoty[9][8]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[0][0]
        + hraci_pole_hodnoty[1][1]
        + hraci_pole_hodnoty[2][2]
        + hraci_pole_hodnoty[3][3]
        + hraci_pole_hodnoty[4][4]
        + hraci_pole_hodnoty[5][5]
        + hraci_pole_hodnoty[6][6]
        + hraci_pole_hodnoty[7][7]
        + hraci_pole_hodnoty[8][8]
        + hraci_pole_hodnoty[9][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[0][1]
        + hraci_pole_hodnoty[1][2]
        + hraci_pole_hodnoty[2][3]
        + hraci_pole_hodnoty[3][4]
        + hraci_pole_hodnoty[4][5]
        + hraci_pole_hodnoty[5][6]
        + hraci_pole_hodnoty[6][7]
        + hraci_pole_hodnoty[7][8]
        + hraci_pole_hodnoty[8][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[0][2]
        + hraci_pole_hodnoty[1][3]
        + hraci_pole_hodnoty[2][4]
        + hraci_pole_hodnoty[3][5]
        + hraci_pole_hodnoty[4][6]
        + hraci_pole_hodnoty[5][7]
        + hraci_pole_hodnoty[6][8]
        + hraci_pole_hodnoty[7][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[0][3]
        + hraci_pole_hodnoty[1][4]
        + hraci_pole_hodnoty[2][5]
        + hraci_pole_hodnoty[3][6]
        + hraci_pole_hodnoty[4][7]
        + hraci_pole_hodnoty[5][8]
        + hraci_pole_hodnoty[6][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[0][4]
        + hraci_pole_hodnoty[1][5]
        + hraci_pole_hodnoty[2][6]
        + hraci_pole_hodnoty[3][7]
        + hraci_pole_hodnoty[4][8]
        + hraci_pole_hodnoty[5][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[0][5]
        + hraci_pole_hodnoty[1][6]
        + hraci_pole_hodnoty[2][7]
        + hraci_pole_hodnoty[3][8]
        + hraci_pole_hodnoty[4][9]
    )
    jedna_kombinace = "x" + jedna_kombinace + "x"
    kombinace.append(jedna_kombinace)

    for aaa in kombinace:
        hrac_posledni = nyni_hrac
        if (
            "cc" in aaa
            and nyni_pocitac == 1
            and "zccz" not in aaa
            and "zcccz" not in aaa
            and "zccccz" not in aaa
            and "xccccz" not in aaa
            and "zccccx" not in aaa
            and "zncccz" not in aaa
            and "zcccnz" not in aaa
            and "xncccz" not in aaa
            and "zcccnx" not in aaa
            and "znnccz" not in aaa
            and "zccnnz" not in aaa
            and "xnnccz" not in aaa
            and "zccnnx" not in aaa
        ):
            nyni_pocitac = 2
        elif (
            "ccc" in aaa
            and nyni_pocitac == 2
            and "zcccz" not in aaa
            and "zccccz" not in aaa
            and "xccccz" not in aaa
            and "zccccx" not in aaa
            and "zncccz" not in aaa
            and "zcccnz" not in aaa
            and "xncccz" not in aaa
            and "zcccnx" not in aaa
        ):
            nyni_pocitac = 3
        elif (
            "cccc" in aaa
            and nyni_pocitac == 3
            and "zccccz" not in aaa
            and "xccccz" not in aaa
            and "zccccx" not in aaa
        ):
            nyni_pocitac = 4
        elif "ccccc" in aaa:
            vyherce = "pocitac"
            nyni_pocitac = 5

        if "zzzzz" in aaa:
            vyherce = "hrac"
            nyni_hrac = 5
            if hrac_posledni >= nyni_hrac:
                nyni_hrac = hrac_posledni

        elif "zzzz" in aaa:
            nyni_hrac = 4
            if hrac_posledni >= nyni_hrac:
                nyni_hrac = hrac_posledni

        elif "zzz" in aaa:
            nyni_hrac = 3
            if hrac_posledni >= nyni_hrac:
                nyni_hrac = hrac_posledni

        elif "zz" in aaa:
            nyni_hrac = 2
            if hrac_posledni >= nyni_hrac:
                nyni_hrac = hrac_posledni

        elif "z" in aaa:
            nyni_hrac = 1
            if hrac_posledni >= nyni_hrac:
                nyni_hrac = hrac_posledni

    return


for x in range(0, 50):
    pc_hrac()
    vyherce = ""
    print(nenalezeno, nyni_pocitac, nyni_posledni, nyni_hrac)
    pocitac()
    tahy_hrace = []
    vyhodnoceni()
    if vyherce == "pocitac":
        print("vyhral pocitac!")
        break
    print(kombinace, nenalezeno, nyni_pocitac, nyni_posledni, nyni_hrac)

    hrac()
    vyhodnoceni()
    if vyherce == "hrac":
        print("vyhral jsi!")
        break

    print(kombinace, nenalezeno, nyni_pocitac, nyni_posledni, nyni_hrac)
