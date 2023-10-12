import ftplib

ftp = ftplib.FTP('test.rebex.net')
logowanie = ftp.login('demo', 'password')

print(logowanie)
katalog = ftp.nlst()
print(katalog)
plik = ftp.retrbinary('RETR readme.txt',open('plik_z_ftp','wb').write)
print(plik)
katalog2 = ftp.nlst('pub/example')
print(katalog2)
plik2 = ftp.retrbinary('RETR pub/example/KeyGenerator.png', open('grafika.png','wb').write)