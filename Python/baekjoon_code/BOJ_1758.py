n = int(input())

tip = []
for i in range(n):
    tip.append(int(input()))
tip.sort(reverse=True)

print(tip)

ans = []

for i in range(1,n+1):
    ans.append(tip[i-1] - (i-1))

print(ans)

for i in range(len(ans)):
    print(ans[i])
    if ans[i] < 0 :
        ans[i] = 0
print(ans)

cnt = 0

for i in range(len(ans)):
    cnt += ans[i]

print(cnt)