n = int(input())
liss = []
for i in range(n):
    a, b = map(int,input().split())
    liss.append([a,b])


# liss.sort(key= lambda x: x[1]) 이건 왜 안되지? 해결 끝나는 시간이 같을 경우 더 빠른시간?에 시작하는거 정렬해 줘야해서 조건을 하나 추가해야함
# print(liss)
# liss.sort(key= lambda x : (x[0],x[1]))
liss.sort(key= lambda x : (x[1],x[0]))

print(liss)

cnt = 1
end_time = liss[0][1]

for i in range(1,n):
    if liss[i][0] >= end_time:
        cnt+=1
        end_time= liss[i][1]

print(cnt)
