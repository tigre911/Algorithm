a, b, c, n = map(int,input().split())
#5 9 12 113

cnt = 0

for i in range(1, (n//a)+1):
    for j in range(1, (n // b) + 1):
        for k in range(1, (n // c) + 1):
            if a*i + b*j + c*k == n :
                cnt = 1


print(cnt)