# python jest nie dokładny w obliczeniach, duża liczba miejsc po przecinku wynika z architektury pythona, minlionowe miejsca po przecinku znikają.
# biblioteka numpy ze strony numpy.org
a = 14
b = 3
print("Wynik dodawania:", a + b)
print("Wynik odejmowania:", a - b)
print("Wynik mnożenia:", a * b)
print("Wynik dzielenia:", a / b)
print("Wynik dzielenie bez reszty:", a // b)
print("Wynik potęgowania:", a ** b)
print("Wynik operatora modulo (reszta z dzielenia):", a % b)

pi = 3.14
radius = 4.5
area = pi * (radius ** 2)
print("Powierzchnia koła= ", area)

import sys

print(sys.float_info)
