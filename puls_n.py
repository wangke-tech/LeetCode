#!/usr/bin/env python
# encoding: utf-8
""" 加一个数
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list
"""


def plus(lst, index=0, n=1):
    if index != len(lst) -1:
        lst[index +1] += lst[index] /10
        lst[index] = lst[index] %10
        plus(lst, index +1, n)
    return lst


def clean(lst):
    if lst[-1] > 9:
        lst1 =[int(_) for _ in str(lst[-1])]
        del lst[-1]
        lst1.reverse()
        lst.extend(lst1)
    return lst

if '__main__' == __name__:

    lst, n = [int(_) for _ in raw_input("input a list").split(' ')], int(raw_input('input n'))
    lst.reverse()
    lst[0] += n
    lst = plus(lst)
    lst = clean(lst)
    lst.reverse()
    print lst
