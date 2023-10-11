a = 'helló'
b = a.encode('utf-8')
print(b)
print(a)

a = 'helló'
b = a.encode('latin1')
print(b)
print(a)

a = 'helló'
b = a.encode('cp1252')
print(b)
print(a)

# dekodowanie
print(b.decode('cp1252'))

x=123.456
y=1234.456

# formatowanie
print(x.__format__('0.2f'))
print(format(x, '0.1f'))
print(format(x, '6.1f'))
print(format(y, '6.1f'))

#wypełniacz
