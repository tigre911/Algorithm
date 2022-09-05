n =input().split('-')
print(n)
lst = []

for i in n:
    cnt = 0
    temp = i.split('+')
    print(f'temp : {temp}')
    for j in temp:
        cnt += int(j)
    lst.append(cnt)
print(f'lst :  {lst}')

ans = lst[0]
for i in range(1,len(lst)):
    ans -= lst[i]

print(ans)