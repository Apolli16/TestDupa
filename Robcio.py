import re

try:
    file_path = input('Writhe Path')
    plik = open(file_path)
    y = plik.readlines()
except:
    print("Nie ma takiego pliku")
    exit()
tablica = []
for n in range(len(y)):
    x = re.findall('\d\d[:]\d\d',str(y[n]))
    tablica+=x
tablica = [x for x in tablica if x != []]
minuty = 0
print(tablica)
for tm in tablica:
    podzielCzas = [int(s) for s in tm.split(':')]
    minuty += (podzielCzas[0] * 60 + podzielCzas[1])
godz, min = divmod(minuty, 60)
dzien, godz = divmod(godz,24)
if dzien < 10:
    print("{} dzień i {}:{}".format(dzien,godz,min))
else:
    print("{} dni i {}:{}".format(dzien, godz, min))


    #123123

