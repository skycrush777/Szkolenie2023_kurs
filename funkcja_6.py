def add_up(x, y):
    return x + y


print(add_up(2, 5))

add_up = lambda x, y: x + y
print(add_up(2,5))
# add_up powyżej to funckja anonimowa; lambda moze byc wykonywana w locie i moze byc gdzies wykonywana w jakims miejscu tzw. na miejscu.... w locie .... zawsze działa jak return i dodaje się jak funckja. nazwa zmiennej, a lambda działa jak funkcja
names = ["Tomek", "Piotrek", "Adam"]
print(list(filter(lambda x: len(x)==4, names)))
print(list(filter(lambda x: len(x)==7, names)))
print(list(filter(lambda x: len(x)==5, names)))
# len - długościowo ; filter - filtruje, names pracuje na tablicy "names"
print(sorted(names, key=lambda x: len(x), reverse=True))
print(sorted(names, key=lambda x: len(x)))




