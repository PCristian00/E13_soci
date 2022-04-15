def socio(x, lista):
    if x in lista:
        print("Il valore " + str(x) + " è nella lista\nIndice "+str(lista.index(x)))
    else:
        print("Il valore " + str(x) + " NON è nella lista")


print("Inserire numeri separati da spazi")
print("INVIO per confermare")
lista = [int(x) for x in input().split()]

val = int(input("Inserire valore da cercare: "))
socio(val, lista)
