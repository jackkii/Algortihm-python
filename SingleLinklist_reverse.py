# SingleLinklist_reverse.py
# -----------------------------
# 使用递归完成链表转置
# -----------------------------
# Jackkii  2019/03/28
#

# 定义链表结点
class ListNode(object):

    def __init__(self, value, next =None):
        self.val = value
        self.next = next
        
    def getNext(self):
        return self.next

    def getValue(self):
        return self.val

# 定义链表操作
class SingleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    # 返回头指针
    def get_head(self):
        return self._head

    # 是否为空
    def isempty(self):
        return self._head is None

    # 当前结点插入操作
    def add(self, val):
        node = ListNode(val)
        node.next = self._head
        self._head = node
        self._size += 1

    # 表尾插入操作
    def append(self, val):
        node = ListNode(val)
        if self.isempty():                  # 若空链表，则在头部创建结点
            self._head = node
        else:
            temp = self._head               # 临时指针用于寻找尾部结点
            while temp.getNext() is not None:
                temp = temp.getNext()       # 遍历链表
            temp.next = node                # 指向尾部结点
        self._size += 1

    # 检索元素是否在链表中
    def search(self, val):
        temp = self._head
        iffound = False
        while temp is not None and not iffound:
            if temp.getValue() == val:
                iffound = True
            else:
                temp = temp.getNext()
        return iffound

    # 寻找元素对应下标index
    def index(self, val):
        temp = self._head
        count = 0
        isfound = False
        while temp is not None and not isfound:
            count += 1
            if temp.getValue() == val:
                isfound = True
            else:
                temp = temp.getNext()
        if isfound:
            return count
        else:
            raise Exception('%s is not in linkedlist' %val )

    # 删除链表中某项元素
    def remove(self, val):
        temp = self._head
        pre = None
        while temp is not None:
            if temp.getValue() == val:
                if not pre:
                    self._head = temp.getNext()
                else:
                    pre.next = temp.getNext()
                break
            else:
                pre = temp
                temp =temp.getNext()
        self._size -= 1
        
        # ??待解决问题，若删除失败如何

    # 链表中间插入元素
    def insert(self, pos, val):
        if pos <= 1:
            self.add(val)
        elif pos > self._size:
            self.append(val)
        else:
            newnode = ListNode(val)
            count = 1
            temp = self._head
            pre = None
            while count < pos:
                count += 1
                pre = temp
                temp = temp.getNext()
            pre.next = newnode
            newnode.next = temp
            self._size += 1

    # 得到尾指针
    def get_tail(self):             
        temp = self._head           
        while temp.getNext() is not None:  
            temp = temp.getNext()
        return temp

    # 打印链表元素
    def printlist(self):
        temp = self._head
        while temp is not None:
            print(temp.getValue())
            temp = temp.getNext()


# 链表转置递归函数
def list_reverse(pointer):
    if pointer is None or pointer.getNext() is None:        # 如果链表为空，或者只有一个元素，则返回当前指针
        return pointer
    else:
        temp = list_reverse(pointer.getNext())              # 取得下一结点指针
        temp.next = pointer                                 # 令下一结点指向当前结点
        pointer.next = None                                 # 当前结点指向None
        return pointer                                      # 返回当前结点


n = eval(input())                   # 输入接下来输入数据的个数
S = list(input().split(' '))        # 将一串数据分开存入一个列表中
myylist = SingleLinkedList()        # 创建一个链表
for _ in range(n):                  # 将列表中的数据存入链表中
    myylist.append(S[_])
new_head = myylist.get_tail()       # 由于要转置链表，故遍历得到当前指向尾部结点的指针，存为新头指针
list_reverse(myylist.get_head())    # 转置链表
myylist._head = new_head            # 更改新头指针
myylist.printlist()                 # 打印
