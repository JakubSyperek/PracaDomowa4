linia = 'kanapka'

with open("text.txt", "w+") as plik:
    for linia in plik:
        print(linia,end="")