url = 'https://www.acmicpc.net/problem/6236'

'''
현우는 용돈을 효율적으로 활용하기 위해 계획을 짜기로 하였다. 
현우는 앞으로 N일 동안 자신이 사용할 금액을 계산하였고, 돈을 펑펑 쓰지 않기 위해 정확히 M번만 통장에서 돈을 빼서 쓰기로 하였다. 
현우는 통장에서 K원을 인출하며, 통장에서 뺀 돈으로 하루를 보낼 수 있으면 그대로 사용하고, 
모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원을 인출한다. 
다만 현우는 M이라는 숫자를 좋아하기 때문에, 
정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다. 
현우는 돈을 아끼기 위해 인출 금액 K를 최소화하기로 하였다. 
현우가 필요한 최소 금액 K를 계산하는 프로그램을 작성하시오.
'''
'''
입력
1번째 줄에는 N과 M이 공백으로 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ M ≤ N)

2번째 줄부터 총 N개의 줄에는 현우가 i번째 날에 이용할 금액이 주어진다. (1 ≤ 금액 ≤ 10000)
'''

n , m = map(int, input().split())

money = []
for _ in range(n):
    money.append(int(input()))
summy = sum(money)
start, end = 0, summy
result = summy

while start <= end:
    mid = (start + end) // 2
    temp = mid
    flag = False
    cnt = 1
    for i in range(n):
        if mid < money[i]:
            flag = True
            break
        if temp < money[i]:
            temp = mid
            cnt += 1
        temp -= money[i]

    if flag == False:
        if cnt <= m:
            end = mid - 1
            if mid < result:
                result = mid
        else:
            start = mid + 1
    else:
        start = mid + 1

print(result)


