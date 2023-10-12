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

print(tree)
