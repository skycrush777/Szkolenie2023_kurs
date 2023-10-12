import re

tekst = "Python to nie tylko gad, ale także język programowania"
# wynik = re.match(r'Python', tekst) wykonuje szykanie od początku
wzorzec = re.compile(r'ni')
# wynik = wzorzec.search(tekst)
wynik = wzorzec.findall(tekst)
print(type(wynik))


print(wynik)

# print(f'Dopasowano: {wynik.group()}, poczatek: {wynik.span()[0]}, koniec: {wynik.span()[1]}')
# if wynik:
    # print(f'Dopasowano: {wynik.group()}, poczatek: {wynik.start()}, koniec: {wynik.end()}')


if len(wynik)>0:
    print(f'Dopasowano: {wynik}')
else:
    print(wynik)