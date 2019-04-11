# BSearch.py
# ----------------------
# 二分查找非递归解法，输入几组递增正整数数组及待查找的几个数(分别)
# ----------------------
# Jackkii 2019/4/11


def bsearch(numm, val):
    left, right = 0, len(numm)-1
    while left <= right:
        mid = (left + right) // 2
        if numm[mid] > val:
            right = mid - 1
        elif numm[mid] < val:
            left = mid + 1
        else:
            midd = mid
            while midd != 0 and numm[midd-1] == val:
                midd = midd - 1
            return midd
    return -1


N = eval(input())
num = []
for i in range(N):
    temp = list(input().split(','))
    temp = [int(x) for x in temp]
    num.append(temp)
for i in range(N):
    target = int(input())
    print(bsearch(num[i], target))

