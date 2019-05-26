# postorder.py
# -----------------------
# 二叉树的后序遍历
# 非递归版后序遍历（使用两个栈实现）
# 后序遍历: 左孩子，右孩子，根节点
# 栈1弹出节点放栈2，再将节点的左孩子，右孩子分别放入栈1中
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


def postorder(btreeNode):
    # 递归版后序遍历
    if btreeNode:
        postorder(btreeNode.lchild)
        postorder(btreeNode.rchild)
        if btreeNode.elem is not None:
            print(btreeNode.elem)

def postorder_feidigui(btree):
    # 非递归版后序遍历（使用两个栈实现）
    # 须有个栈专门实现打印顺序 stack2
    # 栈1弹出节点放栈2，再将节点的左孩子，右孩子分别放入栈1中，
    # 下次则会弹出右孩子放栈2，将右孩子的左右孩子放入栈1，即将右孩子支路都先压入栈2中

    stack1, stack2 = [], []
    stack1.append(btree.root)
    while len(stack1) > 0:
        node = stack1.pop()  # 先将根节点放至stack2的最底
        stack2.append(node)

        if node.lchild is not None:  # 若有左孩子，先放进stack1
            stack1.append(node.lchild)
        if node.rchild is not None:  # 若有右孩子，则之后会先将右孩子的一支放入stack2中
            stack1.append(node.rchild)  # 使得最后stack2输出为左孩子，右孩子，根节点

    while len(stack2) > 0:  # 打印输出
        x = stack2.pop().elem
        if x is not None:
            print(x)


if __name__ == '__main__':
    data = input().split(' ')
    MyTree = bTree(data, bTreeNode())
    MyTree.create_tree(MyTree.root)

    postorder(MyTree.root)
    print()
    postorder_feidigui(MyTree)
