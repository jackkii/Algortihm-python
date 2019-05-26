# inorder.py
# -----------------------
# 二叉树的中序遍历
# 非递归版中序遍历（使用栈实现）
# 中序遍历: 左孩子，根节点，右孩子
# 将左孩子全部进栈，直到None,然后最后一个左孩子出栈打印，
# 再将右孩子入栈，右孩子的所有左子树入栈，循环
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


def inorder(btreeNode):
    # 递归版中序遍历
    if btreeNode:
        inorder(btreeNode.lchild)
        if btreeNode.elem is not None:
            print(btreeNode.elem)
        inorder(btreeNode.rchild)


def inorder_feidigui(btree):
    # 非递归版中序遍历（使用栈）
    # 将左孩子全部进栈，直到None,然后最后一个左孩子出栈打印，
    # 再将右孩子入栈，右孩子的所有左子树入栈，循环
    stack = []
    node = btree.root
    while len(stack) > 0 or node is not None:
        if node is not None:  # 如果node不为空，则定有左孩子(可能为None)
            stack.append(node)  # 将左孩子全部进栈
            node = node.lchild
        else:
            node = stack.pop()  # 当左孩子全进栈后，最后一个左孩子出栈
            if node.elem is not None:
                print(node.elem)  # 打印最后一个左孩子，再将对应右孩子进栈
            node = node.rchild  # 之后将右孩子的左子树路径全部进栈


if __name__ == '__main__':
    data = input().split(' ')
    MyTree = bTree(data, bTreeNode())
    MyTree.create_tree(MyTree.root)

    inorder(MyTree.root)
    print()
    inorder_feidigui(MyTree)
