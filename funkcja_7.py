def print_the_next_number(start):
    print(start + 1)
    if start >= 10:
        return 'Idź na kawę!'
    return print_the_next_number(start + 1)


print(print_the_next_number(5))
# referencja funkcja odwołująca się sama do siebie wywołuje. zaczynamy od 5 dlatego wyswietla się 6 do 11 bo większe niż 10 i pozniej wyswietla idz na kawe....
