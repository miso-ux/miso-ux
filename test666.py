import operator
lst = []
#cislo = int(input("z: "))
while True:
    cislo = int(input("z: "))
    lst.append(cislo)
    # print(lst)
    if cislo == '':
      #  print(lst)
        # lst.remove('')
        break
cislo = int(cislo)
# lst = int(lst)
# filter()
sum_ = sum(int(lst))
max_ = max(lst)
min_ = min(lst)
# avg_ = avg(lst)
print(max_, "|", min_, "|")
