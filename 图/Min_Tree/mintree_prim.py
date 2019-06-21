# mintree_prim.py
# -----------------
# 使用prim算法求最小生成树
# -----------------
# Jackkii  20190621
#

num = eval(input())
mygraph = []   # 二维矩阵
nownode = list(range(num))      # 未加入最小生成树的结点集
mymintree = []          # 最小生成树集合
mymintreecost = 0

for x in range(num):            # 输入矩阵
    mygraph.append(list(map(int, input().split())))

mymintree.append(nownode.pop(0))

while len(nownode) != 0:        # 重复过程直到最小生成树包括图中所有顶点
    mincost = 65535
    minindex = 0
    for x in mymintree:         # 对每个最小生成树中的元素
        for y in nownode:       # 于当前非最小生成树顶点
            if 0 < mygraph[x][y] < mincost:     # 找最小边
                mincost = mygraph[x][y]
                minindex = y

    mymintree.append(minindex)                  # 将最小边即顶点加入最小生成树中
    nownode.pop(nownode.index(minindex))
    mymintreecost = mymintreecost + mincost

print(mymintreecost)
