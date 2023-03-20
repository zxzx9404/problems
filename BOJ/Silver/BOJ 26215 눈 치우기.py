# 40ms
# 아무튼 큰거부터 계속 치워야 제일 효율적인 정리가 가능하니까
# 그냥 매번 무지성 sort

N = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

if max(arr) > 1440:
    print(-1)
else:
    time = 0
    while arr and time < 1441:
        arr[0] -= 1
        if len(arr) > 1:
            arr[1] -= 1
            arr.pop(1) if not arr[1] else '여기 pass 쓰면 왜 에러남'
        arr.pop(0) if not arr[0] else '여기도'
           
        arr.sort(reverse=True)
        time += 1

    print(time if time != 1441 else -1)