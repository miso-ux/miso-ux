print("Vypocet obvodu trojuholnika. Dlzky stran su v mm")
while True:
    try:
        strana_a = float(input("Zadaj stranu 'a' v mm: "))
        break
    except:
        print ("Strana 'a' musi byt cislo!!!")
while True:
    try:
        strana_b = float(input("Zadaj stranu 'b' v mm: "))
        break
    except:
        print ("Strana 'b' musi byt cislo!!!")
while True:
    try:
        strana_c = float(input("Zadaj stranu 'c' v mm: "))
        break
    except:
        print ("Strana 'c' musi byt cislo!!!")
import math
vypocet1 = strana_a + strana_b + strana_c
cm = (vypocet1 / 10)
print ("Obvod trojuholnika je", vypocet1, "mm")
print ("Obvod trojuholnika je", cm, "cm")

print("Obvod trojuholnika je", vypocet1, "mm. Prepocte na cm je ", cm, "cm")
