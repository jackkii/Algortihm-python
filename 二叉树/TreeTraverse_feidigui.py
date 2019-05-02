# TreeTraverse_feidigui.py
# -----------------------------
# 二叉树的先中后序遍历打印，非递归形式
# -------------------------------
# Jackkii     2019/05/02
#

class Node:
    def __init__(self, elem=None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    def __init__(self, data):
        self.root = Node()
        self.data = data

    def create_tree(self, node, i=0):
        if i >= len(self.data):
            return
        else:
            if self.data[i] != '#':
                node.elem = self.data[i]
                if 2*i+1 < len(data):
                    node.lchild = Node()
                    self.create_tree(node.lchild, 2*i+1)
                if 2*i+2 < len(data):
                    node.rchild = Node()
                    self.create_tree(node.rchild, 2*i+2)


def preorder(mytree):
    stack = []
    stack.append(mytree.root)
    while len(stack) > 0:
        node = stack.pop()
        if node.elem is not None:       # 先将根节点打印
            print(node.elem)

        if node.rchild is not None:     # 若有右孩子，放进栈中
            stack.append(node.rchild)
        if node.lchild is not None:     # 若有左孩子，之后会先打印左孩子，再处理左孩子的右左孩子
            stack.append(node.lchild)   # 使得实现打印根节点，左孩子，右孩子


def inorder(mytree):
    stack = []
    node = mytree.root
    while len(stack) > 0 or node is not None:
        if node is not None:        # 如果node不为空，则定有左孩子
            stack.append(node)      # 将左孩子全部进栈
            node = node.lchild
        else:
            node = stack.pop()      # 当左孩子全进栈后，最后一个左孩子出栈
            if node.elem is not None:
                print(node.elem)        # 打印最后一个左孩子，再将对应右孩子进栈
            node = node.rchild          # 之后将右孩子的左子树路径全部进栈


def postorder(mytree):
    stack1, stack2 = [], []
    stack1.append(mytree.root)
    while len(stack1) > 0:
        node = stack1.pop()             # 先将根节点放至stack2的最底
        stack2.append(node)

        if node.lchild is not None:     # 若有左孩子，先放进stack1
            stack1.append(node.lchild)
        if node.rchild is not None:     # 若有右孩子，则之后会先将右孩子的一支放入stack2中
            stack1.append(node.rchild)  # 使得最后stack2输出为左孩子，右孩子，根节点

    while len(stack2) > 0:
        x = stack2.pop().elem
        if x is not None:
            print(x)


if __name__ == '__main__':
    K = input()
    data = []
    if len(K) != 0:
        for x in range(len(K)):
            data = list(K.split())  # 得到list数组（中间元素为string类）
    # 构建树
    MyTree = Tree(data)
    MyTree.create_tree(MyTree.root)
    # postorder(MyTree)
    inorder(MyTree)

