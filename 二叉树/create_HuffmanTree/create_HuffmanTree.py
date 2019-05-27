# create_HuffmanTree.py
# ---------------------------------
# 构建哈夫曼树，并输出WPL，带权路径和
# ---------------------------------
# Jackkii       2019/05/27
#


class HuffmanTreeNode:
    def __init__(self, key, lchild=None, rchild=None, parent=None):
        self.key = key
        self.leftchild = lchild
        self.rightchild = rchild
        self.parent = parent

    def isleaf(self):
        return not self.leftchild and not self.rightchild


class HuffmanTree:
    def __init__(self, root=None):
        self.root = root
        self.Trees = []

    def datainsert(self, key):              # 初始将data中数值转为结点放入列表self.Trees中
        newNode = HuffmanTreeNode(key)
        self.Treesappend(newNode)

    def Treesappend(self, Node):            # 考虑key值大小的插入
        for x in range(len(self.Trees)):    # 遍历列表（从小到大），找到合适key值位置插入
           if Node.key < self.Trees[x].key:
                self.Trees.insert(x, Node)
                break
        if len(self.Trees) == 0 or Node.key > self.Trees[-1].key:   # 若空表或整个列表中元素都比key小，则插到最后一位
           self.Trees.append(Node)

    def create_Huffman(self):               # 构建树，从Trees列表中取出两个权值最小的，构建新树（值为二者相加，小的为左子树）
        while len(self.Trees) > 1:          # 当列表有两个结点以上时
            Node1 = self.Trees.pop(0)
            Node2 = self.Trees.pop(0)
            if Node1.key < Node2.key:
                newNode = HuffmanTreeNode(key=Node1.key+Node2.key, lchild=Node1, rchild=Node2)
            else:
                newNode = HuffmanTreeNode(key=Node1.key+Node2.key, lchild=Node2, rchild=Node1)
            self.Treesappend(newNode)       # 插入新树的结点

        self.root = self.Trees[0]       # 将列表构建完成的树的根节点赋给root

    def cal_WPL(self, node, x):         # 计算带权路径和
        if node.isleaf():               # 若是叶子节点，则返回路径长度乘权值
            return x*node.key
        else:                           # 若不是叶子，则继续向下前进
            return self.cal_WPL(node.leftchild, x+1)+self.cal_WPL(node.rightchild, x+1)


if __name__ == '__main__':
    data = input().split()              # 输入一串初始哈夫曼树的数字
    data = [int(data[x]) for x in range(len(data))] 
    myhtree = HuffmanTree()             
    for x in range(len(data)):          # 创建各权值结点
        myhtree.datainsert(data[x])
    myhtree.create_Huffman()            # 建树
    WPL = myhtree.cal_WPL(myhtree.root, 0)  # 从根节点出发计算带权路径和
    print(WPL)
