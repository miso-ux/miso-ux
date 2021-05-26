rok1 = int(input("zadaj 1 rok: "))
rok2 = int(input("zadaj 2 rok: "))
if rok1 > rok2:
    print("mas zly rozsah")
rok1 -= 1
rok2 += 1
for rozsah in range(rok1, rok2):
    if rozsah % 4 == 0 and rozsah % 100 != 0 or rozsah % 4 == 0 and rozsah % 400 == 0:
        print("tieto one", rozsah)