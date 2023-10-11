def pass_reff(list1=[]):
    list1.extend([22, 33])
    print("lista wewnątrz funkcji", list1)

def ff(cyfra):
    global a
    a=10
    # funkcja global przykrywa i nadaje wszystkm pozostałym zmiennym spoza funkcji wartość nadaną jeśli funkcja zostanie wykonana, globale są uznawane za mało konieczne.
    cyfra = a + 4
    print('A wewnątrz',a)
# global przykryje tą wartość z zmiennej a poniżej z funkcji ff
a=5
ff(a)
print(a)

list1 = [12, 76, 90]
# a terad dodajmy pass_reff(list1) - pokazuje wtedy resztę zduplikowanych list, to dodaje listy które przez przypadek duplikujemy, w innych językach była by nadpisana w liście ostatnia lista(wartość) pamiętać o zasięgach i "referencjach funkcji"

pass_reff(list1)
print(list1)
