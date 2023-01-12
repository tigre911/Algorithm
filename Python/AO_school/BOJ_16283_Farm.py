a, b, n, w = map(int, input().split())
# 양과 염소는 같은 사료를 먹고, 양 한 마리는 하루에 사료를 정확히 a 그램 먹고, 염소 한 마리는 하루에 정확히 b 그램을 먹는다고 한다.
# 양 사료 a , 염소 사료 b
# 양과 염소 전체가 n마리
# 어제 하루 동안 소비한 전체 사료의 양이 w그램
# a = 3 , b = 4 , n = 9 , w = 32
# w= (a*x) + (b*y)
x = 0
y= 0
ship, goat = 0,0
cnt = 0 # key point
for i in range(1,n):
    x = i
    y = n-i

    if w == (a*x) + (b*y) :
        ship = x
        goat = y
        cnt += 1

if cnt == 1:
    print(ship, goat)
else:
    print(-1)

