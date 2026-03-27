# AERT Toolkit
# Name:Sanchit
# Roll No:2501730475
# Section:A

# -------------------------
# 1. Stack ADT
# -------------------------

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


# -------------------------
# 2. Recursive Factorial
# -------------------------

def fact(i):
    if i==0 or i==1:
        return 1
        
    elif i<0:
        return "inavlid input"
    else:
        return fact(i-1)*i


# -------------------------
# 3. Naive Fibonacci
# -------------------------

fib_calls = 0

def fibonacci(n):
    global fib_calls
    fib_calls += 1

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# -------------------------
# 4. Memoized Fibonacci
# -------------------------

memo = {}
memo_calls = 0

def fibonacci_memo(n):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

    return memo[n]


# -------------------------
# 5. Tower of Hanoi
# -------------------------

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return

    tower_of_hanoi(n - 1, source, target, auxiliary)
    print("Move disk", n, "from", source, "to", target)
    tower_of_hanoi(n - 1, auxiliary, source, target)


# -------------------------
# 6. Recursive Binary Search
# -------------------------

def binary_search(arr, left, right, key):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, left, mid - 1, key)
    else:
        return binary_search(arr, mid + 1, right, key)


# -------------------------
# Main Program
# -------------------------

if __name__ == "__main__":

    # Stack Demo
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack pop:", s.pop())
    print("Stack peek:", s.peek())

    # Factorial
    print("Factorial of 5:",fact(5))

    # Fibonacci
    print("Fibonacci(6):", fibonacci(6))
    print("Naive Fibonacci calls:", fib_calls)

    # Memoized Fibonacci
    print("Memo Fibonacci(6):", fibonacci_memo(6))
    print("Memoized Fibonacci calls:", memo_calls)

    # Tower of Hanoi
    print("Tower of Hanoi for 3 disks:")
    tower_of_hanoi(3, "A", "B", "C")

    # Binary Search
    arr = [2, 4, 6, 8, 10, 12]
    result = binary_search(arr, 0, len(arr) - 1, 10)
    print("Binary Search result index:", result)