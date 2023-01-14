li = [int(input()) for _ in range(10)]

print(li)

sum_li = 0


for i in range(len(li)):
    sum_li += li[i]
    if sum_li >= 100:
        if sum_li - 100 > 100 - (sum_li - li[i]): # 합 - 100 > 100 - (합 - 현재 리스트의 숫자)
            sum_li -= li[i]
        break


print(sum_li)