a = int(input())

a_list = list(map(int,input().split()))
#[1, 100, 2, 50, 60, 3, 5, 6, 7, 8]
dp=[0] * (a+1)

print(a_list)

ans = 0

dp[0]= a_list[0] #1

for i in range(1,a):
    for j in range(i):
        if a_list[i] > a_list[j]: # a_list[1] > a_list[0] 뒷자리 숫자가 앞자리 수보다 크다면
            dp[i] = max(dp[i], dp[j] + a_list[i]) #max(dp[1] , dp[0] + a_list[1]) -> dp[1] = 101
            print(i, j)
            print(f"for문안에서 dp{i} : ",dp[i])                                      #dp[2]=0
            print(f'(dp[{i}] : {dp[i]} , dp[{j}] + a_list[{i}] : {dp[j]} + {a_list[i]} )')
                                                  #max(dp[3] , dp[2] + a_list[3]) -> dp[3]=0 + 50
        else:
            dp[i] = max(dp[i],a_list[i]) # dp[2] = 2
            print(i, j)
            print(f"여긴 esle for문안에서 dp{i} : ", dp[i])

for b in range(a+1):
    print(f'dp{b} : {dp[b]}')

print(max(dp))