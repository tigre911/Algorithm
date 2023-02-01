import sys
# input = sys.stdin.readline
#
# 등차수열은 연속하는 두 항의 차이가 일정한 수열을 뜻한다. 연속한 두 항 중 뒷항에서 앞항을 뺀 값을 공차라고 한다.
# 초항이 a이고 공차가 d인 등차수열이 주어진다. 수열의 i번째 원소를
# Ai라 할 때, 다음 쿼리를 수행하는 프로그램을 작성하시오.

a, d = map(int, input().split())
#4 2
# 4 6 8 10 12 ****

#5 3

q = int(input())
#3

#2
q_li = [ list(map(int,input().split())) for _ in range(q)]
#1 1 1 => 4
# 1 1 2 => 4+6
# 2 1 2 => 4,6 의 최대 공약수 => 2
#[5,8,11,14,17,20,23,...]
#1 2 5 => 8 + 11 + 14 + 17 => 50
#2 3 6

max_val = max(q_li)[2]


arr = []
for m in range(max_val):
    arr.append(a + d*m)


for i in range(q):

    if q_li[i][0] == 1:
        cnt = 0
        for j in range(q_li[i][1]-1,q_li[i][2]):
            cnt += arr[j]
        print(cnt)

    else:
        def gcd_(arr):
            gcd=arr[q_li[i][1]]
            for k in range(q_li[i][1]-1,q_li[i][2]):
                gcd=gcd_(gcd,arr[k])
            print(gcd)
        # print(ans)

#출력
# 4
# 10
# 2

