#frog.py
#---------------------
#小青蛙跳台阶
#一次只能跳一格或两格
#----------------------
#Jackkii   2019/03/28
#

def jump(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return jump(n-1) + jump(n - 2)

n=eval(input())
print(jump(n))
