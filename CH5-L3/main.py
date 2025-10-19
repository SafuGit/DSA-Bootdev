def fib(n):
  grandparent = 0
  parent = 1
  current = 0
  if n == 0:
      return 0
  if n == 1:
      return 1
  for i in range(0, n - 1):
    current = parent + grandparent
    grandparent = parent
    parent = current
  return current

print(fib(10))