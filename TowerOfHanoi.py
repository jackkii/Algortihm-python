#TowerOfHanoi.py
#-------------------------
#汉诺塔
#对柱子编号A,B,C，将所有圆盘从A移动到C
#步骤：先将N-1个小圆盘从A移动到B
#     将第N个底盘从A移动到C
#      将N-1个小圆盘从B移动到C
#----------------------------
#Jackkii    2019/03/24
#


def move(N, A, B, C):
    # move函数，将N个圆盘从A借助B移动到C
    
    if N == 1:
        print('将%s上的第%s个圆盘从%s移动到%s'%(A, N, A, C))
    else:
        move(N-1, A, C, B)                                                #将N-1个圆盘从A移动到B
        print('将%s上的第%s个圆盘从%s移动到%s' % (A, N, A, C))              #将第N个圆盘从A移动到C
        move(N-1, B, A, C)                                                #将N-1个圆盘从B移动到C

#测试
move(4, 'A','B','C')
