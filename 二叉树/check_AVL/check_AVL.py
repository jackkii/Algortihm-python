# check_AVL.py
# --------------------------
# 判断给定层序序列，判断是否是AVL树
# --------------------------
# Jackkii   2019/05/28
#

class bsTreeNode:
    def __init__(self, key=None, lchild=None, rchild=None, parent=None, ldepth=0, rdepth=0, bfactor=0):
        self.key = key
        self.leftchild = lchild
        self.rightchild = rchild
        self.parent = parent
        self.rdepth = rdepth
        self.ldepth = ldepth
        self.balancefactor = bfactor

class bsTree:
    def __init__(self, data, root=None):
        self.root = root
        self.data = data

    def create_tree(self, node, i=0):                   # 创建二叉搜索树，给定层序数组时
        if i >= len(self.data):
            return
        elif self.data[0] == '':
            self.root = None
        else:
            if self.data[i] != '#':
                node.key = self.data[i]
                if 2*i+1 < len(self.data):
                    node.leftchild = bsTreeNode()
                    self.create_tree(node.leftchild, 2*i+1)
                if 2*i+2 < len(self.data):
                    node.rightchild = bsTreeNode()
                    self.create_tree(node.rightchild, 2*i+2)

    def updatedepth(self, node):                       # 计算这个树每个结点的左高度，右高度，balancefactor
        if node and node.key is not None:
            node.ldepth = self.updatedepth(node.leftchild)
            node.rdepth = self.updatedepth(node.rightchild)
            node.balancefactor = node.ldepth - node.rdepth
            return max(node.rdepth, node.ldepth)+1      # 左右较大的树高加上本层高度1为此结点高度
        else:
            return 0


def inorder(bsTreeNode, stack=[]):                      # 中序遍历
    if bsTreeNode:
        inorder(bsTreeNode.leftchild, stack)
        if bsTreeNode.key is not None:
            stack.append(bsTreeNode.key)
        inorder(bsTreeNode.rightchild, stack)

def isbstree(mytree):                                   # 判断是否是二叉搜索树
    stack = []
    inorder(mytree.root, stack)                         # 判断中序遍历是否是有序的
    stack_order = stack.copy()
    stack_order.sort()
    if stack == stack_order:
        return True
    return False

def isAVL(mytreenode, x=True):                               # 判断是否是AVL树
    if mytreenode:                                      # 遍历所有结点的balancefactor
        if -1 <= mytreenode.balancefactor <= 1:
            x = isAVL(mytreenode.leftchild, x) and isAVL(mytreenode.rightchild, x)
        else:
            x = False
    return x


if __name__ == '__main__':
    data = input().split(' ')
    for x in range(len(data)):
        if data[x] != '#':
            data[x] = int(data[x])
    MyTree = bsTree(data, bsTreeNode())
    MyTree.create_tree(MyTree.root)
    MyTree.updatedepth(MyTree.root)

    print(isbstree(MyTree) and isAVL(MyTree.root))

