n = int(input())
huwi = input()

su = []
for _ in range(n):
    su.append(int(input()))

arr = []
for j in huwi:
    if j.isalpha():                 
        arr.append(su[ord(j)-65])
    else:
        if j == '+':                        
            c = arr[-2] + arr[-1]
            del arr[-1], arr[-1]
            arr.append(c)
        elif j == '*':
            c = arr[-2] * arr[-1]  
            del arr[-1], arr[-1]
            arr.append(c)
        elif j == '/':
            c = arr[-2] / arr[-1]  
            del arr[-1], arr[-1]
            arr.append(c)
        elif j == '-':
            c = arr[-2] - arr[-1]  
            del arr[-1], arr[-1]
            arr.append(c)
print(f'{arr[0]:.2f}')