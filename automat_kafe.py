from data_automat import MENU
from data_automat import zasobnik
import os

os.system("cls")
espresso = ""
latte = ""
cappuccino = ""
nakup_kavy = "ano"

def vyhodnoceni_surovin(espresso,latte,cappuccino):
    for seznam in MENU:
        if (
            zasobnik["water"] - MENU[seznam]["ingredients"]["water"] >= 0
            and zasobnik["milk"] - MENU[seznam]["ingredients"]["milk"] >= 0
            and zasobnik["water"] - MENU[seznam]["ingredients"]["coffee"] >= 0
        ):
            if seznam == "espresso":
                espresso = "🟩"
            elif seznam == "latte":
                latte = "🟩"
            elif seznam == "cappuccino":
                cappuccino = "🟩"

        else:
            if seznam == "espresso":
                espresso = "🟥"
            elif seznam == "latte":
                latte = "🟥"
            elif seznam == "cappuccino":
                cappuccino = "🟥"
    return (espresso,latte,cappuccino)

def zobrazeni(espresso,latte,cappuccino):
    espresso,latte,cappuccino = vyhodnoceni_surovin(espresso,latte,cappuccino)
    print("Automat na kavu / cenik / moznost koupit")
    print(f"espresso:{MENU['espresso']['cost']} kc {espresso}")
    print(f"latte:{MENU['latte']['cost']} kc {latte}")
    print(f"cappuccino:{MENU['cappuccino']['cost']} kc {cappuccino}")
    print("-----------------------------------")
    return(espresso,latte,cappuccino)

def nakup(kava):
    water = zasobnik["water"] - MENU[kava]["ingredients"]["water"]
    milk = zasobnik["milk"] - MENU[kava]["ingredients"]["milk"]
    coffee = zasobnik["coffee"] - MENU[kava]["ingredients"]["coffee"]
    print (water,milk,coffee)
    zasobnik["water"] = water
    zasobnik["milk"] = milk
    zasobnik["coffee"] = coffee


while nakup_kavy == "ano": 
    espresso,latte,cappuccino = zobrazeni(espresso,latte,cappuccino)
    print (espresso,latte,cappuccino)
    if espresso == "🟥" and latte == "🟥" and cappuccino =="🟥":
        print ("Automat nema suroviny!")
        break

    print (zasobnik["water"])
    print (zasobnik["milk"])
    print (zasobnik["coffee"])
    kava = input("Jakou kavu si prejete? :")

    if kava == "espresso" and espresso == "🟩" or kava == "latte" and latte == "🟩"or kava == "cappuccino" and cappuccino == "🟩":
        nakup(kava)
    else:
        print ("Chybne zadani kavy!")

    nakup_kavy = input("Chcete dalsi kavu? ano/ne:")
    

    


