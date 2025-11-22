def reverse(x):
    return x[::-1]

print(reverse("HelloWorld"))

num = [2,4,55,7,2,5,8,9,38,35,89]
num = list(set(num))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1]=arr[j+1] ,arr[j]
    return arr

num = bubble_sort(num)
print(num)

def linear_search(arr,target):
    for i,value in enumerate(arr):
        if value == target:
            return i
    return -1

print(linear_search(num,38))

def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1

    return -1

print(binary_search(num,38))


# linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

curr = head
while curr :
    print(curr.data ,end=" -> ")
    curr = curr.next


print()

# hashmap
hashmap = {"a": 1, "b": 2}
hashmap["c"] = 3
print(hashmap["b"])   

print()

# recursion 
#factorial
def factorial(n):
    if n == 0 or n == 1 : #the base case 
        return 1
    return n * factorial(n-1) #recursion call

print(factorial(7))

print()

#Fibonacci
def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

for i in range(0,10):
    print(Fibonacci(i), end = " ")  