n = int(input())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n: # 122333444455555
        start = mid + 1
    else:
        end = mid - 1

print(start)