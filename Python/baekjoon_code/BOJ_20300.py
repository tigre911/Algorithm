# -*- coding: utf-8 -*-

'''n = int(input())
sonsil = list(map(int,input().split()))

sonsil.sort()

print(sonsil)
if n>1:
    cnt = sonsil[(n//2)-1] + sonsil[n//2]
else:
    cnt = sonsil[0]
print(cnt)
'''
import sys

input = sys.stdin.readline

N = int(input())

sonsil = list(map(int, input().split()))

sonsil.sort() # 정렬

i = 0 # 손실 리스트의 첫번째 인덱스
j = N - 1 # 손실 리스트의 마지막 인덱스
max_loss = 0 # 구하려는 근손실 값

if N % 2 == 1: # 홀수일 때
    j = N - 2
    max_loss = sonsil[-1] # 마지막 인덱스 값이 최소?

while i < j:
    max_loss = max(max_loss, sonsil[i] + sonsil[j])
    i += 1
    j -= 1
print(max_loss)