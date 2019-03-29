#kuohao_matching.py
#------------------------------
#使用栈来实现括号匹配
#------------------------------
#Jackkii  2019/03/28
#

# 顺序栈(使用列表实现)
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
            return True
        else:
            return False

    def get_top(self):
        return self.stack[-1]

    def stack_len(self):
        return self.Len


#括号匹配字典(通过右括号匹配左括号)
dict_match = {'}': '{', ']': '[', ')': '('}


def matching(sstr):
    # 匹配函数
    
    myyystack = MyStack()                   # 创建栈对象
    for x in range(len(sstr)):              # 遍历输入的字符串
        if sstr[x] in ['{', '(', '[']:      # 遇到一个左括号
            myyystack.push(sstr[x])         # 推入栈中
        elif sstr[x] in ['}', ']', ')']:    # 遇到右括号
            if myyystack.is_empty() or myyystack.get_top() != dict_match[sstr[x]]:  # 如果此时栈为空，或栈顶元素不匹配
                return False
            else:
                myyystack.pop()             # 匹配则消去该括号
        else:
            continue                        # 遇到其他字符，则跳过
    if not myyystack.is_empty():            # 遍历字符串结束后，若栈非空，则匹配失败
        return False
    return True


sstr = input()                              # 输入字符串
print(matching(sstr))                       # 打印检查结果
