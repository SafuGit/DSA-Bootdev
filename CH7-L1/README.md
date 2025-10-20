# Stacks
URL: https://www.boot.dev/lessons/4fb8c103-5bab-4e0a-a0df-e4a024ee20b9

A stack is a data structure that stores ordered items. It's like a list, but its design is more restrictive. It only allows items to be added or removed from the **top** of the stack.

It's called a "stack" because it behaves just like a stack of physical items. Imagine a stack of plates: it's easy to take an item off the top of the stack, but you can't really get to the items in the middle or at the bottom without removing the items on top first. 

You'll often hear a stack referred to as a **LIFO (Last In, First Out)** data structure.

---

## Assignment

In this chapter we'll build a stack from scratch! A stack will be useful at LockedIn when we need **undo/redo functionality**. For example, a user can add other users to their "connections" list, and then undo the last connection they added. Stacks are a great way to implement undo functionality.

For now, we'll just focus on two methods: `push` and `size`. Notice that the `Stack` class already has a constructor and the underlying `List` that we'll use to store items.

1. **Complete the `push` method**: It should add an item to the top of the stack. The "top" of the stack is the end of the list in our implementation.
2. **Complete the `size` method**: It should return the number of items in the stack.

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        # Add item to top of stack (end of list)
        pass

    def size(self):
        # Return number of items in stack
        pass
```

---

## Example Usage

```python
stack = Stack()
stack.push({"name": "Alice", "role": "Developer"})
stack.push({"name": "Bob", "title": "CTO"})
print(stack.size())  # prints 2
```
