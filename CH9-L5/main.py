from node import Node


class LinkedList:
  def add_to_tail(self, node):
    if self.head == None:
      self.head = node
      return
    last_node = None
    for iter_node in self.__iter__():
      if iter_node.next == None:
        last_node = iter_node
    last_node.next = node

  # don't touch below this line

  def __init__(self):
    self.head = None

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next

  def __repr__(self):
    nodes = []
    for node in self:
      nodes.append(node.val)
    return " -> ".join(nodes)
