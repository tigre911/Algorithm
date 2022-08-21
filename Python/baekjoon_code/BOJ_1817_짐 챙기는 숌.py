n , m = map(int,input().split())

if n == 0 :
    print(0)
    exit()

books = list(map(int,input().split()))
print(books)
cnt = 1
box = 0



for i in range(n):
    if books[i] + box > m:
        box = books[i]
        cnt += 1
    else:
        box += books[i]
print(cnt)