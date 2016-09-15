#!/usr/bin/env python
# encoding: utf-8

"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

# 2 3 4 5 9 2 3 1
# 从前往后求 存到一个数组 pre
# 从后往前求 存到一个数组 post
# 遍历i
    # lst1[i] *lst2[i]
"""


def main(lst):

    # 2 3 4 5
    # pre[i] = pre[i-1] * lst[i-1]
    # post[i] = post[i +1] *lst[i +1]
    # lenlst -1 =i:
    #    post[lenlst -1] = lst[

    lenlst = len(lst)
    pre, post = [1] *lenlst, [1] *lenlst
    result = list()

    for i in range(lenlst):
        rev_i = lenlst -1 -i
        if 0==i:
            pre[0] = 1
            post[rev_i] = 1
        else:
            pre[i] = pre[i -1] *lst[i -1]
            post[rev_i] = post[rev_i +1] *lst[rev_i +1]

    for i in range(lenlst):
        tmp = pre[i] * post[i]
        result.append(tmp)

    print 'pre', pre
    print 'post', post
    print 'result', result

    return result


if '__main__' == __name__:

    print '\n\n**********************\n'
    print __doc__
    print '**********************\n\n\n'

    lst = [int(n) for n in raw_input('Please input nums saperated by space,then tap enter.\nFor example: 3 5 6 1\n \n').split(' ')]

    main(lst)
