# fs_mintree_K
# 20190621

import copy

def Kruskal(mat):   # mat 是邻接矩阵
    n = len(mat)  # 顶点数
    edges = {}    # 总的边集和权重，字典
    for i in range(n):
        for j in range(i+1, n):    # 上三角
            if i != j:
                edges[(i+1, j+1)] = mat[i][j]

    SortedEdges = sorted(edges.items(), key=lambda x: x[1])

    E = []  # 已添加的边
    totalCost = 0
    for x in SortedEdges:
        if E == []:
            E.append(x[0])
            totalCost += x[1]
        else:
            if isCircle(E, x[0]) == True:
                continue
            else:
                E.append(x[0])
                totalCost += x[1]
            if len(E) == n-1:
                break
    if len(E) == 1:
        totalCost = 0

    return totalCost

def isCircle(tuplelist, atuple):   # 检查是否回环
    o = atuple[0]
    p = o
    d = atuple[1]

    alist = [p]   # 从起点出发能到达额点, 队列

    c = copy.deepcopy(tuplelist)
    while alist:
        cc = copy.deepcopy(c)
        p = alist.pop(0)
        for edge in cc:
            if p in edge:
                if p == edge[0]:
                    alist.append(edge[1])
                else:
                    alist.append(edge[0])
                if d in alist:
                    return True
                c.remove(edge)
    else:
        return False




if __name__ == '__main__':
    N = eval(input())
    mat = []

    for _ in range(N):
        mat.append(list(map(int, input().split())))

    minCost = Kruskal(mat)
    print(minCost)
