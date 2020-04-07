#!/usr/bin/python

N = (int)(input("input the N : "))
sum = 0
for i in range(N):
    s = int(input("input number : "))
    sum += s
aver = sum/N

print("average : ",aver)
