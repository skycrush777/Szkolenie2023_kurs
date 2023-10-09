wiek = 2023 - 1986
str1 = '1 to jest tekst 1\n'
str2 = f'wiek = {wiek}\n'
# \t tabulator \n następny wiersz
str3 = f"""
******************************************
*3 to jest tekst 3, to też wiek {wiek}
 *                   ale ma specjalne opcje 
*i kolejne wiersze
******************************************"""
print(str1, str2, str3)
