# Task_assignment
# ---------------------
# 使用分支定界法解任务分配问题
# --------------------
# Jackkii       20190608
#

Task = []           # 存储可行解
Taskcost = []       # 存储可行解对应cost


class TreeNode:
    def __init__(self, key, parent=None, task=0):
        self.key = key                  # key存储每个结点下界
        self.parent = parent
        self.child = []
        self.task = task                # task 为此节点表示本层人被分配到的任务

    def minchild(self):                 # 返回最小孩子结点，及其下标位置（剪枝）
        minchild = self.child[0]
        minchild_index = 0
        for x in range(len(self.child)):
            if self.child[x].key <= minchild.key:
                minchild = self.child[x]
                minchild_index = x
        return minchild, minchild_index


class BranchAndBound:
    def __init__(self, N, n):
        self.root = None
        self.N = N              # cost矩阵
        self.n = n              # cost矩阵维数
        self.nowmin = 999999    # 现行解的最小cost

    def findroot(self):         # 确定所有人任务分配的最小下界，并赋值给root
        countmin = 0
        for x in range(len(self.N)):  # 对每个人取最小的cost相加为下界
            countmin = countmin + min(self.N[x])
        self.root = TreeNode(countmin)

    def caldown(self, isuse):   # 计算此节点之后任务分配的cost下界, isuse为已分配任务列表
        ii = len(isuse)         # 分配了多少个任务，现在就该下一个人了（下标-1再+1）
        nodecostmin = 0
        for x in range(ii, self.n):             # 对余下每个人遍历
            curmin = 99999
            for xx in range(self.n):            # 对每个任务遍历，找未被分配任务的cost最小值
                if xx not in isuse and curmin > self.N[x][xx]:  # 若任务未被分配，
                    curmin = self.N[x][xx]
            nodecostmin = curmin + nodecostmin                  # 将每个人最小cost相加
        return nodecostmin                      # 返回得此结点往后的最小cost

    def buildlayer(self, currentnode, isuse):   # 建立每一层的各个结点（广度优先）
        if currentnode.key > self.nowmin:   # 若currentnode的下界已经大于可行解的实际cost值，不继续进行计算
            return

        elif len(isuse) == self.n:          # 传进来叶子节点，同时currentnode.key小于nowmin
            global Task, Taskcost
            self.nowmin = currentnode.key   # 更新最小值
            Task.append(isuse)              # 将可行解存入

            sumcost = 0                     # 存入可行解对应的实际cost值
            for x in range(self.n):
                sumcost = sumcost + self.N[x][isuse[x]]
            Taskcost.append(sumcost)

        else:
            for xx in range(self.n):        # 遍历每一个未被分配任务
                if xx not in isuse:
                    issuse = isuse.copy()
                    issuse.append(xx)       # 将分配的任务加入列表中(python中为引用，为不改变isuse，选择copy())

                    curmin = self.caldown(issuse) # 计算节点下界，已分配任务cost+未分配任务最小值
                    for ii in range(len(issuse)):
                        curmin = curmin + self.N[ii][issuse[ii]]

                    tempnode = TreeNode(curmin, parent=currentnode, task=xx)
                    currentnode.child.append(tempnode)  # 将结点添加进当前结点的孩子列表中

            # 本层结点建立完成
            tempnode, tempnode_index = currentnode.minchild()       # 先计算最小孩子结点，以便得到nowmin，
            issuse = isuse.copy()                                   # 之后可以减少其他节点计算量
            issuse.append(tempnode.task)
            self.buildlayer(tempnode, issuse)

            for x in range(len(currentnode.child)-1):               # 返回此层，计算其他节点下界
                if x != tempnode_index:
                    issuse = isuse.copy()
                    issuse.append(currentnode.child[x].task)
                    self.buildlayer(currentnode.child[x], issuse)


if __name__ == '__main__':
    n = eval(input())       # n个任务n个人
    N = []                  # cost矩阵
    for _ in range(n):
        n1 = input().split()
        n1 = list(int(n1[x]) for x in range(len(n1)))
        N.append(n1)
    isuse = []              # 已分配任务列表
    myBAB = BranchAndBound(N, n)
    myBAB.findroot()
    myBAB.buildlayer(myBAB.root, isuse)

    taskcost = min(Taskcost)        # 可行解中最小cost值，暂时不知道会有几个可行解
    print(taskcost)
    taskcost_index = Taskcost.index(taskcost)
    task = list(Task[taskcost_index][x]+1 for x in range(n))
    print(task)
