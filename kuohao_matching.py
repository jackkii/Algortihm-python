
class MyStack:
    def __init__(self):
        self.stack = []
        self.Len = 0

    def pop(self):
        if self.is_empty():
            raise LookupError('stack is empty')
        else:
            self.Len -= 1
            return self.stack.pop()

    def push(self, value):
        self.stack.append(value)
        self.Len += 1

    def is_empty(self):
        if self.Len == 0:
            return 1
        else:
            return 0

    def get_top(self):
        return self.stack[-1]

    def stack_len(self):
        return self.Len


#括号匹配字典
dict_match = {'}': '{', ']': '[', ')': '('}


def matching(sstr):
    #匹配函数

    myyystack = MyStack()
    for x in range(len(sstr)):
        if sstr[x] in ['{', '(', '[']:
            myyystack.push(sstr[x])
        elif sstr[x] in ['}', ']', ')']:
            if myyystack.is_empty() or myyystack.get_top() != dict_match[sstr[x]]:
                return False
            else:
                myyystack.pop()
        else:
            continue
    if not myyystack.is_empty():
        return False
    return True


sstr = input()
print(matching(sstr))
