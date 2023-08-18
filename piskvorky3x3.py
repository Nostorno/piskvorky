import os, random

os.system("cls")
pocitac_odehral = "ne"
vyherce = ""
odehrano_kol = 0
jedna_kombinace = ""
kombinace = []

set1 = ["⬜️", "⬜️", "⬜️"]
set2 = ["⬜️", "⬜️", "⬜️"]
set3 = ["⬜️", "⬜️", "⬜️"]
set_all = [set1, set2, set3]

set1_vy = ["n", "n", "n"]
set2_vy = ["n", "n", "n"]
set3_vy = ["n", "n", "n"]
set_vy_all = [set1_vy, set2_vy, set3_vy]


def vypis():
    print(set1[0], end="")
    print(set1[1], end="")
    print(set1[2])
    print(set2[0], end="")
    print(set2[1], end="")
    print(set2[2])
    print(set3[0], end="")
    print(set3[1], end="")
    print(set3[2])


def pocitac(pocitac_odehral, odehrano_kol):
    while pocitac_odehral != "ano":
        pc_x = random.randint(0, 2)
        pc_y = random.randint(0, 2)
        pc_tah = set_vy_all[pc_y][pc_x]
        if pc_tah == "n":
            set_all[pc_y][pc_x] = "🟥"
            set_vy_all[pc_y][pc_x] = "c"
            pocitac_odehral = "ano"
            odehrano_kol = odehrano_kol + 1
            vypis()

        else:
            pocitac_odehral = "ne"
    return odehrano_kol


def souradnice():
    pozicexy = input("zadej souradnice xy :")
    if len(pozicexy) != 2:
        os.system("cls")
        vypis()
        print("hodnota neobsahuje dve osy! hraj znovu!" + str(pozicexy))
        pozicexy = ""
        x, y = souradnice()

    x = int(pozicexy[0])
    y = int(pozicexy[1])

    if x > 2 or y > 2:
        os.system("cls")
        vypis()
        print("hodnota mimo hraci pole! hraj znovu!" + str(pozicexy))
        pozicexy = ""
        x, y = souradnice()
    return (x, y)


def hrac(odehrano_kol):
    x, y = souradnice()
    tah = set_vy_all[y][x]
    if tah == "n":
        set_all[y][x] = "🟩"
        set_vy_all[y][x] = "z"
        odehrano_kol = odehrano_kol + 1
        vypis()
    elif tah == "z" or tah == "c":
        vypis()
        print("policko uz je obsazene! hraj znovu!")
        odehrano_kol = hrac(odehrano_kol)
    return odehrano_kol


def vyhodnoceni(vyherce):
    jedna_kombinace = set1_vy[0] + set1_vy[1] + set1_vy[2]
    kombinace.append(jedna_kombinace)
    jedna_kombinace = set2_vy[0] + set2_vy[1] + set2_vy[2]
    kombinace.append(jedna_kombinace)
    jedna_kombinace = set3_vy[0] + set3_vy[1] + set3_vy[2]
    kombinace.append(jedna_kombinace)
    jedna_kombinace = set1_vy[0] + set2_vy[0] + set3_vy[0]
    kombinace.append(jedna_kombinace)
    jedna_kombinace = set1_vy[1] + set2_vy[1] + set3_vy[1]
    kombinace.append(jedna_kombinace)
    jedna_kombinace = set1_vy[2] + set2_vy[2] + set3_vy[2]
    kombinace.append(jedna_kombinace)
    jedna_kombinace = set1_vy[0] + set2_vy[1] + set3_vy[2]
    kombinace.append(jedna_kombinace)
    jedna_kombinace = set1_vy[2] + set2_vy[1] + set3_vy[0]
    kombinace.append(jedna_kombinace)

    for aaa in kombinace:
        if aaa == "ccc":
            vyherce = "pocitac"
        elif aaa == "zzz":
            vyherce = "hrac"
    return vyherce


while True:
    odehrano_kol = pocitac(pocitac_odehral, odehrano_kol)
    vyherce = vyhodnoceni(vyherce)
    kombinace = []
    if vyherce == "pocitac":
        print("pocitac vyhral !!")
        break
    if odehrano_kol == 9:
        print("nikdo nevyhral")
        break
    odehrano_kol = hrac(odehrano_kol)
    vyherce = vyhodnoceni(vyherce)
    kombinace = []
    if vyherce == "hrac":
        os.system("cls")
        vypis()
        print("vyhral jsi !!")
        break
    os.system("cls")
