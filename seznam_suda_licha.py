seznam = [cislo for cislo in range(1, 21)]
suda = []
licha = []

for trideni in seznam:
    if trideni % 2 == 0:
        suda.append(trideni)
    else:
        licha.append(trideni)

print(suda)
print(licha)
