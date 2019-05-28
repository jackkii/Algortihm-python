# calculate_bstree.py
# -------------------
# 求满足指定大小的二叉搜索树的范围和
# --------------------------
# Jackkii   2019/05/28
#


class bsTreeNode:
    def __init__(self, key, lchild=None, rchild=None,parent=None):
        self.key = key
        # self.payload = val
        self.leftchild = lchild
        self.rightchild = rchild
        self.parent = parent

    def get_leftchild(self):
        return self.leftchild

    def get_rightchild(self):
        return self.rightchild

    def get_key(self):
        return self.key

    def isleaf(self):
        return not self.leftchild and not self.rightchild

    def isleftchild(self):
        return self.parent and self.parent.leftchild == self

    def isrightchild(self):
        return self.parent and self.parent.rightchild == self

    def hasbothchildren(self):
        return self.leftchild and self.rightchild

    def replaceNodeData(self, key, lc, rc):
        self.key = key
        # self.payload = value
        self.leftchild = lc
        self.rightchild = rc
        if self.get_leftchild():
            self.leftchild.parent = self
        if self.get_rightchild():
            self.rightchild.parent = self


class bsTree:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key):        # 插入实现
        if self.root:
            self._put(key, self.root)
        else:
            self.root = bsTreeNode(key)
        self.size = self.size + 1

    def _put(self, key, currentNode):
        if key < currentNode.key:
            if currentNode.get_leftchild():
                self._put(key, currentNode.leftchild)
            else:
                currentNode.leftchild = bsTreeNode(key, parent=currentNode)
        else:
            if currentNode.get_rightchild():
                self._put(key, currentNode.rightchild)
            else:
                currentNode.rightchild = bsTreeNode(key, parent=currentNode)

    def get(self, key):         # 取得key对应节点的payload值
        if self.root:
            res = self._get(key, self.root) # 取得key对应节点
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):   # 返回key对应节点
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftchild)
        else:
            return self._get(key, currentNode.rightchild)

    def delete(self, key):      # 删除
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)    # 先查找得到节点
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError

    def findmin(self, currentNode):
        if currentNode.leftchild:
            return self.findmin(currentNode.leftchild)
        else:
            return currentNode

    def remove(self, currentNode):
        if currentNode.isleaf():    # 删除叶子节点
            if currentNode == currentNode.parent.leftchild:
                currentNode.parent.leftchild = None
            else:
                currentNode.parent.rightchild = None

        elif currentNode.hasbothchildren():     # 待删除节点有两个孩子
            succ = self.findmin(currentNode.rightchild)
            currentNode.key = succ.key
            self.remove(succ)

        else:       # 待删除节点有一个孩子
            if currentNode.get_leftchild():     # 待删除节点有左孩子
                if currentNode.isleftchild():     # 如果自己是左孩子
                    currentNode.leftchild.parent = currentNode.parent
                    currentNode.parent.leftchild = currentNode.leftchild
                elif currentNode.isrightchild():    # 如果自己是右孩子
                    currentNode.leftchild.parent = currentNode.parent
                    currentNode.parent.rightchild = currentNode.rightchild
                else:                               # 如果自己是根节点,左孩子成为根节点
                    currentNode.replaceNodeData(currentNode.leftchild.key,
                                                currentNode.leftchild.leftchild,
                                                currentNode.leftchild.rightchild)
            else:   # 带删除节点有右孩子
                if currentNode.isleftchild():      # 如果自己是左孩子
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.leftchild = currentNode.rightchild
                elif currentNode.isrightchild():    # 如果自己是右孩子
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.rightchild = currentNode.rightchild
                else:                               # 如果自己是根节点
                    currentNode.replaceNodeData(currentNode.rightchild.key,
                                                currentNode.rightchild.leftchild,
                                                currentNode.rightchild.rightchild)

def preorder(bstreeNode):
    if bstreeNode:
        print(bstreeNode.key, end=' ')
        preorder(bstreeNode.leftchild)
        preorder(bstreeNode.rightchild)


def postorder(bstreeNode):
    if bstreeNode:
        postorder(bstreeNode.leftchild)
        postorder(bstreeNode.rightchild)
        print(bstreeNode.key, end=' ')


def calculate(bstreeNode, result, L, R):
    if bstreeNode:
        if L <= bstreeNode.key <= R :
            result1 = result + bstreeNode.key
        else:
            result1 = result
        return result1 + calculate(bstreeNode.leftchild, result, L, R) + calculate(bstreeNode.rightchild, result, L, R)
    else:
        return 0


if __name__ == '__main__':
    data = input().split()
    data = [int(data[i]) for i in range(len(data))]
    mybstree = bsTree()
    for i in range(len(data)):
        mybstree.put(data[i])
    n = input().split()
    L = int(n[0])
    R = int(n[1])
    print(calculate(mybstree.root, 0, L, R))




