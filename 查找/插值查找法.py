# 插值查找法.py
# ------------------------------------------------------
# 根据数据位置分布，利用公式预测数据所在未知，以二分方式渐渐逼近
# 需先经过排序， 时间复杂度取决于数据分布情况， 平均优于O(lgn)
# -------------------------------------------------------
# Jackkii   20190407
#

import random

def interpolation_search(data, val, low, high):
    mid = low
    if low < high and val != -1:
        # 插值查找法公式 让mid的值变化更接近关键字key
        mid = low + int((val-data[low]) / (data[high]-data[low]) * (high-low))
        # 原二分查找为 mid = low + 1/2*(high - low)

        if val == data[mid]:
            return mid
        elif val < data[mid]:
            return interpolation_search(data, val, low, mid-1)
        elif val > data[mid]:
            return interpolation_search(data, val, mid+1, high)
    return -1


# 产生50个1-150从小到大的随机数
data = [random.randint(1, 150) for _ in range(50)]
data.sort()

print('data为：')
for i in range(5):
    for j in range(10):
        print('%3d--%-3d' % (i*10+j+1, data[i*10+j]), end=' ')
print()

while True:
    val = int(input('请输入查找键值（1-150)，输入-1结束:'))
    if val == -1:
        break
    num = interpolation_search(data, val, 0, 49)
    if num == -1:
        print('未找到')
    else:
        print('在第%2d个位置找到"%3d"' % (num+1, data[num]))
