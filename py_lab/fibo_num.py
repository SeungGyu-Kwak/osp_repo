#!/usr/bin/python

N = (int)(input("fibonacci Number ? " ))
answer = 0; f0 = 0; f1 = 1


if N < 1:
    print(f0)
    print("F%d = %d"%(N,f0))
elif N < 2:
    print(f1)
    print("F%d = %d"%(N,f1))
else:
    for i in range(1,N):
        if i<2:
            print(i,end=" ")
        answer = f1 + f0
        f0 = f1
        f1 = answer
        print(answer,end=" ")

    print()
    print("F%d = %d" %(N,answer))
