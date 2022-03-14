n = int(input('masukkan jumlah tanding : ', ))
x = 1
poin = 0
poinSum = 0
goalSum = 0
assistSum = 0
kebobol = 0
while x <= n:
    hasil = input('hasil pertandingan ke -{} (w/l/d)           : '.format(x), )
    if hasil == 'w':
        poin = 3
    elif hasil == 'd':
        poin == 1
    elif hasil == 'l':
        poin = 0
    poinSum += poin
    
    goal = int(input('jumlah goal pertandingan ke -{}     : '.format(x), ))
    goalSum += goal
    
    oppgoal = int(input('jumlah kebobolan pertandingan ke -{}: '.format(x), ))
    kebobol += oppgoal
    x += 1
print('poin              : ',poinSum)
print('jumlah goal       : ',goalSum)
print('jumlah goal lawan : ',kebobol)


    




