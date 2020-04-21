#!/usr/bin/python

def binToOther():
    bin = input("input binary number : ")

    D = int(bin,2) #2진수를 10진수로 바꿔준다.
    O = format(D,'o') #10진수를 8진수로 바꿔준다.
    H = format(D,'X') #10진수를 16진수로 바꿔준다.

    print("OCT >> ",O)
    print("DEC >> ",D)
    print("HEX >> ", H)

if __name__=='__main__':
    print("this is my_module.")

