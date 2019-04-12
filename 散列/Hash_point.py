# Hash_point.py
# ----------------------
# 求一条过原点直线上点的数量, 给N个点的坐标
# ----------------------
# Jackkii   2019/04/12
#


class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size         # key
        self.count = [0] * self.size

    def hashfunction(self, key):
        # 除留余数法
        return key % self.size

    def rehash(self, old_hash):
        # 线性探测法
        return (old_hash+1) % self.size

    def put(self, key):
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.count[hashvalue] += 1
        else:
            if self.slots[hashvalue] != key:
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.count[nextslot] += 1
                else:
                    self.count[nextslot] += 1
            else:
                self.count[hashvalue] += 1

    def get(self, key):
        startslot = self.hashfunction(key)

        count0 = 0
        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                count0 = self.count[position]
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return count0

    def max(self):
        return max(self.count)


N = eval(input())
my_hash = HashTable(10)
for i in range(N):
    x = list(input().split(' '))
    k = int(x[1])//int(x[0])
    my_hash.put(k)
print(my_hash.max())
