# Hash_diamond.py
# ------------------------
# 表中存宝石，石头的string用来查找
# -------------------------
# Jackkii   2019/04/12
#


class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size         # key

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
        else:
            if self.slots[hashvalue] != key:
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key

    def get(self, key):
        startslot = self.hashfunction(key)

        stop = False
        found = False
        position = startslot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True
        return found


kinds = list(input())
kinds = [ord(x) for x in kinds]
my_own = list(input())
my_own = [ord(x) for x in my_own]
my_hash = HashTable(9)
result = 0
for i in range(len(kinds)):
    my_hash.put(kinds[i])
for j in range(len(my_own)):
    if my_hash.get(my_own[j]) is True:
        result += 1
print(result)
