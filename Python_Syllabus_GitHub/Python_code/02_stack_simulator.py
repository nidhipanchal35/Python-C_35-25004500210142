"""Practical: 3.2 Stack Simulator"""

stack = []

def push(item):
    stack.append(item)

def pop():
    if is_empty():
        print("Stack is empty.")
        return None
    return stack.pop()

def peek():
    return stack[-1] if stack else None

def is_empty():
    return len(stack) == 0

def display():
    print("Stack (bottom to top):", stack)

for item in [10, 20, 30, 40, 50]:
    push(item)
print("Top item:", peek())
print("Popped:", pop())
print("Popped:", pop())
display()
