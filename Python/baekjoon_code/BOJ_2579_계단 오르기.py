'''
n = int(input())
stairs = [int(input()) for _ in range(n)] # [10, 20, 15, 25, 10, 20]
dp = [0] * (n+1)
dp[0] = stairs[0] # 10
dp[1] = stairs[0] + stairs[1] # 30
dp[2] = max(stairs[0]+stairs[1], stairs[0] + stairs[2]) # (10 + 20) or (20 + 15) 중 큰 값
for i in range(3,n):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], # dp[0] + stairs[2] + stairs[1]
                dp[i-2] + stairs[i])

print(dp[n-1])
'''

N = int(input())

stair = [0] # 시작점 값
for _ in range(N):
    stair.append(int(input())) # [0, 10, 20, 15, 25, 10, 20]

if N == 1:
    print(stair[1])
else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

    print(dp[N])