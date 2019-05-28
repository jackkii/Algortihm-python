# huffman_coding1.py
# ------------------------
# 哈夫曼编码（使用list实现)
# ------------------------
# Jackkii   2019/05/28
#

class HuffmanTreeNode:
    def __init__(self, key, val='#', lchild=None, rchild=None, parent=None):
        self.key = key
        self.val = val
        self.leftchild = lchild
        self.rightchild = rchild
        self.parent = parent

    def isleaf(self):
        return not self.leftchild and not self.rightchild


class HuffmanTree:
    def __init__(self):
        self.root = None

    def create_Huffman(self, nodelist):                         # 将结点构建为树
        while len(nodelist) > 1:                                # 若结点数目大于1，则从左向右找两个权值最小的结点
            node1_index, node1 = self.findmin(nodelist)
            nodelist.pop(node1_index)
            node2_index, node2 = self.findmin(nodelist)
            nodelist.pop(node2_index)
            # 创建新结点，权值为左右节点之和，左孩子为权值较小的
            newnode = HuffmanTreeNode(node1.key + node2.key, lchild=node1, rchild=node2)
            node1.parent = newnode
            node2.parent = newnode

            nodelist.append(newnode)                            # 将新结点放入list尾部

        if len(nodelist) == 1:                                  # 当表中仅剩一个结点时,即为根节点，赋给root
            self.root = nodelist[0]

    def findmin(self, nodelist):                                # 找到列表中结点权值最小的（从左向右找）
        x = nodelist[0]
        x_index = 0
        for ii in range(len(nodelist)):
            if x.key > nodelist[ii].key:
                x = nodelist[ii]
                x_index = ii
        return x_index, x


def valconvertcode(hTreenode, x, mycodedict):                   # 创建Huffman编码字典(用list实现)
    if hTreenode:                                               # 哈夫曼编码，结点若有左孩子，结点到左孩子的路径标0，若有右孩子
        if hTreenode.isleaf():                                  # 结点到右孩子的路径标1，每个叶子结点内权值对应字母的编码即为
            mycodedict.append(hTreenode.val)                    # 根节点到该叶子结点路径上0或1的累积，并存进表中
            mycodedict.append(x)
        else:
            valconvertcode(hTreenode.leftchild, x+'0', mycodedict)
            valconvertcode(hTreenode.rightchild, x+'1', mycodedict)


def dataconvertcode(data, mycodedict):                          # 根据编码表,将输入的str字符串，转为哈夫曼编码
    for x in range(len(data)):
        y_index = mycodedict.index(data[x])
        print(mycodedict[y_index+1], end='')


if __name__ == '__main__':
    n = eval(input())                                           # 本例中并未使用
    str = list(input())                                         # 将输入的字符串转换为单个字符的列表
    mydict = []
    nodelist = []
    for x in range(len(str)):
        if str[x] not in mydict:
            mydict.append(str[x])                               # 将str[x]中元素不重复的添加到mydict
            mydict.append(str.count(str[x]))                    # 统计该元素出现次数，即为权值

    x = 0
    while x < len(mydict):                                      # 将mydict中元素转换为node(key,val),key为权值，val为字符
        nodelist.append(HuffmanTreeNode(mydict[x+1], mydict[x]))
        x = x+2

    myhuffman = HuffmanTree()                                   # 构建树
    myhuffman.create_Huffman(nodelist)

    mycodedict = []                                             # 构建huffman编码表
    valconvertcode(myhuffman.root,'', mycodedict)
    dataconvertcode(str, mycodedict)
