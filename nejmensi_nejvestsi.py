score = input("zadej cislo oddeluj carkou :")
seznam_score = score.split(",")  # vytvori seznam z vyse zadanych cisel
min = int(seznam_score[0])  # do promene min a max ulozi prvni cislo ze seznamu
max = int(seznam_score[0])
for (
    bbb
) in (
    seznam_score
):  # projde seznam a ulozi cislo do min nebo max podle velikosti prvniho cisla
    if int(bbb) < min:
        min = int(bbb)
    if int(bbb) > max:
        max = int(bbb)

print("nejmensi cislo je :" + str(min))
print("nejvetsi cislo je :" + str(max))
