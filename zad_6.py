def zad_6(lista1: list, lista2: list):
    nowa_lista = lista1 + lista2
    nowa_lista = list(dict.fromkeys(nowa_lista))
    nowa_lista = [el**3 for el in nowa_lista]
    return(nowa_lista)
print(zad_6([4,2],[2,4,5]))