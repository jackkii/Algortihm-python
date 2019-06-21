# mintree_Kruskal.py
# ---------------------
# 最小生成树，使用kruskal算法
# ---------------------
# Jackkii   20190621
# 参考了fs的isCircle()函数判断回环

import copy
def isCircle(tuplelist, atuple):   # 检查是否回环
    o = atuple[0]               # 起点
    p = o                           
    d = atuple[1]               # 终点

    alist = [p]   # 存当前点的当前队列(从起点走到终点过程中)

    c = copy.deepcopy(tuplelist)
    while alist:
        cc = copy.deepcopy(c)
        p = alist.pop(0)        # 当前点
        for edge in cc:
            if p in edge:           
                if p == edge[0]:
                    alist.append(edge[1])
                else:
                    alist.append(edge[0])
                if d in alist:
                    return True     # 如果最小生成树中已有从起点走向终点路径，则会构成环
                c.remove(edge)      # 此边判断过了，移除
    else:
        return False

num = eval(input())
mygraph = []   # 二维矩阵
mydictgraph = {}
mymintree = []  # 最小生成树
mymintreecost = 0

for x in range(num):
    mygraph.append(list(map(int, input().split())))
    for y in range(num):
        if 0 < mygraph[x][y] < 65535:
            mydictgraph[(x, y)] = mygraph[x][y]     # 存每边对应权重入字典

mysortdict = sorted(mydictgraph.items(), key=lambda x: x[1])        # 对边权重进行排序

count = 0
for x in range(len(mysortdict)):
    if count < num-1 and not isCircle(mymintree, mysortdict[x][0]):        # 取最小权重边依次判断是否成环
        mymintree.append(mysortdict[x][0])
        mymintreecost = mymintreecost + mysortdict[x][1]
        count = count + 1

print(mymintreecost)
