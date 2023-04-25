# 3면이 보이는 주사위의 개수
  # N > 2 일때 4개 고정
# 2면이 보이는 주사위의 개수
  # 윗면을 포함하는 주사위 = (N - 2) * 4
  # 윗면을 포함하지 않는 모서리 주사위 = (N - 1) * 4
# 1면이 보이는 주사위의 개수
  # 전체 보이는 주사위 개수 (N**2 * 5) - 3면 - 2면

# 3면합 최소 구하기 -> 마주보는 3개 중 각각 작은 값 구해서 더하기 A - F / B - E / C - D
  # 2면합 최소 -> 위 3개의 값 중 작은 2개
  # 1면합 최소 -> 그냥 주사위 값 중 최소 값

N = int(input())
arr = list(map(int, input().split()))
ans = 0

if N == 1:
    ans = sum(arr) - max(arr)

else:
    lower_num = [min(arr[0], arr[5]), min(arr[1], arr[4]), min(arr[2], arr[3])]
    lower_num.sort()
    three_myeon_shown_dice = 4
    two_myeon_shown_dice = (N - 1) * 4 + (N - 2) * 4
    one_myeon_shown_dice = (N**2 * 5) - three_myeon_shown_dice * 3 - two_myeon_shown_dice * 2

    ans += sum(lower_num) * three_myeon_shown_dice
    ans += sum(lower_num[:2]) * two_myeon_shown_dice
    ans += lower_num[0] * one_myeon_shown_dice

print(ans)