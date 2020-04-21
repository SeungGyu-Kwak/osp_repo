#!/usr/bin/python

def UnionIntersection():
    list1 = list(map(int,input("1st list: ").replace('[','').replace(']','').split(',')))
    list2 = list(map(int,input("2nd list: ").replace('[','').replace(']','').split(',')))

    unionlist = list(set(list1).union(list2))
    unionlist.sort()

    print("union",unionlist)

    intersection = list(set(list1).intersection(list2))
    intersection.sort()

    print("intersection",intersection)
