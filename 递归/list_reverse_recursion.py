#list_reverse_recursion.py
#---------------------------
#列表转置，使用递归实现
#---------------------------
#Jackkii   2019/03/28
#
def reverse(n, array):
   if n==0:
        return
   else:
       rearray.append(array[n-1])
       reverse(n-1,array)


n = eval(input())
rearray = []
array = list(input().split())
array = [int(x) for x in array]
reverse(n, array)

for _ in range(n):
    print(rearray[_])
