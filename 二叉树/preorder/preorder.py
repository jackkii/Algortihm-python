# preorder.py
# -----------------------
# 二叉树的递归先序遍历
# 二叉树的非递归先序遍历(使用栈实现)
# 先序遍历: 根节点，左孩子，右孩子
# 栈非空时，打印栈顶元素，将栈顶元素的右孩子和左孩子依次放入栈中
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


def preorder(btreeNode):
    # 递归版先序遍历
    if btreeNode:
        if btreeNode.elem is not None:
            print(btreeNode.elem)
        preorder(btreeNode.lchild)
        preorder(btreeNode.rchild)

def preorder_feidigui(btree):
    # 非递归版先序遍历(使用栈实现)
    # 栈非空时，打印栈顶元素，将栈顶元素的右孩子和左孩子依次放入栈中
    stack = []
    stack.append(btree.root)

    while len(stack) > 0:
        nownode = stack.pop()
        if nownode.elem is not None:
            print(nownode.elem)

        if nownode.rchild is not None:
            stack.append(nownode.rchild)
        if nownode.lchild is not None:
            stack.append(nownode.lchild)


if __name__ == '__main__':
    data = input().split(' ')
    MyTree = bTree(data, bTreeNode())
    MyTree.create_tree(MyTree.root)

    preorder(MyTree.root)
    print()
    preorder_feidigui(MyTree)
