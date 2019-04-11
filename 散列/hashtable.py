# hashtable.py
# ----------------------
# 哈希表的插入删除查找，使用除数留余法及链表法
#-----------------------
# Jackkii   2019/04/11
#

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class HashTable:
    def __init__(self, msize):
        self.size = msize
        self.slots = [None] * self.size         # key

    def hashfunction(self, key, msize):
        # 除留余数法
        return key % msize

    def rehash(self, my_hash, key):
        # 链表法再哈希
        newnode = Node(key)
        current = self.slots[my_hash]
        while current.next is not None:
            current = current.next
        current.next = newnode
        return newnode

    def put(self, key):
        my_hash = self.hashfunction(key, self.size)
        newnode = Node(key)

        if self.slots[my_hash] is None:
            self.slots[my_hash] = newnode
        else:
            if self.slots[my_hash].val != key:
                self.rehash(my_hash, key)

    def get(self, key):
        # 判断元素是否在散列表中
        my_hash = self.hashfunction(key, self.size)

        found = False
        stop = False
        current = self.slots[my_hash]
        while current is not None and not found and not stop:
            if current.val == key:
                found = True
            if current.next is None:
                stop = True
            current = current.next
        return found

    def delete(self, key):
        if self.get(key) is False:
            print('Delete Error')
        else:
            my_hash = self.hashfunction(key, self.size)
            current = self.slots[my_hash]
            if current.val == key:
                self.slots[my_hash] = current.next
            else:
                while current.next.val != key:
                    current = current.next
                current.next = current.next.next


size = eval(input())
myyhash = HashTable(size)
num = list(input().split())
num = [int(x) for x in num]
for i in range(len(num)):
    myyhash.put(num[i])
N = eval(input())   # 待插入元素个数
for i in range(N):
    x = int(input())
    myyhash.put(x)
D = eval(input())   # 待删除元素个数
for i in range(D):
    x = int(input())
    myyhash.delete(x)
S = eval(input())   # 待查找元素个数
for i in range(S):
    x = int(input())
    print(myyhash.get(x))
