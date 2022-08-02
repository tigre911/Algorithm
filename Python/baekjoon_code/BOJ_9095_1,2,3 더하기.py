t = int(input())

test_case = []

for _ in range(t):
    test_case.append(int(input()))

d = [0] * 11 # n은 양수이며 11보다 작다
d[1] = 1 # 1일때 1, -> 1가지 경우의 수
d[2] = 2 # 2일때 1+1 , 2, -> 2가지 경우의 수
d[3] = 4 # 3일때 1+1+1, 1+2 , 2+1 , 3 -> 4가지 경우의 수
d[4] = 7 # 4일때
d[5] = 13 # 5일때 1+1+1+1+1
d[6] = 24
d[7] = 44

for i in range(4,max(test_case)+1):
    d[i] = d[i-3] + d[i-2] + d[i-1] # 4 = 1 + 2 + 3

for j in test_case:
    print(d[j])