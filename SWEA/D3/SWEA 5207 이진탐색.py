TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = list(map(int, input().split()))

    ans = 0
    # arr2의 원소를 하나씩 순회하면서 검사
    for key in arr2:
        l, r = 0, N-1
        dir = [0, 0]

        if arr1[l] <= key <= arr1[r]:

            while l <= r:
                mid = (l+r) // 2

                if arr1[mid] == key:
                    ans += 1
                    break

                elif arr1[mid] > key:
                    r = mid - 1
                    if dir[0]:
                        break
                    # 왼쪽 선택을 저장
                    dir[0], dir[1] = 1, 0

                else:
                    l = mid + 1
                    if dir[1]:
                        break
                    # 오른쪽 선택을 저장
                    dir[0], dir[1] = 0, 1

    print(f'#{tc} {ans}')