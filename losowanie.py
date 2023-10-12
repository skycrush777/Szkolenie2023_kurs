import random
# kostka do gry k6
k6 = random.randint(1,6)
print("Wynik rzutu kością: ",k6)

# inny sposób losowania
lista = ["Tomek", "Kasia", "Basia", "Marcin"]
loteria = random.choice(lista)
print("Elektryczna Izera wygrywa: ", loteria)

# inny sposób losowania
liczba = random. random()
print(liczba)

liczba2 = random.randrange(-1000,1000,2)
print(liczba2)

# losowanie wartości float
liczba3 = random.uniform(-1000, 1000)
print(liczba3)