import re

tekst = "Python to nie tylko gad, ale także język programowania"
wynik = re.match(r'Python', tekst)
print(wynik)

print(f'Dopasowano: {wynik.group()}, poczatek: {wynik.span()[0]}, koniec: {wynik.span()[1]}')
print(f'Dopasowano: {wynik.group()}, poczatek: {wynik.start()}, koniec: {wynik.end()}')
