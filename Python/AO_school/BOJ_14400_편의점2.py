import sys; input = sys.stdin.readline
n = int(input())
xmap = [] # x좌표
ymap = [] # y좌표
for _ in range(n):
    x, y = map(int, input().split())
    xmap.append(x)
    ymap.append(y)
xmap.sort()
ymap.sort()

print(xmap, ymap)

xmid = xmap[(n-1)//2]
ymid = ymap[(n-1)//2]

print(xmid , ymid) # 모든 고객들의 거리 합을 최소로 하는 위치

ans = 0
#거리를 구해준다
for i in range(n):
    ans += abs(xmid - xmap[i]) + abs(ymid - ymap[i])
print(ans)