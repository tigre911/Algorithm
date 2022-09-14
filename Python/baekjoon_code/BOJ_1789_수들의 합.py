s = int(input())
cnt = 0
ans = 0
while True:
    cnt += 1
    ans += cnt
    if ans > s:
        break


print(cnt -1)

    # print(ans, cnt)

