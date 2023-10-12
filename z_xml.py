import re
import xml.etree.ElementTree as ET
import requests

url = requests.get('https://api.weatherapi.com/v1/current.xml?key=d863af85e8fa43618f682810220812&q=Lodz&aqi=no')
print(url.status_code)
plik = url.text

with open('danexml.xml', 'w') as f:
    f.write(plik)

with open('danexml.xml','r') as f:
    tree = ET.parse(f)

root = tree.getroot()
print(root.tag)
print(root.attrib)
for dziecko in root:
    print(dziecko.tag, dziecko.attrib)
    # sprawdzamy gałęzie drzewa dziecko w root xml

x=[elem.tag for elem in root.iter()]
for i in x:
    print(i)

for miasto in root.iter('name'):
    print(miasto.text)

for temp_c in root.iter('temp_c'):
    print(temp_c.text)