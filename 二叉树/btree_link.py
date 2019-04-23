# btree_link.py
# 二叉树的链表实现(简单）及二叉树的三种递归遍历
# -----------------------------------------
# Jackkii   2019/04/23
#


class BinaryTree:
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
        return self.leftChild

    def insert_right(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
        return self.rightChild

    def get_rightChild(self):
        return self.rightChild

    def get_leftChild(self):
        return self.leftChild

    def set_rootVal(self, obj):      # 当前结点数据
        self.key = obj

    def get_rootVal(self):           # 获取当前结点数据
        return self.key


def preorder(tree):                 # 先序遍历
    if tree:
        print(tree.get_rootVal())
        preorder(tree.get_leftChild())
        preorder(tree.get_rightChild())


def inorder(tree):                  # 中序遍历
    if tree:
        inorder(tree.get_leftChild())
        print(tree.get_rootVal())
        inorder(tree.get_rightChild())


def postorder(tree):                # 后序遍历
    if tree is not None:
        postorder(tree.get_leftChild())
        postorder(tree.get_rightChild())
        print(tree.get_rootVal())


if __name__=='__main__':
    my_Tree = BinaryTree('root')
    A = my_Tree.insert_left('A')
    B = my_Tree.insert_right('B')
    C = A.insert_left('C')
    D = A.insert_right('D')
    E = B.insert_left('E')
    F = D.insert_left('F')
    preorder(my_Tree)
