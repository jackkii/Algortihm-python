#7_out.py
#------------------------------------
#n人围圈报数，7的倍数退出，循环至最后一人
#------------------------------------
#jackkii    2019/03/18

peopleNumber = input()
n = int(peopleNumber)   #将input输入的字符串转换为int型
counter=0               #计数7
i=-1                    #列表下标从0开始
l=list(range(1,n+1))    #列表l储存初始编号

while n > 0:
    i += 1              #移动到下一个编号
    counter += 1        #计数加一

    if i >= n:          #如果移动到末尾
        i = 0           #则从头开始

    if counter == 7:    #如果计数到7
        counter = 0     #重置counter
        print(l[i])     #打印出元素原来的编号
        l.remove(l[i])  #移除
        i -= 1          #移动至删除元素的上一位
        n -= 1          #列表元素减一
