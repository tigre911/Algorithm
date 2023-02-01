a, b = map(int, input().split())

while a % b != 0:

    temp = a % b #나머지

    print(a, b, temp)

    a = b
    b = temp

print(b)