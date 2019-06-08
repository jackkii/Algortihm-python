# 01Knapsack
# ----------------------------
# 01背包问题
# ---------------------------
# Jackkii    2019/06/08
#


def createK(W, n, w, v):
    # 构建k表: 背包各重量下所能达到的最大价值
    # W: 背包可容纳最大重量
    # n: n件物品
    # w: n件物品的重量列表
    # v: n件物品的价值列表
    k = list(list(0 for _ in range(0, n+1)) for __ in range(0, W+1))   # 创建二维数组储存表，行为0~W,列为0~n
    for x in range(1, W+1):                                            # 遍历每一个重量
        for j in range(1, n+1):                                        # 遍历每一个可能物品
            k[x][j] = k[x][j-1]                                        # 当此时物品重量大于背包重量时，背包只能放进前一个物品
            if w[j-1] <= x:                                            # 当此时物品重量小于背包重量时，比较放进前后总价值
                k[x][j] = max(k[x][j], k[x-w[j-1]][j-1]+v[j-1])        # 满背包重量减去此物重量时背包价值+此物价值
    return k                                                           # 返回k表，最尾元素为所求最大价值k[W][n]


def finditem(W, n, item, w, v, k):
    # 找到该重量背包达到对应最大价值时，放进背包的物品
    # W: 背包重量
    # n: 物品数量
    # item: 该重量背包对应最大价值时，n件物品分别是否放进背包中（0-1列表）
    # w: n件物品的重量列表
    # v: n件物品的价值列表
    # k: 书包各重量对应最大价值表
    if n >= 0:                                  # 更新item列表从n开始直到0，item[0]一直为0
        if k[W][n] == k[W][n-1]:                # 此时价值与前一个物品价值相等
            item[n] = 0                         # 第n件物品未放进背包中
            finditem(W, n-1, item, w, v, k)     # 寻找n-1物品是否放进
        elif W-w[n-1] >= 0 and k[W][n] == k[W-w[n-1]][n-1] + v[n-1]:        # 若此时背包可装得进前一物品，且加了此物品价值
            item[n] = 1                                                     # 装进了此物品
            finditem(W-w[n-1], n-1, item, w, v, k)                          # 寻找减去此物品重量的背包的最大价值对应的物品


if __name__ == '__main__':
    N = eval(input())
    W = eval(input())
    w = input().split()
    w = list(int(w[x]) for x in range(len(w)))
    v = input().split()
    v = list(int(v[x]) for x in range(len(v)))
    k = createK(W, N, w, v)
    print(k[W][N])
    item = list(0 for x in range(N+1))
    finditem(W, N, item, w, v, k)
    for x in range(len(item)):          输出对应物品序号（1开始）
        if item[x] == 1:
            print(x, end=' ')



