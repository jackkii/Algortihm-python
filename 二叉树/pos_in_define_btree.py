# pos_in_define_btree.py
# 根据二叉树的先序遍历和中序遍历构建二叉树
# 并按后序遍历和层序遍历输出
# --------------------------------------
# Jackkii       2019/05/02
#


class Node:
    def __init__(self, elem=None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    def __init__(self, preorderlist, inorderlist):
        self.root = Node()
        self.preorderlist = preorderlist
        self.inorderlist = inorderlist

    def create_tree(self, node, inorderlist, preorderlist):
        if len(inorderlist) == 0:
            return
        elif len(inorderlist) == 1:
            node.elem = inorderlist[0]

        elif len(inorderlist) == 2:
            node.elem = preorderlist[0]
            if preorderlist[0] == inorderlist[1]:
                node.lchild = Node()
                node.lchild.elem = preorderlist[1]
            elif preorderlist[0] == inorderlist[0]:
                node.rchild = Node()
                node.rchild.elem = preorderlist[1]

        else:
            mid = inorderlist.index(preorderlist[0])
            node.elem = preorderlist[0]

            node.lchild = Node()
            self.create_tree(node.lchild, inorderlist[0:mid], preorderlist[1:mid+1])
            node.rchild = Node()
            self.create_tree(node.rchild, inorderlist[mid+1:len(inorderlist)], preorderlist[mid+1:len(preorderlist)])

def cengxu(mytree):
    queue = []
    queue.append(mytree.root)
    while len(queue) > 0:
        node = queue.pop(0)
        if node.elem is not None:
            print(node.elem, end=' ')
        if node.lchild is not None:
            queue.append(node.lchild)
        if node.rchild is not None:
            queue.append(node.rchild)


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
            print(x, end=' ')


if __name__ == '__main__':
    K1 = input()
    K2 = input()
    preorderlist, inorderlist = [], []
    if len(K1) != 0:
        for x in range(len(K1)):
             preorderlist= list(K1.split())  # 得到list数组（中间元素为string类）
    if len(K2) != 0:
        for x in range(len(K2)):
            inorderlist = list(K2.split())

    # 构建树
    MyTree = Tree(preorderlist, inorderlist)
    MyTree.create_tree(MyTree.root, inorderlist, preorderlist)

    # postorder(MyTree)
    cengxu(MyTree)
