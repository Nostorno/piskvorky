import os, random

os.system("cls")

hraci_pole_cele = []
hraci_pole_hodnoty = []
vyherce = ""
jedna_kombinace = ""
kombinace = []
start = "ano"
nyni_pocitac = int(1)
nyni_hrac = 1
nyni_posledni = 0
nenalezeno = 0

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


def pocitac():
    global start, nyni_posledni, nenalezeno, nyni_pocitac
    pocitac_odehral = "ne"
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
            pc_tah = hraci_pole_hodnoty[pc_y][pc_x]
            if pc_tah == "n":
                hraci_pole_cele[pc_y][pc_x] = "🟥"
                hraci_pole_hodnoty[pc_y][pc_x] = "c"

                print(kombinace, nenalezeno, nyni_pocitac, nyni_posledni, nyni_hrac)

                nyni_posledni = nyni_pocitac
                vyhodnoceni()
                if nyni_pocitac > nyni_posledni:
                    pocitac_odehral = "ano"
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
    global vyherce, nyni_pocitac, nyni_hrac
    for ccc in range(0, 10):
        jedna_kombinace = "".join(hraci_pole_hodnoty[ccc][0:10])
        kombinace.append(jedna_kombinace)
    for ddd in range(0, 10):
        jedna_kombinace = "".join([seznam[ddd] for seznam in hraci_pole_hodnoty])
        kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[4][0]
        + hraci_pole_hodnoty[3][1]
        + hraci_pole_hodnoty[2][2]
        + hraci_pole_hodnoty[1][3]
        + hraci_pole_hodnoty[0][4]
    )
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[5][0]
        + hraci_pole_hodnoty[4][1]
        + hraci_pole_hodnoty[3][2]
        + hraci_pole_hodnoty[2][3]
        + hraci_pole_hodnoty[1][4]
        + hraci_pole_hodnoty[0][5]
    )
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
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[9][4]
        + hraci_pole_hodnoty[8][5]
        + hraci_pole_hodnoty[7][6]
        + hraci_pole_hodnoty[6][7]
        + hraci_pole_hodnoty[5][8]
        + hraci_pole_hodnoty[4][9]
    )
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[9][5]
        + hraci_pole_hodnoty[8][6]
        + hraci_pole_hodnoty[7][7]
        + hraci_pole_hodnoty[6][8]
        + hraci_pole_hodnoty[5][9]
    )
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[5][0]
        + hraci_pole_hodnoty[6][1]
        + hraci_pole_hodnoty[7][2]
        + hraci_pole_hodnoty[8][3]
        + hraci_pole_hodnoty[9][4]
    )
    kombinace.append(jedna_kombinace)
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[4][0]
        + hraci_pole_hodnoty[5][1]
        + hraci_pole_hodnoty[6][2]
        + hraci_pole_hodnoty[7][3]
        + hraci_pole_hodnoty[8][4]
        + hraci_pole_hodnoty[9][5]
    )
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
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[0][4]
        + hraci_pole_hodnoty[1][5]
        + hraci_pole_hodnoty[2][6]
        + hraci_pole_hodnoty[3][7]
        + hraci_pole_hodnoty[4][8]
        + hraci_pole_hodnoty[5][9]
    )
    kombinace.append(jedna_kombinace)
    jedna_kombinace = (
        hraci_pole_hodnoty[0][5]
        + hraci_pole_hodnoty[1][6]
        + hraci_pole_hodnoty[2][7]
        + hraci_pole_hodnoty[3][8]
        + hraci_pole_hodnoty[4][9]
    )
    kombinace.append(jedna_kombinace)

    for aaa in kombinace:
        if "ccccc" in aaa:
            vyherce = "pocitac"
            nyni_pocitac = 5
        elif "cccc" in aaa and nyni_pocitac == 3 and "zccccz" not in aaa:
            nyni_pocitac = 4
        elif (
            "ccc" in aaa
            and nyni_pocitac == (2 or 3)
            and "zcccz" not in aaa
            and "zccccz" not in aaa
        ):
            nyni_pocitac = 3
        elif (
            "cc" in aaa
            and nyni_pocitac == (1 or 2)
            and "zccz" not in aaa
            and "zcccz" not in aaa
            and "zccccz" not in aaa
        ):
            nyni_pocitac = 2

        elif "zz" in aaa and nyni_hrac == 1:
            nyni_hrac = 2
        elif "zzz" in aaa and nyni_hrac == 2:
            nyni_hrac = 3
        elif "zzzz" in aaa and nyni_hrac == 3:
            nyni_hrac = 4
        elif "zzzzz" in aaa:
            vyherce = "hrac"

    return


for x in range(0, 50):
    pocitac()
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
