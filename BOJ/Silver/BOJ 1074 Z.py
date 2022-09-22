# 수학적 재귀 풀이법
N, r, c = map(int, input().split())

ans = 0

while N != 0:

	N -= 1

	# 1사분면
	if r < 2 ** N and c < 2 ** N:
		ans += ( 2 ** N ) * ( 2 ** N ) * 0

	# 2사분면
	elif r < 2 ** N and c >= 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 1
		c -= ( 2 ** N )
        
	# 3사분면    
	elif r >= 2 ** N and c < 2 ** N: 
		ans += ( 2 ** N ) * ( 2 ** N ) * 2
		r -= ( 2 ** N )
        
	# 4사분면    
	else:
		ans += ( 2 ** N ) * ( 2 ** N ) * 3
		r -= ( 2 ** N )
		c -= ( 2 ** N )
    
print(ans)


# 모든 점을 탐색하는 재귀 방식, but 메모리초과

def z(n, i, j, y, x):
    global cnt, ans, p
    if n == 1:
        for di, dj in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            ni, nj = i + di, j + dj
            cnt += 1
            if y == ni and x == nj:
                ans = cnt
                p = True
                return
    else:
        for o in range(2):
            for u in range(2):
                if p:
                    return
                z(n-1, (i+(2**(n-1))*o), (j+(2**(n-1))*u), y, x)


n, r, c = map(int, input().split())

arr = [[0] * 2**n for _ in range(2**n)]
ans = 0
cnt = -1
p = False
z(n, 0, 0, r, c)
print(ans)


