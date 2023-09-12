from data10x10 import moznosti_hrac_2, moznosti_hrac_3, moznosti_hrac_4

print(moznosti_hrac_2, moznosti_hrac_3, moznosti_hrac_4)

hodnota = input("zadej nejakou kombinaci :")
print("--------- vyhodnoceni-----------")

for test in moznosti_hrac_2:
    if test in hodnota:
        print("obsahuje zz")
    else:
        print("neobsahuje")
