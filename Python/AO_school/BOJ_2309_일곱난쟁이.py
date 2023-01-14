li = []

for i in range(9):
    li.append(int(input()))

li.sort()

print(li)

sum_li = sum(li)

for i in range(9):
    for j in range(i+1, 9):
        if sum_li - li[i] - li[j] == 100:
            print(li[i], li[j])
            a = li[i]
            b = li[j]

            # li.remove(li[i])

            break
li.remove(a)
li.remove(b)
print(*li)