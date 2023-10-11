# dane z plików .csv otwarty np przez pythona to bez sensu. są biblioteki specjalne ktore otwierają ładnie pliki. python ma zostać pythonem a praca jest na plikach.
# by otworzył polskie znaki to opcja encoding
f = open('tekst.txt',encoding='utf-8')
text = f.read()
print(text)
# read(65) wyświetla 65 znaków
#
f = open('baza.dat', 'r')
text = f.read(65)
print(text)
f.close()
# f.colse() - usuwa z pamięci plik.


f = open('slice.dat', 'r')
f.write(text)
f.close()


#f = open('slice.dat', 'a')
#f.write(text)
#f.close()

with open("slice.dat",'r') as f:
    print(f.readline())
    # bierze 5 pierwszych znaków
    print(f.readline())
    # bierze kolejne znaki z drugiego wiersza
    print(f.readline())

