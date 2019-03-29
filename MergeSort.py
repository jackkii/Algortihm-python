# MergeSort.py
# --------------------------
# 归并排序
# -------------------------
# Jackkii    20190321
#

import math

def Merge(left, q, right, A_num):
    # 排序函数
    # 输入：数组A_num和最左，中间和最右元素下标
    # 输出：排好序的数组A_num
    L = A_num[left : q+1]       # 左数组
    R = A_num[q+1 : right+1]    # 右数组
    L.append(10001)             # 待排序数组中数字均小于10001
    R.append(10001)
    i = 0
    j = 0
    for x in range(left,right+1):   # 将左右数组中小的数字放入A_num数组中
        if L[i] <= R[j]:
            A_num[x] = L[i]
            i += 1
        else:
            A_num[x] = R[j]
            j += 1

def MSort(left, right, A_num):   
    # 归并排序递归函数
    # 输入：数组A_num及最左最右元素下标
    if left < right:                      # 若左下标大于等于右下标，则只有一个元素，即已排好序
        q = math.floor((left+right)/2)    # 将数组对半分为两个子数组
        MSort(left, q, A_num)             # 左数组排序
        MSort(q+1, right, A_num)          # 右数组排序
        Merge(left, q, right, A_num)      # 将左右数组合并为A_num

K=eval(input())                     # K为待排序数组个数
for x in range(K):                  # 执行K次排序
    num = list(input().split())  # 得到list数组（中间元素为string类）
    num = [int(x) for x in num]    # 将元素转换为int型                     
    MSort(0,len(num)-1,num)           # 归并排序
    print(num)                        # 打印排好序的数组

