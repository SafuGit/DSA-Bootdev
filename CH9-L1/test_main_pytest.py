import pytest
from main import Node


class TestNode:
  """Test suite for the Node class"""

  def test_node_initialization_with_value(self):
    """Test creating a node with a value"""
    # Arrange & Act
    node = Node("Llewelyn Moss")
    
    # Assert
    assert node.val == "Llewelyn Moss", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Node Initialization - Value\n"
      f"{'='*70}\n"
      f"📊 Created node with: 'Llewelyn Moss'\n"
      f"✅ Expected val: 'Llewelyn Moss'\n"
      f"❌ Got val:      {node.val}\n"
      f"💡 Constructor should set self.val = val\n"
      f"{'='*70}\n"
    )

  def test_node_initialization_next_is_none(self):
    """Test that new node's next is None by default"""
    # Arrange & Act
    node = Node("Anton Chigurh")
    
    # Assert
    assert node.next is None, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Node Initialization - Next Field\n"
      f"{'='*70}\n"
      f"📊 Created new node\n"
      f"✅ Expected next: None\n"
      f"❌ Got next:      {node.next}\n"
      f"💡 Constructor should set self.next = None\n"
      f"{'='*70}\n"
    )

  def test_set_next_links_two_nodes(self):
    """Test linking two nodes together"""
    # Arrange
    first_node = Node("Llewelyn Moss")
    second_node = Node("Anton Chigurh")
    
    # Act
    first_node.set_next(second_node)
    
    # Assert
    assert first_node.next is second_node, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Set Next - Linking Nodes\n"
      f"{'='*70}\n"
      f"📊 first_node.set_next(second_node)\n"
      f"✅ Expected first_node.next: {second_node}\n"
      f"❌ Got first_node.next:      {first_node.next}\n"
      f"💡 set_next should assign self.next = node\n"
      f"{'='*70}\n"
    )

  def test_set_next_preserves_node_value(self):
    """Test that set_next doesn't affect node values"""
    # Arrange
    first_node = Node("Carson Wells")
    second_node = Node("Ed Tom Bell")
    
    # Act
    first_node.set_next(second_node)
    
    # Assert
    assert first_node.val == "Carson Wells", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Set Next - First Node Value Preserved\n"
      f"{'='*70}\n"
      f"📊 After linking nodes\n"
      f"✅ Expected first val: 'Carson Wells'\n"
      f"❌ Got first val:      {first_node.val}\n"
      f"{'='*70}\n"
    )
    assert second_node.val == "Ed Tom Bell", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Set Next - Second Node Value Preserved\n"
      f"{'='*70}\n"
      f"📊 After linking nodes\n"
      f"✅ Expected second val: 'Ed Tom Bell'\n"
      f"❌ Got second val:      {second_node.val}\n"
      f"{'='*70}\n"
    )

  def test_chain_three_nodes(self):
    """Test creating a chain of three nodes"""
    # Arrange
    node1 = Node("Llewelyn Moss")
    node2 = Node("Anton Chigurh")
    node3 = Node("Carson Wells")
    
    # Act
    node1.set_next(node2)
    node2.set_next(node3)
    
    # Assert
    assert node1.next is node2, "First node should link to second"
    assert node2.next is node3, "Second node should link to third"
    assert node3.next is None, "Third node should have no next"
    
    # Verify chain traversal
    assert node1.next.next is node3, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Chain Three Nodes - Traversal\n"
      f"{'='*70}\n"
      f"📊 Chain: node1 → node2 → node3\n"
      f"✅ Expected node1.next.next: {node3}\n"
      f"❌ Got node1.next.next:      {node1.next.next}\n"
      f"💡 Should be able to traverse the chain\n"
      f"{'='*70}\n"
    )

  def test_bootdev_scenario_build_list(self):
    """Test building linked list as in Boot.dev scenario"""
    # Arrange
    linked_list = Node("Llewelyn Moss")
    
    # Act - Add Anton Chigurh
    node2 = Node("Anton Chigurh")
    linked_list.set_next(node2)
    
    # Add Carson Wells
    node3 = Node("Carson Wells")
    node2.set_next(node3)
    
    # Add Ed Tom Bell
    node4 = Node("Ed Tom Bell")
    node3.set_next(node4)
    
    # Assert - Convert to list for verification
    result = []
    current = linked_list
    while current:
      result.append(current.val)
      current = current.next
    
    expected = ["Llewelyn Moss", "Anton Chigurh", "Carson Wells", "Ed Tom Bell"]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Boot.dev Scenario - Build List\n"
      f"{'='*70}\n"
      f"📊 Built linked list with 4 nodes\n"
      f"✅ Expected list: {expected}\n"
      f"❌ Got list:      {result}\n"
      f"{'='*70}\n"
    )

  def test_bootdev_full_scenario(self):
    """Test complete Boot.dev scenario with all 6 nodes"""
    # Arrange
    linked_list = Node("Llewelyn Moss")
    
    # Build the list step by step
    names = ["Anton Chigurh", "Carson Wells", "Ed Tom Bell", "Carla Jean Moss", "Wendell"]
    current = linked_list
    
    # Act
    for name in names:
      new_node = Node(name)
      current.set_next(new_node)
      current = new_node
    
    # Assert
    result = []
    current = linked_list
    while current:
      result.append(current.val)
      current = current.next
    
    expected = ["Llewelyn Moss", "Anton Chigurh", "Carson Wells", "Ed Tom Bell", "Carla Jean Moss", "Wendell"]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Boot.dev Full Scenario\n"
      f"{'='*70}\n"
      f"📊 Built complete linked list with 6 nodes\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_node_repr_returns_value(self):
    """Test that node's __repr__ returns the value"""
    # Arrange
    node = Node("Test Value")
    
    # Act
    result = repr(node)
    
    # Assert
    assert result == "Test Value", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Node __repr__\n"
      f"{'='*70}\n"
      f"📊 Node value: 'Test Value'\n"
      f"✅ Expected repr: 'Test Value'\n"
      f"❌ Got repr:      '{result}'\n"
      f"💡 __repr__ should return self.val\n"
      f"{'='*70}\n"
    )

  def test_multiple_set_next_calls(self):
    """Test that set_next can be called multiple times (overwrites)"""
    # Arrange
    node1 = Node("First")
    node2 = Node("Second")
    node3 = Node("Third")
    
    # Act
    node1.set_next(node2)
    node1.set_next(node3)  # Overwrite
    
    # Assert
    assert node1.next is node3, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Multiple Set Next Calls\n"
      f"{'='*70}\n"
      f"📊 Called set_next twice (should overwrite)\n"
      f"✅ Expected next: {node3} ('Third')\n"
      f"❌ Got next:      {node1.next}\n"
      f"💡 Second set_next call should overwrite first\n"
      f"{'='*70}\n"
    )

  def test_node_with_empty_string_value(self):
    """Test node can hold empty string"""
    # Arrange & Act
    node = Node("")
    
    # Assert
    assert node.val == "", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Node with Empty String\n"
      f"{'='*70}\n"
      f"📊 Created node with empty string\n"
      f"✅ Expected val: ''\n"
      f"❌ Got val:      '{node.val}'\n"
      f"{'='*70}\n"
    )
    assert node.next is None, "Next should still be None"

  def test_linked_list_traversal(self):
    """Test traversing through a linked list"""
    # Arrange
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node1.set_next(node2)
    node2.set_next(node3)
    
    # Act - Traverse the list
    values = []
    current = node1
    while current is not None:
      values.append(current.val)
      current = current.next
    
    # Assert
    assert values == ["A", "B", "C"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Linked List Traversal\n"
      f"{'='*70}\n"
      f"📊 Traversed: node1 → node2 → node3 → None\n"
      f"✅ Expected values: ['A', 'B', 'C']\n"
      f"❌ Got values:      {values}\n"
      f"{'='*70}\n"
    )

  def test_node_independence(self):
    """Test that nodes are independent objects"""
    # Arrange
    node1 = Node("Node1")
    node2 = Node("Node2")
    
    # Act
    node1.set_next(node2)
    
    # Assert
    assert node1 is not node2, "Nodes should be different objects"
    assert node1.val != node2.val, "Nodes should have different values"
    assert node2.next is None, "Second node should have no next reference"
