# btree_list.py
# 二叉树列表实现
# ------------------------------
# Jackkii   2019/04/23
# 

myTree = ['a',              # root
          ['b',             # left subtree
           ['d', [], []],   # left
           ['e', [], []]],  # right
          ['c',             # right subtree
           ['f', [], []],   # left
           []]              # right empty
          ]


def insert_left(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insert_right(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


insert_left(myTree[1][1], 't')  # 给d添加左子树
print(myTree)
