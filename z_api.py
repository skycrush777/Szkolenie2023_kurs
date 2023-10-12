import requests
miasto = input("Podaj miasto: ")
url = requests.get(f'http://api.weatherapi.com/v1/current.json?key=d863af85e8fa43618f682810220812&q={miasto}&aqi=no')
print(url.status_code)
lokalizacja = url.json()['location']['name']
temp_C = url.json()['current']['temp_c']

print(lokalizacja)
print(temp_C)
with open("pogoda.txt",'a', encoding='utf-8')as f:
    f.write(f'\nW mieście {lokalizacja}, jest {temp_C} stopni C°')
f.close()
input('Wciśnij Enter by zakończyć program')