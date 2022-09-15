n = (input())
s = input()
cnt = 0
i = 0
while i <= len(n)-len(s):
    print(n[i:len(s)+i])
    if s == n[i:len(s)+i] :
        cnt +=1
        i += len(s)
    else:
        i += 1
print(cnt)