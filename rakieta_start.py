# funkcja odliczania, która rekurencyjnie obsłuży start rakiety
# -countdown od liczby całkowitej n, aż osiągniemy 0, na końcu komunikat START

def countdown(rakieta):
    print(rakieta - 1)
    if rakieta <= 1:
        return 'START'
    return countdown(rakieta - 1)


print(countdown(100))