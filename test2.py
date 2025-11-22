# =============================================
# Internship-Ready Python Practice Sheet
# Covers: Sorting, Searching, Recursion, Strings, Math
# =============================================

# ------------------------------
# 1️⃣ Bubble Sort
# ------------------------------
def bubble_sort(arr):
    """
    Sorts the list in ascending order using Bubble Sort
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# ------------------------------
# 2️⃣ Linear Search
# ------------------------------
def linear_search(arr, target):
    """
    Returns the index of target if found, else -1
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# ------------------------------
# 3️⃣ Binary Search
# ------------------------------
def binary_search(arr, target):
    """
    Binary search on sorted array. Returns index if found, else -1
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ------------------------------
# 4️⃣ Recursion
# ------------------------------

# Factorial (recursive)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Fibonacci (iterative - efficient)
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Fibonacci (recursive - classic, less efficient)
def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

# ------------------------------
# 5️⃣ Prime Check
# ------------------------------
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

# ------------------------------
# 6️⃣ String Utilities
# ------------------------------

# Reverse string
def reverse_string(s):
    return s[::-1]

# Check palindrome
def is_palindrome(s):
    return s == s[::-1]

# Naive substring search (returns index or -1)
def substring_search(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1

# ------------------------------
# 7️⃣ Example Usage
# ------------------------------
if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    numbers = list(set(numbers))  # remove duplicates
    numbers = bubble_sort(numbers)
    
    print("Sorted numbers:", numbers)
    print("Linear search index of 3:", linear_search(numbers, 3))
    print("Binary search index of 5:", binary_search(numbers, 5))
    
    print("Factorial 5:", factorial(5))
    
    print("Fibonacci first 10 numbers (iterative):")
    for i in range(10):
        print(fibonacci_iter(i), end=" ")
    print()
    
    print("Is 29 prime?", is_prime(29))
    print("Is 30 prime?", is_prime(30))
    
    s = "madam"
    print(f"Reverse of '{s}':", reverse_string(s))
    print(f"Is '{s}' palindrome?", is_palindrome(s))
    
    text = "datascience"
    pattern = "sci"
    print(f"Substring '{pattern}' found at index:", substring_search(text, pattern))
