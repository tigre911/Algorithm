import sys
input = sys.stdin.readline

n = int(input())

m = list(map(int,input().split()))

print(m)
money = int(input())

sum = sum(m)

print(sum)

max_money = max(m)
min_money = 0

# print(f'max  : {max_money}')

while max_money >= min_money:
    mid = (max_money + min_money)//2
    print(f'mid : {mid}')
    res = 0
    print(f'res : {res}')
    for i in m:
        if i >= mid:
            res += mid
        else:
            res += i

    if res <= money:
        min_money = mid + 1
    else:
        max_money = mid - 1

print(max_money)

# while sum > money:
#     m.sort(reverse=True)
#     max_money = max(m)
#     max_money -= 1
#     m[0] = max_money
#     sum -= 1
#
# # print(sum)
# print(max_money)