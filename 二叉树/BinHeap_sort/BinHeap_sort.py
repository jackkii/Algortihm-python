# BinHeap_sort.py
# ------------------------------
# 最大堆的构建，堆排序找出第k个最大值
# ------------------------------
# Jackkii       2019/05/27
#

class BinHeap:
    def __init__(self):
        self.heapList = [0]  # 堆可由列表实现，堆的头结点储存在列表[1]位置处
        self.currentSize = 0  # 实际堆中元素个数，为len(heapList)-1

    def insert(self, k):  # 插入（尾端）
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)  # 需进行上浮操作，不断与父节点比较

    def percUp(self, ii):  # 上浮
        while ii // 2 > 0:  # 插入的节点有父节点
            if self.heapList[ii] > self.heapList[ii // 2]:  # 交换次序
                self.heapList[ii // 2], self.heapList[ii] = self.heapList[ii], self.heapList[ii // 2]
            ii = ii // 2  # 不断与父节点比较，直到根节点（根节点为最大堆中最大值）

    def delmax(self):  # 删除最大值，将最后一个叶子节点放至根节点，再依次与值大的孩子交换
        heapmax = self.heapList[1]  # 列表[1]为最大堆的根节点
        self.heapList[1] = self.heapList[-1]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()  # 删除最后一个节点数值（已放至根结点处）
        self.percDown(1)  # 进行下沉操作，将最大值换到根结点处
        return heapmax

    def percDown(self, ii):  # 下沉
        while (ii * 2) <= self.currentSize:  # 如果有孩子
            maxchild = self.maxChild(ii)  # 找到左右孩子中大的一个的位置
            if self.heapList[ii] < self.heapList[maxchild]:  # 如果ii的孩子大于ii，则交换
                self.heapList[ii], self.heapList[maxchild] = self.heapList[maxchild], self.heapList[ii]
            ii = maxchild  # 不管有无交换，都要向下遍历

    def buildHeap(self, alist):  # 将一个完全二叉树的列表转为最大堆
        self.currentSize = len(alist)
        self.heapList = [0] + alist  # 0处不存节点
        m = len(alist) // 2  # 完全二叉树有一半叶子节点，一半父节点，不断将父节点进行下沉操作
        while m > 0:
            self.percDown(m)
            m = m - 1

    def maxChild(self, n):  # 返回当前结点的孩子节点中值大的一个的位置
        if 2 * n + 1 > self.currentSize or self.heapList[2 * n] > self.heapList[2 * n + 1]:
            return 2 * n
        return 2 * n + 1


if __name__ == '__main__':
    data = input().split(',')  # 输入完全二叉树列表
    data = [int(data[x]) for x in range(len(data))]
    mybinheap = BinHeap()
    mybinheap.buildHeap(data)  # 从完全二叉树转换为最大堆

    k = eval(input())
    for x in range(k-1):
        mybinheap.delmax()
    print(mybinheap.delmax())







