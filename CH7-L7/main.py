from stack import Stack

def is_balanced(input_str):
  stack = Stack()
  for bracket in input_str:
    if bracket == "(":
      stack.push("(")
    if bracket == ")":
      if stack.size() == 0:
        return False
      stack.pop()
  if stack.size() == 0:
    return True
  return False