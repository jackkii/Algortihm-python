# FullArrange_recursion.py
# ------------------------
# 全排列(递归)
# ------------------------
# Jackkii     2019/03/29
#


def perm(n, begin, end):

    if begin >= end:                        # 当begin大于等于end时，即整个n已经交换好了
       print(n)
    else:h
        i = begin
        for _ in range(begin, end):
            n[_], n[i] = n[i], n[_]         # 第一次固定当前列表头元素，执行后面列表的全排列，
                                            # 第二次将当前列表头元素与下一元素交换，再执行后面列表的全排列......
            perm(n, begin+1, end)          
            n[_], n[i] = n[i], n[_]         # 将n恢复为最初的列表


num = eval(input())                         # 输入一个大于零的数字
n = list(range(1, num+1))                   # 生成一个1到n的顺序列表
perm(n, 0, len(n))                          # 对其进行全排列并打印
