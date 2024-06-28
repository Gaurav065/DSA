import math


print(1000*math.log(1000000))


def linear_search(a,x):
    n = len(a)
    for i in range(0,n):
        if a[i]==x:
            return True
        else:
            return False
        


# [1,2,3,45,5,,6,6,6]
#  .....>>>


# worst case scenario for this would be O(n)
# the best case O(1)
# averag case scenario O(n)


