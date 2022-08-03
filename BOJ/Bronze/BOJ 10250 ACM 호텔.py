a = int(input())

for i in range(a):
    chung, ho, sonnim = map(int, input().split())
    if sonnim % chung == 0 and sonnim // chung < 10:
        son_ho = str(chung) + '0' + str(sonnim // chung)
    elif sonnim % chung == 0 and sonnim // chung >= 10:
        son_ho = str(chung) + str(sonnim // chung)
    elif sonnim // chung +1 < 10 and sonnim // chung + 1 < 10:
        son_ho = str(sonnim % chung) + '0' + str(sonnim // chung +1)
    else:
        son_ho = str(sonnim % chung) + str(sonnim // chung +1)
    
    print(son_ho)