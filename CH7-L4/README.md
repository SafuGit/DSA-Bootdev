# Pop and Peek
URL: https://www.boot.dev/lessons/d148cd17-4fb1-47f3-9501-0fd9f433f54d

Now that we can add items to our stack, we need to be able to **view the top item**, and **remove the top item**.

---

## Assignment

1. **Complete the `peek` method**: It should return the top item from the stack **without modifying** the stack. If the stack is empty, return `None`.

2. **Complete the `pop` method**: It should **remove and return** the top item from the stack. If the stack is empty, return `None`.

---

## Stack Operations

### Peek
- **Purpose**: View the top item without removing it
- **Returns**: Top item (or `None` if empty)
- **Modifies stack?**: No
- **Time complexity**: O(1)

### Pop
- **Purpose**: Remove and return the top item
- **Returns**: Top item (or `None` if empty)
- **Modifies stack?**: Yes (removes item)
- **Time complexity**: O(1)

---

## Example Usage

```python
stack = Stack()
stack.push({"name": "Alice", "role": "Developer"})
stack.push({"name": "Bob", "role": "Designer"})

print(stack.peek())  # {"name": "Bob", "role": "Designer"}
print(stack.size())  # 2 (peek doesn't remove)

print(stack.pop())   # {"name": "Bob", "role": "Designer"}
print(stack.size())  # 1 (pop removes item)

print(stack.pop())   # {"name": "Alice", "role": "Developer"}
print(stack.pop())   # None (stack is empty)
```

---

## Tips

- Remember: the "top" of the stack is the **end** of the list
- Peek returns the item but leaves it in the stack
- Pop returns the item and removes it from the stack
- Both return `None` if the stack is empty
