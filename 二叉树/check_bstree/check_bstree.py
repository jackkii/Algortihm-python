# check_bstree.py
# ------------------
# 验证二叉搜索树
# 层次建树。使用中序遍历输出，与排序后比对，若相同则为二叉搜索树
# -------------------------
# Jackkii      2019/05/26
#

class bsTreeNode:
    def __init__(self, key=None, lchild=None, rchild=None, parent=None):
        self.key = key
        self.leftchild = lchild
        self.rightchild = rchild
        self.parent = parent


class bsTree:
    def __init__(self, data, root=None):
        self.root = root
        self.data = data

    def create_tree(self, node, i=0):   # 层序建树
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
                if 2*i+2 <len(self.data):
                    node.rightchild = bsTreeNode()
                    self.create_tree(node.rightchild, 2*i+2)


def inorder(bsTreeNode, stack=[]):      # 得到中序遍历的节点顺序，递归法
    if bsTreeNode:
        inorder(bsTreeNode.leftchild, stack)
        if bsTreeNode.key is not None:
            stack.append(bsTreeNode.key)
        inorder(bsTreeNode.rightchild, stack)


if __name__ == '__main__':
    data = input().split(' ')
    for x in range(len(data)):
        if data[x] != '#':
            data[x] = int(data[x])       # 考虑到会有字母输入，排序不方便

    MyTree = bsTree(data, bsTreeNode())  # 建树
    MyTree.create_tree(MyTree.root)

    stack = []
    inorder(MyTree.root, stack)       # 若为二叉搜索树，则中序遍历输出应为从小到大顺序排列
    stack_order = stack.copy()
    stack_order.sort()
    if stack == stack_order:
        print('True')
    else:
        print('False')
