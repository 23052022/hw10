
import random
print("number")
n = int(input())
mylist = [random.randint(0, n) for _ in range(10)]
print(mylist)
target1 =int(input("enter x:"))
def twoSum(mylist,target):
    values = dict()
    for i, elem in enumerate(mylist):
        comp = target - elem
        if comp in values:
            return[values[comp],i]
        values[elem]=i
    return[]
nums = twoSum(mylist,target1)
print(nums)
