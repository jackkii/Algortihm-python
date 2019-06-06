# unboundedKnapsack
# ----------------------------
# 无限背包问题
# ---------------------------
# Jackkii    2019/06/06
#


def unboundedKnapsack(W, n, w, v):          # W为背包重量，n为物品数量，w为物品重量的列表，v为物品价值的列表
    k = list(0 for _ in range(0, W+1))      # 创建初始列表k，存放每一重量下背包可存放的物品的最大总价值
    for x in range(1, W+1):                 # 循环每种重量
        for ii in range(0, n):              # 每种重量尝试每种不同物品
            if w[ii] <= x:  
                k[x] = max(k[x], k[x - w[ii]] + v[ii])  # 若values值大于前一种，则替换
    return k[W]                             # 返回所求重量下的最大value


if __name__ =='__main__':
    N = eval(input())
    W = eval(input())
    w = input().split()
    w = list(int(w[x]) for x in range(len(w)))
    v = input().split()
    v = list(int(v[x]) for x in range(len(v)))
    k = unboundedKnapsack(W, N, w, v)
    print(k)


