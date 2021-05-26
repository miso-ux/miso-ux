lst = []

while True:
    cislo = input("kokot: ")
    lst.append(cislo)
    print(lst)
    except:
        print("")
        continue
max_ = max(lst)
min_ = min(lst)
print(max_, "|", min_, "|")


