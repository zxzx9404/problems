# 40ms
# 4, 7, 44, 47, 444 등 4와 7로만 이루어진 모든 수를 검토해서
# A <= num <= B 이면 카운트를 올려주는 식

def dfs(num):
    global ans
    
    if num > B:
        return
    
    if num >= A:
        ans += 1
    
    dfs(num * 10 + 4)
    dfs(num * 10 + 7)
        

A, B = map(int, input().split())
ans = 0

dfs(0)

print(ans)


############################

# 64ms
# 처음에 뻘짓으로 푼 방식
# +1 하면서 모든 수를 검토하면 시간초과가 나니까
# 4,7이 아닌 자릿수 중 제일 큰 자리수부터 올려주면 되지 않을까?
# 를 구현해봄
# 20000을 예로 들면
# 20000 -> 30000 -> 40000 -> 41000 -> 42000 -> ... -> 44444

A, B = map(int, input().split())
ans = 0
num = 10 ** (len(str(A)) - 1)

while num <= B:
    for i in range(len(str(num))):
        if str(num)[i] not in '47':
            k = len(str(num)) - i - 1
            while True:
                temp = num + 10 ** k
                
                if temp > B:
                    k -= 1
                    if k == -1:
                        print(ans)
                        quit()
                else:
                    num = temp
                    break
            break    
    else:
        if A <= num <= B:
            ans += 1
            print(num)
        num += 1
        
print(ans)