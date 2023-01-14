n, m, k = map(int, input().split())
# n = 6 ,m = 3 ,k =2
# n 여학생 수 ,m 남학생수 ,k명은 반드시 인턴십 참여해야함(인턴십 참여하면 대회 참여 불가)
# 2명의 여학생과 1명의 남학생이 팀

cnt = 0
for i in range(1,(n+m)//3+1):
    # print((n - 2*i) + (m - i) - k)
    if (n - 2*i) + (m - i) - k >= 0:
        if (n - 2*i)>=0 and (m - i)>=0:
            cnt +=1

print(cnt)