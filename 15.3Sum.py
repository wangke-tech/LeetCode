#!/usr/bin/env python
# encoding: utf-8

"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
    [-1, -1, 2]
]

# 先取出两个数相加
  取相反数
  判断相反数是否在剩下的数组里 并且 该数字不在i之前的数组中
      输出三个数
# 去重
# [[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]

"""


def three_sum(lst):
    result = list()
    for i in range(len(lst)):
        for j in range(i +1, len(lst)):
            if j +1 < len(lst) -1:
                num = -(lst[i] +lst[j])
                if num in lst[j +1:] and num not in lst[:i]:
                    result.append([lst[i], lst[j], -(lst[i] +lst[j])])
    return result

if '__main__' == __name__:
    lst = [-1, 0, 1, -1, 2, -4]
    print three_sum(lst)



