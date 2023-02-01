a, b = map(int, input().split())
Ans=0
cnt = 0
for i in range(a, b + 1):
    temp=1
    while temp<=i:
        if i%temp==0:
            cnt=temp
        temp*=2
    Ans+=cnt
print(Ans)