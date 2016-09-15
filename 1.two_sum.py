#!/usr/bin/env python
# encoding: utf-8

""" 1.Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if target == nums[i] +nums[j]:
                return [i, j]

if '__main__' == __name__:
    nums = [2, 7, 11, 15]
    target = 9
    print two_sum(nums, target)
