# travel
# -----------------
# 旅行商问题(分支定界法)
# -----------------
# Jackkii   20190608
#

city = []
citycost = []

class TreeNode:
    def __init__(self, key, parent=None, city=0):
        self.key = key
        self.parent = parent
        self.child = []
        self.city = city

    def minchild(self):                         # 找值最小的孩子节点
        minchild = self.child[0]
        minchild_index = 0
        for x in range(len(self.child)):
            if self.child[x].key <= minchild.key:
                minchild = self.child[x]
                minchild_index = x
        return minchild, minchild_index


class Travel:
    def __init__(self, N, m):
        self.root = None
        self.N = N
        self.m = m
        self.nowmin = 999999

    def findtwomin(self, ii):           # 给定某行，返回最小两个数
        min1 = 99999
        min2 = 99999
        for xx in range(self.m):
            if self.N[ii][xx] != 0:
                if self.N[ii][xx] < min1:
                    min2 = min1
                    min1 = self.N[ii][xx]
                elif min1 < self.N[ii][xx] < min2:
                    min2 = self.N[ii][xx]
        return min1, min2

    def findroot(self):         # 每个城市取最小的两条边相加向上取整
        countmin = 0
        for x in range(self.m):
            min1, min2 = self.findtwomin(x)
            countmin = countmin + min1 + min2
        self.root = TreeNode(countmin)

    def caldown(self, isuse):               # isuse中存了走过城市的序号
        travelmin = 0
        for x in range(1, self.m):          # 不考虑城市0
            if x in isuse:
                x_index = isuse.index(x)
                if x != isuse[-1]:          # 不是列表中的最后一个城市，即前后都有城市，两边均已确定
                    travelmin = travelmin + self.N[isuse[x_index-1]][x] + self.N[x][isuse[x_index+1]]
                else:                       # 列表中最后一个城市的下界两边分别为与相邻城市的一边加上最短边
                    mincost = 99999
                    for xx in range(self.m):
                        if xx != x and xx != isuse[-2]:     # 在排除自己与自己的0边，与相邻城市的一边的剩余所有边中找最小边
                            if mincost > self.N[x][xx]:
                                mincost = self.N[x][xx]

                    travelmin = travelmin + self.N[isuse[x_index-1]][x] + mincost

        yettravelmin = 0
        for x in range(self.m):  # 对剩下的城市计算距离最小的边
            if x not in isuse:
                yettravelmin = yettravelmin + sum(self.findtwomin(x))

        return (travelmin + yettravelmin)//2                # 下界为所有最小边之和除2取整 ？？？

    def buildlayer(self, currentnode, isarrive):
        if currentnode.key > self.nowmin:    # 如果当前下界小于可行解的实际cost，则不再继续
            return

        elif len(isarrive) == self.m:           # 如果到了最后一个城市，应加上去到城市0的cost
            global city, citycost
            currentnode.key = currentnode.key + self.N[isarrive[-1]][0]
            self.nowmin = min(currentnode.key, self.nowmin)     # 更新可行解下界最小值
            city.append(isarrive)               # 将可行解加入列表中

            sumcost = 0                      # 计算可行解的实际cost
            for x in isarrive[0:-1]:               
                x_index = isarrive.index(x)
                sumcost = sumcost + self.N[x][isarrive[x_index+1]]
            sumcost = sumcost + self.N[isarrive[-1]][0]
            citycost.append(sumcost)        # 加入可行解cost列表中

        else:
            for xx in range(self.m):            # 在当前城市遍历其他每一个未走过的城市
                if xx not in isarrive:
                    issarrive = isarrive.copy()
                    issarrive.append(xx)        # 将此城市加入已到达列表中

                    curmin = self.caldown(issarrive)   # 计算此节点下界

                    tempnode = TreeNode(curmin, parent=currentnode, city=xx)    # 创建节点
                    currentnode.child.append(tempnode)

            # 本层节点建立完成
            tempnode, tempnode_index = currentnode.minchild()       
            issarrive = isarrive.copy()
            issarrive.append(tempnode.city)
            self.buildlayer(tempnode, issarrive)            # 从最小孩子节点开始继续下一层建立

            for x in range(len(currentnode.child)):
                if x != tempnode_index:                     # 计算其他孩子节点
                    issarrive = isarrive.copy()
                    issarrive.append(currentnode.child[x].city)
                    self.buildlayer(currentnode.child[x], issarrive)


def printcity(city):        # 打印访问city的顺序
    for x in range(len(city)):
        print(city[x], end='')
        print('->', end='')
    print(0)


def findbest(city, citycost):       # 找可行解中的最优解       
    citycost1 = min(citycost)       # cost值最小的，可能对应几个访问顺序
    city1 = []
    for x in range(len(city)):
        if citycost[x] == citycost1:
            city1.append(city[x])
    citysorted = city1.copy()       # 按增序对访问城市的顺序进行排序
    citysorted.sort()                                   
    return citycost1, citysorted[0]

if __name__ == '__main__':
    m = eval(input())               # 旅行城市的数目
    C = []                          # 城市之间距离矩阵
    for _ in range(m):
        n1 = input().split(',')
        n1 = list(int(n1[x]) for x in range(len(n1)))
        C.append(n1)
    isarrive = [0]                   # 已到达城市列表
    mytravel = Travel(C, m)
    mytravel.findroot()
    mytravel.buildlayer(mytravel.root, isarrive)

    citycostbest, citybest = findbest(city, citycost)
    print(citycostbest)
    printcity(citybest)
    
