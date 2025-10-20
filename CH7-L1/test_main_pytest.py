import pytest
from main import Stack


class TestStack:
  """Test suite for the Stack class - LIFO data structure with push and size methods"""

  def test_empty_stack_size_bootdev(self):
    """Boot.dev test case: Empty stack has size 0"""
    # Arrange
    stack = Stack()
    
    # Act
    result = stack.size()
    
    # Assert
    expected = 0
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Empty Stack Size (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Operations: None (just initialized)\n"
      f"✅ Expected:   {expected}\n"
      f"❌ Got:        {result}\n"
      f"💡 Note:      New stack should have size 0\n"
      f"{'='*70}\n"
    )

  def test_push_two_items_bootdev(self):
    """Boot.dev test case: Push two items, check size"""
    # Arrange
    stack = Stack()
    item1 = {"name": "Alice", "role": "Developer"}
    item2 = {"name": "Bob", "title": "CTO"}
    
    # Act
    stack.push(item1)
    stack.push(item2)
    result = stack.size()
    
    # Assert
    expected = 2
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Push Two Items (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Operations: push(Alice), push(Bob)\n"
      f"✅ Expected:   {expected}\n"
      f"❌ Got:        {result}\n"
      f"💡 Note:      After 2 pushes, size should be 2\n"
      f"{'='*70}\n"
    )

  def test_push_three_items_bootdev(self):
    """Boot.dev test case: Push three items, check size"""
    # Arrange
    stack = Stack()
    items = [
      {"name": "Charlie", "company": "TechCorp"},
      {"name": "Diana", "skills": "Python"},
      {"name": "Ethan", "role": "Manager"}
    ]
    
    # Act
    for item in items:
      stack.push(item)
    result = stack.size()
    
    # Assert
    expected = 3
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Push Three Items (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Operations: push(Charlie), push(Diana), push(Ethan)\n"
      f"✅ Expected:   {expected}\n"
      f"❌ Got:        {result}\n"
      f"💡 Note:      After 3 pushes, size should be 3\n"
      f"{'='*70}\n"
    )

  def test_push_four_items_bootdev(self):
    """Boot.dev test case: Push four items, check size"""
    # Arrange
    stack = Stack()
    items = [
      {"name": "Frank", "experience": "5 years"},
      {"name": "Grace", "education": "MBA"},
      {"name": "Henry", "location": "New York"},
      {"name": "Ivy", "industry": "Finance"}
    ]
    
    # Act
    for item in items:
      stack.push(item)
    result = stack.size()
    
    # Assert
    expected = 4
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Push Four Items (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Operations: 4 push operations\n"
      f"✅ Expected:   {expected}\n"
      f"❌ Got:        {result}\n"
      f"💡 Note:      After 4 pushes, size should be 4\n"
      f"{'='*70}\n"
    )

  def test_push_and_size_multiple_times_bootdev(self):
    """Boot.dev test case: Push, check size, push, check size again"""
    # Arrange
    stack = Stack()
    
    # Act & Assert - First push and size check
    stack.push({"name": "Jack", "connections": 500})
    result1 = stack.size()
    assert result1 == 1, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: First Size Check (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Operations: push(Jack), size()\n"
      f"✅ Expected:   1\n"
      f"❌ Got:        {result1}\n"
      f"{'='*70}\n"
    )
    
    # Act & Assert - Second push and size check
    stack.push({"name": "Kelly", "endorsements": 50})
    result2 = stack.size()
    assert result2 == 2, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Second Size Check (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Operations: push(Jack), size(), push(Kelly), size()\n"
      f"✅ Expected:   2\n"
      f"❌ Got:        {result2}\n"
      f"💡 Note:      Size should increment with each push\n"
      f"{'='*70}\n"
    )

  def test_single_push(self):
    """Edge case: Push single item"""
    # Arrange
    stack = Stack()
    item = {"name": "Solo", "status": "Active"}
    
    # Act
    stack.push(item)
    result = stack.size()
    
    # Assert
    expected = 1
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Single Push\n"
      f"{'='*70}\n"
      f"📊 Operations: push(Solo)\n"
      f"✅ Expected:   {expected}\n"
      f"❌ Got:        {result}\n"
      f"💡 Note:      Single push should result in size 1\n"
      f"{'='*70}\n"
    )

  def test_push_different_data_types(self):
    """Common case: Push different types of data"""
    # Arrange
    stack = Stack()
    
    # Act
    stack.push("string")
    stack.push(42)
    stack.push({"key": "value"})
    stack.push([1, 2, 3])
    stack.push(None)
    result = stack.size()
    
    # Assert
    expected = 5
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Different Data Types\n"
      f"{'='*70}\n"
      f"📊 Operations: push(str), push(int), push(dict), push(list), push(None)\n"
      f"✅ Expected:   {expected}\n"
      f"❌ Got:        {result}\n"
      f"💡 Note:      Stack should handle any data type\n"
      f"{'='*70}\n"
    )

  def test_push_many_items(self):
    """Stress test: Push many items"""
    # Arrange
    stack = Stack()
    num_items = 100
    
    # Act
    for i in range(num_items):
      stack.push({"id": i, "data": f"item_{i}"})
    result = stack.size()
    
    # Assert
    expected = num_items
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Push Many Items\n"
      f"{'='*70}\n"
      f"📊 Operations: {num_items} push operations\n"
      f"✅ Expected:   {expected}\n"
      f"❌ Got:        {result}\n"
      f"💡 Note:      Stack should handle large numbers of items\n"
      f"{'='*70}\n"
    )

  def test_push_duplicate_items(self):
    """Common case: Push same item multiple times"""
    # Arrange
    stack = Stack()
    item = {"name": "Duplicate", "value": 42}
    
    # Act
    stack.push(item)
    stack.push(item)
    stack.push(item)
    result = stack.size()
    
    # Assert
    expected = 3
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Push Duplicate Items\n"
      f"{'='*70}\n"
      f"📊 Operations: push(item) x3 (same item)\n"
      f"✅ Expected:   {expected}\n"
      f"❌ Got:        {result}\n"
      f"💡 Note:      Stack should allow duplicate items\n"
      f"{'='*70}\n"
    )

  def test_items_list_exists(self):
    """Validation: Stack should have items attribute"""
    # Arrange
    stack = Stack()
    
    # Assert
    assert hasattr(stack, 'items'), (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Items Attribute Missing\n"
      f"{'='*70}\n"
      f"💡 Note:      Stack must have 'items' attribute to store data\n"
      f"{'='*70}\n"
    )
    
    assert isinstance(stack.items, list), (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Items Attribute Type\n"
      f"{'='*70}\n"
      f"✅ Expected:   list type\n"
      f"❌ Got:        {type(stack.items).__name__}\n"
      f"💡 Note:      'items' should be a list\n"
      f"{'='*70}\n"
    )

  def test_size_returns_integer(self):
    """Validation: Size method returns integer"""
    # Arrange
    stack = Stack()
    stack.push("item")
    
    # Act
    result = stack.size()
    
    # Assert
    assert isinstance(result, int), (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Size Return Type\n"
      f"{'='*70}\n"
      f"✅ Expected:   int type\n"
      f"❌ Got:        {type(result).__name__}\n"
      f"💡 Note:      size() must return an integer\n"
      f"{'='*70}\n"
    )

  def test_push_maintains_order(self):
    """Validation: Items are pushed to end of list (top of stack)"""
    # Arrange
    stack = Stack()
    
    # Act
    stack.push("first")
    stack.push("second")
    stack.push("third")
    
    # Assert
    assert len(stack.items) == 3, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Items List Length\n"
      f"{'='*70}\n"
      f"✅ Expected:   3 items\n"
      f"❌ Got:        {len(stack.items)} items\n"
      f"{'='*70}\n"
    )
    
    # Verify items are in correct order (LIFO)
    assert stack.items[0] == "first", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: First Item Position\n"
      f"{'='*70}\n"
      f"✅ Expected:   'first' at index 0\n"
      f"❌ Got:        '{stack.items[0]}' at index 0\n"
      f"💡 Note:      Items should be added to end of list\n"
      f"{'='*70}\n"
    )
    
    assert stack.items[-1] == "third", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Last Item Position (Top of Stack)\n"
      f"{'='*70}\n"
      f"✅ Expected:   'third' at end (top of stack)\n"
      f"❌ Got:        '{stack.items[-1]}' at end\n"
      f"💡 Note:      Most recent push should be at top (end of list)\n"
      f"{'='*70}\n"
    )

  def test_realistic_undo_functionality(self):
    """Real-world scenario: LockedIn connection undo feature"""
    # Arrange
    stack = Stack()
    connections = [
      {"name": "Alice Johnson", "role": "Software Engineer"},
      {"name": "Bob Smith", "role": "Product Manager"},
      {"name": "Carol White", "role": "Designer"},
      {"name": "Dave Brown", "role": "Data Scientist"}
    ]
    
    # Act - User adds connections
    for connection in connections:
      stack.push(connection)
    
    result = stack.size()
    
    # Assert
    expected = 4
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Realistic Undo Functionality\n"
      f"{'='*70}\n"
      f"📊 Scenario:   User adds 4 connections\n"
      f"✅ Expected:   {expected} connections in stack\n"
      f"❌ Got:        {result} connections\n"
      f"💡 Use Case:   Stack stores connection history for undo feature\n"
      f"               Most recent connection (Dave) is at top of stack\n"
      f"{'='*70}\n"
    )
    
    # Verify most recent is at top
    assert stack.items[-1]["name"] == "Dave Brown", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Most Recent Connection At Top\n"
      f"{'='*70}\n"
      f"✅ Expected:   'Dave Brown' at top of stack\n"
      f"❌ Got:        '{stack.items[-1]['name']}' at top\n"
      f"💡 Note:      LIFO: Last connection added should be first to undo\n"
      f"{'='*70}\n"
    )

  def test_multiple_stacks_independence(self):
    """Validation: Multiple stack instances are independent"""
    # Arrange
    stack1 = Stack()
    stack2 = Stack()
    
    # Act
    stack1.push("item1")
    stack1.push("item2")
    stack2.push("different")
    
    # Assert
    assert stack1.size() == 2, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Stack 1 Independence\n"
      f"{'='*70}\n"
      f"✅ Expected:   2\n"
      f"❌ Got:        {stack1.size()}\n"
      f"💡 Note:      Each stack instance should be independent\n"
      f"{'='*70}\n"
    )
    
    assert stack2.size() == 1, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Stack 2 Independence\n"
      f"{'='*70}\n"
      f"✅ Expected:   1\n"
      f"❌ Got:        {stack2.size()}\n"
      f"💡 Note:      Each stack instance should be independent\n"
      f"{'='*70}\n"
    )
