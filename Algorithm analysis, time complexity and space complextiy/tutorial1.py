import math


print(1000*math.log(1000000))


def linear_search(a,x):
    n = len(a)
    for i in range(0,n):
        if a[i]==x:
            return True
        else:
            return False
        


def printer(x):
    for i in range(x):
        print("hello")

printer(10)


# o(n)---> O(10
# )
# [1,2,3,45,5,,6,6,6]
#  .....>>>

def recurse(n):
    if(n==0):
        return
    else:
        pass # operation
    recurse(n-1)


#O(N)

for i in range(0,5): #-----> o(n)
    for j in range(0,5):
        for k in range(0,5):#-----> o(n)
            print("*"*k)
        

#O(n^2)


for i in range(0,10, i//2):
    print(i)
#o log(n)

for i in range(0,10,i**2):
    print(i)


#o log(logn)

# worst case scenario for this would be O(n)
# the best case O(1)
# averag case scenario O(n)


#### calculate the time complexity

def func():
    for i in range(10):
        print(i)

    for j in range(20):
        print(j)


# when there is a condition where we have 2 loops, the time compexity is calculated as O(i)+O(j), --- O(i+j), i==j O(2i or 2j)== O (n)



##### find the time complexity of the fucntion


def find_max(arr):
    if not arr:
        return None
    

    max_val = arr[0]

    for i in arr[1:]:
        if i>max_val:
            max_val=i

    return max_val