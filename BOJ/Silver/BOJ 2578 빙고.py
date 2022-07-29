chulsu_pan = []
sahe_pan = []
bingo_pan = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], 
[20, 21, 22, 23, 24], [0, 5, 10, 15, 20], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], 
[3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [0, 6, 12, 18, 24], [4, 8, 12, 16, 20]]

for i in range(5):
    chulsu_pan.extend(list(map(int, input().split())))

for i in range(5):
    sahe_pan.extend(list(map(int, input().split())))

bingo_su = 0

for i in range(len(sahe_pan)):
    for j in range(12):
        try:
            bingo_pan[j].remove(chulsu_pan.index(sahe_pan[i]))
        except:
            pass
        if bingo_pan[j] == []:
            bingo_su += 1
            bingo_pan[j].append('clear')
    if bingo_su >= 3:
        print(i+1)
        break



# bingo1 = [1, 2, 3, 4, 5]
# bingo2 = [6, 7, 8, 9, 10]
# bingo3 = [11, 12, 13, 14, 15]
# bingo4 = [16, 17, 18, 19, 20]
# bingo5 = [21, 22, 23, 24, 25]
# bingo6 = [1, 6, 11, 16, 21]
# bingo7 = [2, 7, 12, 17, 22]
# bingo8 = [3, 8, 13, 18, 23]
# bingo9 = [4, 9, 14, 19, 24]
# bingo10 = [5, 10, 15, 20, 25]
# bingo11 = [1, 7, 13, 19, 25]
# binho12 = [5, 9, 13, 17, 21]