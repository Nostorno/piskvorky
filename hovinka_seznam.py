set1 = ["💩", "💩", "💩", "💩"]
set2 = ["💩", "💩", "💩", "💩"]
set3 = ["💩", "💩", "💩", "💩"]
set4 = ["💩", "💩", "💩", "💩"]
celek = [set1, set2, set3, set4]
print(f"{set1}\n{set2}\n{set3}\n{set4}\n")
pozicexy = input("zadej souradnice kde nechces bobik xy :")
x = int(pozicexy[0])
y = int(pozicexy[1])

celek[x][y] = ["😀"]
print(f"{set1}\n{set2}\n{set3}\n{set4}\n")
