
n = int(input())

cnt = 0

for i in range(1, n+1): # 택희
    for j in range(1, n+1): # 영훈
        for k in range(1, n+1): # 남규
            #조건에 반하는 결과일때 지나간다
            if i + j + k !=n:
                continue
            if k < j+2: #남규는 영훈이보다 2개 이상 많은 사탕을 가져야 한다.
                continue
            if i % 2 == 1: #택희가 받는 사탕의 수는 홀수개가 되어서는 안 된다.
                continue

            cnt+=1

print(cnt)