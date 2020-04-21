#!/usr/bin/python

import my_pkg

if __name__== '__main__':
    
    while True:
        print("Select menu: 1)conversion 2)union/intersection 3)exit? ")
        num = int(input(">>"))

        if (num == 1):
            my_pkg.binToOther()
        elif (num == 2):
            my_pkg.UnionIntersection()
        elif (num == 3):
            print("exit the program..")
            break
        else:
            print("Wrong number. Input the number in (1~3)")



