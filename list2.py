test = input("zadaj cislo: ")
try:
    my_list = []
    while True:
        my_list.append(int(input()))
except:
    print(test)