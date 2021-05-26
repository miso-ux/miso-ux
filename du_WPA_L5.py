lst = []
while True:
    try:
        cislo = int(input("Zadaj cele cislo: "))
        lst.append(cislo)
        continue
    except ValueError:
        print()
    break
print(lst)
count_ = len(lst)
sum_ = sum(lst)
avg_ = sum(lst) / len(lst)
max_ = max(lst)
min_ = min(lst)
print("pocet: ", count_, "|", "spolu: ", sum_, "|", "priemer :", int(avg_),
      "|", "najmensie: ", min_, "|", "najvacsie: ", max_,)
