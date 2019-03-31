# SingleLinkedList.py
# ---------------------------
# 单向链表
# --------------------------
# Jackkii    2019/03/24
#


class ListNode(object):
    # 定义链表结点
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def get_next(self):
        return self.next

    def get_value(self):
        return self.val


class SingleLinkedList:
    # 定义链表操作
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        # 是否为空
        return self._head is None

    def add(self, val):
        # 当前结点插入操作
        node = ListNode(val)
        node.next = self._head
        self._head = node
        self._size += 1

    def append(self, val):
        # 表尾插入操作
        node = ListNode(val)
        if self.is_empty():                  # 若空链表，则在头部创建结点
            self._head = node
        else:
            temp = self._head               # 临时指针用于寻找尾部结点
            while temp.getNext() is not None:
                temp = temp.getNext()       # 遍历链表
            temp.next = node                  # 指向尾部结点
        self._size += 1

    def search(self, val):
        # 检索元素是否在链表中
        temp = self._head
        if_found = False
        while temp is not None and not if_found:
            if temp.getValue() == val:
                if_found = True
            else:
                temp = temp.getNext()
        return if_found

    def index(self, val):
        # 寻找元素对应下标index
        temp = self._head
        count = 0
        is_found = False
        while temp is not None and not is_found:
            count += 1
            if temp.getValue() == val:
                is_found = True
            else:
                temp = temp.getNext()
        if is_found:
            return count
        else:
            raise Exception('%s is not in linkedlist' % val)

    def remove(self, val):
        # 删除链表中某项元素
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
                temp = temp.getNext()
        self._size -= 1

    def insert(self, pos, val):
        # 链表中间插入元素
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

    def printlist(self):
        # 打印链表元素
        temp = self._head
        while temp is not None:
            print(temp.getValue(), end=' ')
            temp = temp.getNext()


# try
mylist = SingleLinkedList()
mylist.insert(1, 3)
mylist.printlist()
mylist.append(101)
