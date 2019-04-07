# greatest_common_divisor.py
# ----------------------------
# 最大公约数（辗转相除法）
# ----------------------------
# Jackkii    2019/03/28
#

def div(a, b):
    # 两数a>b
    if a % b == 0:
        return b
    else:
        return div(b, a % b)


num = eval(input())
for _ in range(num):
    S = list(input().split(' '))
    a = int(S[0])
    b = int(S[1])
    print(div(a, b))
