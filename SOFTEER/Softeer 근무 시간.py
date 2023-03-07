def trans_to_time(time):
    hour, minute = time.split(':')

    return (int(hour)*60+int(minute))

ans = 0

for _ in range(5):
    go, back = map(trans_to_time, input().split())
    ans += (back - go)

print(ans)