#QuickSort.py
#-----------------------
#快速排序,取三数中值作为pivot
#        且无论元素多少都使用快排
#-----------------------
#Jackkii   20190321
#

import math

def Median3(A_num, left, right):
    #使用三数中值分割法选取枢纽元（pivot)
    #即取左端，右端，中间元素的中值作为枢纽元
    
    center = math.ceil((left+right)/2) #取中间值(用floor也可）
    #排序三个数字
    if A_num[left] > A_num[center]:
        A_num[left], A_num[center] = A_num[center], A_num[left]
    if A_num[left] > A_num[right]:
        A_num[left], A_num[right] = A_num[right], A_num[left]
    if A_num[center] > A_num[right]:
        A_num[right], A_num[center] = A_num[center], A_num[right]

    #将中值放至倒数第二个元素，隐藏pivot
    A_num[right-1], A_num[center] = A_num[center], A_num[right-1]
    #返回中值，即pivot
    return A_num[right-1]  

def partition(A_num, left, right):
    #分组函数，以pivot为界，小于pivot的元素放左数组，大于pivot的元素放右数组
    #返回分组后pivot的下标
    
    if left == right-1:
        #若数组中只有两个元素，则无需取中值
        if A_num[right] < A_num[left]:
            A_num[right], A_num[left] = A_num[left], A_num[right]
        return left
    else:
        i = left
        j = right - 1
        pivot = Median3(A_num, left, right)
        while 1:
            i += 1
            j -= 1 
            while i <= right - 1 and A_num[i] < pivot:
                i += 1        #在左边若有大于等于pivot的元素
            while j >= 0 and A_num[j] > pivot:
                j -= 1        #在右边若有小于等于pivot的元素
            if i < j:         #若i,j不交错则二者交换
                A_num[j], A_num[i] = A_num[i], A_num[j]
            else:             #i,j交错则已完成分组
                break
        
        # 将pivot交换至中间
        A_num[i], A_num[right - 1] = A_num[right - 1], A_num[i]
        #返回pivot下标
        return i             

#快速排序
def QSort(A_num, left, right):
    if left < right:          #若数组中元素多于1个，则排序
        pivot = partition(A_num, left, right)
        #排序左右子数组
        QSort(A_num, left, pivot-1)
        QSort(A_num, pivot+1, right)




K=eval(input())                 #K为待排序数组个数
for x in range(K):              #执行K次排序
    num = list(input().split()) #得到list数组（元素为string型）
    num = [int(x) for x in num]   #转换string为int
    QSort(num, 0, len(num)-1)     #快速排序
    print(num)
