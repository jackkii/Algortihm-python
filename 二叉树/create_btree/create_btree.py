# Create_btree.py
# -----------------------
# 按层次排序构造二叉树
# -----------------------
# Jackkii   2019/05/26
#

class bTreeNode:
    def __init__(self, elem=None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class bTree:
    def __init__(self, data, root=None):
        self.root = root
        self.data = data

    def create_tree(self, node, i=0):
        if i >= len(self.data):           # 若指针指到最后一个元素
            return
        elif data[0] == '':              # 空树
            self.root = None
        else:                             # 若还有元素需要加入树中
            if self.data[i] != '#':
                node.elem = self.data[i]
                if 2*i+1 < len(data):      # 判断该节点是否有左孩子
                    node.lchild = bTreeNode()
                    self.create_tree(node.lchild, 2*i+1)    # 有则创建并赋值
                if 2*i+2 < len(data):      # 判断该节点是否有右孩子
                    node.rchild = bTreeNode()
                    self.create_tree(node.rchild, 2*i+2)


if __name__ == '__main__':
    data = input().split(' ')
    MyTree = bTree(data, bTreeNode())
    MyTree.create_tree(MyTree.root)

    N = int(input())
    for i in range(N):
        eval(input())
