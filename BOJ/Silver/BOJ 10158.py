w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
X = (t-(w-p))
Y = (t-(h-q))


#X의 이동 계산
if X <= 0: #방향전환 없이 끝나는 경우
    p = p+t
else: #방향전환을 하는 경우
    if (X//w) % 2 == 1: #홀수번만큼 꺾임
        p = t - w*(X//w) - (w-p)
    elif (X//w) % 2 == 0: #짝수번만큼 꺾임
        p = w - (t - w*(X//w) - (w-p))

#Y의 이동 계산
if Y <= 0:  #방향전환 없이 끝나는 경우
    q = q+t
else: #방향전환을 하는 경우
    if (Y//h) % 2 == 1: #홀수번만큼 꺾임
        q = t - h*(Y//h) - (h-q)
    elif (Y//h) % 2 == 0: #짝수번만큼 꺾임
        q = h - (t - h*(Y//h) - (h-q))

print(p, q)