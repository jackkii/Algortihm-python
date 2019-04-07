# FullArrange_deep.py
# ---------------------------
# 全排列（深度搜索）画深度搜索图理解
# ---------------------------
# Jackkii   2019/03/29
#


def fullarrange_deep(pointer):

    if pointer == len(arr):                 # 若指针指向列表最后一个元素的下一个空地方（实际仅是计数器，并不是指针）
        print(temp)                         # 打印存储完所有数字的临时列表
        return

    for _ in range(0, len(arr)):            # 相当于省略else
        if visit[_] is True:                # 如果当前位置_为True,则可访问
            temp[pointer] = arr[_]          # 将元素存在临时列表中, pointer为临时列表的位置计数器
            visit[_] = False                # 将此元素所在位置_改为False
            fullarrange_deep(pointer + 1)   # 指针指向下一位置
            visit[_] = True                 # 递归调用完成，即此元素之后的小列表的全排列都排好了，将此元素所在位置改回True


n = eval(input())                           # 输入一个大于0的数字
arr = list(range(1, n+1))                   # 生成一个1到n的列表
visit = [True for x in range(0, n)]         # 生成该列表对应的bool元素可访问列表
temp = ['' for xx in range(0, n)]           # 生成一个临时列表存储全排列后数字
fullarrange_deep(0)                         # 全排列，指针从第一个元素开始
