# Using a Stack
URL: https://www.boot.dev/lessons/77eead15-82c9-4047-b303-f93c1ac6af2d

LockedIn supports a basic scripting language. It allows technically savvy HR managers to write scripts that can automate repetitive tasks on the platform. The language makes use of **parentheses to group operations together**, and we need to be able to check if the parentheses in a script are balanced.

---

## Balanced Parentheses

Parentheses are **balanced** when each parenthesis has a corresponding parenthesis, and the pairs of parentheses are properly nested. 

### Examples of Balanced:
```
()
()()
((()))
(()(()))
```

---

## Unbalanced Parentheses

### Examples of Unbalanced:
```
(          - Missing closing parenthesis
())        - Extra closing parenthesis
(()()      - Missing closing parenthesis
(()))      - Extra closing parenthesis
)(         - Wrong order (closing before opening)
```

---

## Assignment

Complete the `is_balanced` function.

- It takes a **string** as input
- Returns `True` if the parentheses in the string are **balanced**
- Returns `False` otherwise
- Use an instance of the provided `Stack` class in `stack.py` to keep track of the parentheses

---

## Algorithm Strategy

Use a stack to track opening parentheses:

1. Iterate through each character in the string
2. When you encounter `(`:
   - Push it onto the stack
3. When you encounter `)`:
   - Pop from the stack (this matches the pair)
   - If stack is empty when trying to pop, it's unbalanced
4. After processing all characters:
   - If stack is empty: balanced ✅
   - If stack has items: unbalanced ❌ (unclosed opening parentheses)

---

## Example Walkthrough

**Input:** `"((()))"`

```
Char | Action      | Stack After
-----|-------------|-------------
(    | push        | [(]
(    | push        | [(, (]
(    | push        | [(, (, (]
)    | pop         | [(, (]
)    | pop         | [(]
)    | pop         | []

Final: Stack is empty → Balanced ✅
```

**Input:** `"(()))"`

```
Char | Action      | Stack After
-----|-------------|-------------
(    | push        | [(]
(    | push        | [(, (]
)    | pop         | [(]
)    | pop         | []
)    | pop (empty!)| Error!

Final: Tried to pop from empty stack → Unbalanced ❌
```

---

## Tips

- Use the Stack class provided in `stack.py`
- Remember: stack is LIFO (Last In, First Out)
- Opening `(` pushes, closing `)` pops
- Handle edge cases: empty strings, immediate closing parenthesis
