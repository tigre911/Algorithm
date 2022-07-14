n, k = map(int,input().split())
# n 탑의수
# k 만드려는 높이 차이

top_height = list(map(int, input().split()))

cnt = 0

for i in range(1,n):
    if top_height[i]-top_height[i-1] > k:
        # cnt += top_height[i]-top_height[i-1] - k
        cnt += 1
    elif top_height[i]-top_height[i-1] < k:
        # cnt += top_height[i-1]-top_height[i] - k
        cnt += 1

print(min(n,cnt))