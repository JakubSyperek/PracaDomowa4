
plik = open("tekst.txt","a+")
lista = []
for x in range (0,100,4):
    lista += [x]
plik.writelines(str(lista))
plik.close()
