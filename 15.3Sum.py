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


0 0 0 0 0

0 0     0
0   0   0
0     0 0
  0 0   0
方法1:
# 先取出两个数相加
  取相反数
  判断相反数是否在剩下的数组里 并且 该数字不在i之前的数组中
      输出三个数


滤重:
判断lst[j] 不属于 i+1 到j之间的集合

对第一个数滤重:i 之前没有和lst[i] 相等的
对第二个数滤重:j 之前没有和lst[j] 相等的 <=> lst[j]不属于 i +1 和 j -1 之间的值  lst[i +1, j]
                                           i +1 = j 时，上述条件成立 lst[i+1, j] == [],这个不影响
对第三个数滤重:写到这里,发现滤重条件太复杂，不妨换一种思路。


方法2
分类统计

{-1: 2, 0:1, 1:1, 2:1, -4:1}
字典中是否有3个0
取两个数 判断其相反数是否在字典中
取1个v>=2数 k * 2 判断其相反数是否在字典中

"""


def three_sum(nums):
    result = []
    dic = dict()

    # 分类统计出现次数
    for n in nums:
        dic[n] = 1 if n not in dic else dic[n] +1
    print dic

    # 如果0的个数>=3
    if 0 in dic:
        if 3 <=dic[0]:
            result.append([0, 0, 0])

    keys = dic.keys()
    lenkeys = len(keys)

    for i in range(lenkeys):

        # 取两个数，判断其相反数是否在字典的keys中
        for j in range(i +1, lenkeys):
            num = -(keys[i] +keys[j])
            if j +1 < lenkeys:
                if num in keys[j +1:]:
                    result.append([keys[i], keys[j], num])

        # 取一个出现次数>=2的数，乘以2,判断其相反数是否在字典的keys中
        if dic[keys[i]] >=2:
            num = - keys[i] * 2
            if num in keys[:i] or num in keys[i +1:]:
                result.append([keys[i], keys[i], num])
    return result

if '__main__' == __name__:

    print '\n\n******************\n', __doc__, '\n******************\n'
    #lst = [-1, 0, 1, -1, 2, -4]
    lst = [int(n) for n in raw_input('Please Input Some Numbers Seperated By Space Ending With Taping enter:\n').split(' ')]
    print three_sum(lst)
