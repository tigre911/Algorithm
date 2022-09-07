t = int(input())
arr=[]
for i in range(t):
    arr.append(int(input()))

dp = [0]*101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2 #dp
dp[5] = 2 #dp[]


for i in range(6,max(arr)):
    dp[i] = dp[i - 1] + dp[i - 5]

'''
dp[6] = 3 #dp[5] + dp[1]
dp[7] = 4
dp[8] = 5
dp[9] = 7
dp[10] = 9
dp[11] = 12 #dp[10] + dp[6]
dp[12] = 16 #dp[11] + dp[7]'''

for lst in arr:
    if lst>5:
        dp[lst] = dp[lst-1] + dp[lst-5]
        print(dp[lst])
    elif lst==4 or lst == 5:
        print(2)
    else:
        print(1)