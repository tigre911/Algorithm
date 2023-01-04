n = int(input())

ans_li = list(map(int,input().split()))

cnt = 0
cnt_li = []

for i in range(1,max(ans_li)+1): # 1 2 3 4 5 6 7 8 9
    cnt = 0 # 초기화 시켜주는 곳
    for j in ans_li: # 5 1 7 9
        cnt += abs(i-j)
    cnt_li.append(cnt)

# print(cnt_li)
#
# print(min(cnt_li))

print(cnt_li.index(min(cnt_li)) + 1)


# 위쪽이  시간초과로 틀린코드

# 정답코드

n = int(input())
a = list(map(int, input().split()))
a.sort()

# 중간값(median)을 출력
print(a[(n - 1) // 2])
