# stack_try.py
# -----------------------
# stack_try
# 尝试将整数转换为二进制(使用堆栈结构）
# -----------------------
# Jackkii    2019/03/18
# Jackkii    2019/05/23    修改一些细节

class myStack:                #myStack类
    def __init__(self):       
        self.Len = 0          #堆栈深度
        self.stack = []       #使用列表实现堆栈

    def pop(self):
        if self.isEmpty():    #如果堆栈无元素
            raise LookupError('stack is empty')   #报错
        else:
            self.stack.pop()  #有元素则弹出，使用列表的pop
            self.Len -= 1     #深度减一

    def push(self,value):
        self.stack.append(value)  #朝栈尾添加元素
        self.Len += 1             #深度加一

    def isEmpty(self):        #判断栈是否为空
        if self.Len == 0:
            return True
        return False

    def getTop(self):         #取得栈顶元素
        return self.stack[-1]

    def stackLen(self):       #取得堆栈深度
        return self.Len

    def printt(self):         #此为整数转换为二进制输出方便所设函数
        while not self.isEmpty():   #栈不空则打印，每打印一个数，弹出一个数
            print(int(self.getTop()),end='')
            self.pop()

if __name__ == '__main__':              
    num=eval(input())             #input字符串转换成数字
    mmystack=myStack()            #创建堆栈
    while num/2 != 0:             #当商不为0时   
        mmystack.push(num%2)      #将每次除2的余数推进栈
        num =(num-num%2)/2        
    mmystack.printt()
    
   
'''
思路：
建栈：使用列表实现
      1.__init__中 创建栈长，列表
      2.push,pop,isempty函数
      3.gettop, stacklen, print函数（方便输出)
十进制转二进制：
       原理：模二余数入栈，num=num减余数再除2（num整除//2/也可),循环到商不为0后倒序输出
