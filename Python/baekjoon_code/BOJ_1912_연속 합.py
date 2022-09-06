'''n = int(input())

arr = list(map(int,input().split()))
# [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
print(arr)

dp = [0] * (n+1)

dp[1] = max(arr)

for i in range(2,n):
    dp[i] = max(arr[i], dp[i-1]+arr[i])

print(dp)
print(max(dp))
'''
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n # arr[i]까지 고려했을 때 최대 연속합
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1]+arr[i]) # arr[i] 혹은 이전 최대 연속합+arr[i]

print(dp)
print(max(dp))