'''
men    0    1    2    3    4    5    6    7
 0  ['0', '0', '0', '0', '0', '0', '0', '0']   8
 1  ['0', '0', '0', '0', '0', '0', '0', '0']   7
 2  ['0', '0', '0', '0', '0', '0', '0', '0']   6
 3  ['0', '0', '0', '0', '0', '0', '0', '0']   5
 4  ['0', '0', '0', '0', '0', '0', '0', '0']   4
 5  ['0', '0', '0', '0', '0', '0', '0', '0']   3
 6  ['0', '0', '0', '0', '0', '0', '0', '0']   2
 7  ['0', '0', '0', '0', '0', '0', '0', '0']   1
      1    2    3    4    5    6    7    8    al

'''

# 1 ; 1 === 7 :0
# 1 ; 2 === 6 :0
# 1 ; 3 === 5 :0
# 1 ; 4 === 4 :0
l = []
x1 = int(input('x> '))-1
y1 = int(input('y> '))-1
sym = '🟢'
pos = '🐴'
if 0 < x1 < 9 and 0 < y1 < 9:
    # x1 = 8 - y  # 7
    # y1 = x - 1  # 0
    l.append(f'{x1 + 1} : {y1 + 2}')
    l.append(f'{x1 + 1} : {y1 - 2}')
    l.append(f'{x1 - 1} : {y1 + 2}')
    l.append(f'{x1 - 1} : {y1 - 2}')
    l.append(f'{x1 + 2} : {y1 + 1}')
    l.append(f'{x1 - 2} : {y1 + 1}')
    l.append(f'{x1 + 2} : {y1 - 1}')
    l.append(f'{x1 - 2} : {y1 - 1}')
    mass = [['❎'] * 8 for k in range(8)]
    mass[x1][y1] = pos
    for i in l:
        if 0 <= int(i[:2]) < 8 and 0 <= int(i[-2:]) < 8:
            mass[int(i[0])][int(i[-1])] = sym
    for m in mass:
        print()
        for j in m:
            print(j, end='\t')
else:
    print('from 0 to 9')