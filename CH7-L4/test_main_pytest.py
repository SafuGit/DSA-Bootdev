import pytest
from main import Stack


class TestStackPopAndPeek:
  """Test suite for Stack peek() and pop() methods - LIFO retrieval operations"""

  def test_peek_empty_stack(self):
    """Edge case: Peek on empty stack returns None"""
    # Arrange
    stack = Stack()
    
    # Act
    result = stack.peek()
    
    # Assert
    expected = None
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Peek Empty Stack\n"
      f"{'='*70}\n"
      f"📊 Stack:    [] (empty)\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Peek on empty stack should return None\n"
      f"{'='*70}\n"
    )

  def test_pop_empty_stack(self):
    """Edge case: Pop on empty stack returns None"""
    # Arrange
    stack = Stack()
    
    # Act
    result = stack.pop()
    
    # Assert
    expected = None
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Pop Empty Stack\n"
      f"{'='*70}\n"
      f"📊 Stack:    [] (empty)\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Pop on empty stack should return None\n"
      f"{'='*70}\n"
    )

  def test_peek_does_not_modify_stack(self):
    """Validation: Peek should not remove item from stack"""
    # Arrange
    stack = Stack()
    item1 = {"name": "Alice", "role": "Developer"}
    item2 = {"name": "Bob", "role": "Designer"}
    stack.push(item1)
    stack.push(item2)
    
    # Act
    result = stack.peek()
    size_after_peek = stack.size()
    
    # Assert
    assert result == item2, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Peek Returns Top Item\n"
      f"{'='*70}\n"
      f"📊 Stack:    [Alice, Bob] (top: Bob)\n"
      f"✅ Expected: {item2}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )
    
    assert size_after_peek == 2, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Peek Does Not Modify Stack\n"
      f"{'='*70}\n"
      f"📊 Operation: peek()\n"
      f"✅ Expected:  Size remains 2 (no removal)\n"
      f"❌ Got:       Size is {size_after_peek}\n"
      f"💡 Note:     Peek should only VIEW, not REMOVE\n"
      f"{'='*70}\n"
    )

  def test_pop_removes_and_returns_item(self):
    """Validation: Pop should remove and return top item"""
    # Arrange
    stack = Stack()
    item1 = {"name": "Alice", "role": "Developer"}
    item2 = {"name": "Bob", "role": "Designer"}
    stack.push(item1)
    stack.push(item2)
    
    # Act
    result = stack.pop()
    size_after_pop = stack.size()
    
    # Assert
    assert result == item2, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Pop Returns Top Item\n"
      f"{'='*70}\n"
      f"📊 Stack:    [Alice, Bob] (top: Bob)\n"
      f"✅ Expected: {item2}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )
    
    assert size_after_pop == 1, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Pop Removes Item From Stack\n"
      f"{'='*70}\n"
      f"📊 Operation: pop()\n"
      f"✅ Expected:  Size becomes 1 (item removed)\n"
      f"❌ Got:       Size is {size_after_pop}\n"
      f"💡 Note:     Pop should REMOVE the item\n"
      f"{'='*70}\n"
    )

  def test_bootdev_case_1(self):
    """Boot.dev test case 1: Push, peek, pop sequence"""
    # Arrange
    stack = Stack()
    alice = {"name": "Alice", "role": "Developer"}
    bob = {"name": "Bob", "role": "Designer"}
    
    # Act & Assert
    stack.push(alice)
    stack.push(bob)
    
    assert stack.size() == 2, "Size should be 2 after two pushes"
    
    peek_result = stack.peek()
    assert peek_result == bob, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Boot.dev Case 1 - Peek\n"
      f"{'='*70}\n"
      f"📊 Stack:    [Alice, Bob]\n"
      f"✅ Expected: {bob}\n"
      f"❌ Got:      {peek_result}\n"
      f"{'='*70}\n"
    )
    
    pop_result = stack.pop()
    assert pop_result == bob, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Boot.dev Case 1 - Pop\n"
      f"{'='*70}\n"
      f"📊 Stack:    [Alice, Bob]\n"
      f"✅ Expected: {bob}\n"
      f"❌ Got:      {pop_result}\n"
      f"{'='*70}\n"
    )
    
    assert stack.size() == 1, "Size should be 1 after one pop"

  def test_bootdev_case_2(self):
    """Boot.dev test case 2: Pop until empty"""
    # Arrange
    stack = Stack()
    charlie = {"name": "Charlie", "company": "TechCorp"}
    david = {"name": "David", "skills": ["Python", "JavaScript"]}
    
    # Act & Assert
    stack.push(charlie)
    stack.push(david)
    
    pop1 = stack.pop()
    assert pop1 == david, f"First pop should return David, got {pop1}"
    
    pop2 = stack.pop()
    assert pop2 == charlie, f"Second pop should return Charlie, got {pop2}"
    
    pop3 = stack.pop()
    assert pop3 is None, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Boot.dev Case 2 - Pop Empty\n"
      f"{'='*70}\n"
      f"📊 Stack:    [] (empty after 2 pops)\n"
      f"✅ Expected: None\n"
      f"❌ Got:      {pop3}\n"
      f"💡 Note:    Pop on empty stack returns None\n"
      f"{'='*70}\n"
    )

  def test_bootdev_case_3(self):
    """Boot.dev test case 3: Peek, push, pop sequence"""
    # Arrange
    stack = Stack()
    eve = {"name": "Eve", "role": "Manager", "years": 5}
    frank = {"name": "Frank", "role": "DevOps"}
    
    # Act & Assert
    stack.push(eve)
    
    peek1 = stack.peek()
    assert peek1 == eve, f"Peek should return Eve, got {peek1}"
    
    stack.push(frank)
    assert stack.size() == 2, "Size should be 2"
    
    pop1 = stack.pop()
    assert pop1 == frank, f"Pop should return Frank, got {pop1}"
    
    pop2 = stack.pop()
    assert pop2 == eve, f"Pop should return Eve, got {pop2}"
    
    pop3 = stack.pop()
    assert pop3 is None, "Pop on empty stack should return None"

  def test_lifo_order(self):
    """Validation: Verify LIFO (Last In, First Out) order"""
    # Arrange
    stack = Stack()
    items = ["first", "second", "third", "fourth"]
    
    # Act - Push all items
    for item in items:
      stack.push(item)
    
    # Assert - Pop should return in reverse order
    assert stack.pop() == "fourth", "LIFO: Last in (fourth) should be first out"
    assert stack.pop() == "third", "LIFO: Third should come next"
    assert stack.pop() == "second", "LIFO: Second should come next"
    assert stack.pop() == "first", "LIFO: First in should be last out"
    assert stack.pop() is None, "LIFO: Empty stack returns None"

  def test_multiple_peeks_same_result(self):
    """Validation: Multiple peeks return same item (no modification)"""
    # Arrange
    stack = Stack()
    item = {"name": "Test", "value": 42}
    stack.push(item)
    
    # Act
    peek1 = stack.peek()
    peek2 = stack.peek()
    peek3 = stack.peek()
    
    # Assert
    assert peek1 == item, "First peek should return item"
    assert peek2 == item, "Second peek should return same item"
    assert peek3 == item, "Third peek should return same item"
    assert stack.size() == 1, "Stack size should remain 1 after multiple peeks"

  def test_peek_after_pop(self):
    """Common case: Peek returns new top after pop"""
    # Arrange
    stack = Stack()
    stack.push("bottom")
    stack.push("middle")
    stack.push("top")
    
    # Act
    stack.pop()  # Remove "top"
    result = stack.peek()
    
    # Assert
    expected = "middle"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Peek After Pop\n"
      f"{'='*70}\n"
      f"📊 Stack:    [bottom, middle, top] → pop() → [bottom, middle]\n"
      f"✅ Expected: {expected} (new top)\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    After pop, peek should return the new top\n"
      f"{'='*70}\n"
    )

  def test_pop_single_item(self):
    """Edge case: Pop the only item in stack"""
    # Arrange
    stack = Stack()
    only_item = {"name": "Only", "data": "single"}
    stack.push(only_item)
    
    # Act
    result = stack.pop()
    size = stack.size()
    
    # Assert
    assert result == only_item, f"Pop should return the only item"
    assert size == 0, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Pop Single Item - Stack Should Be Empty\n"
      f"{'='*70}\n"
      f"✅ Expected: Size 0 (empty)\n"
      f"❌ Got:      Size {size}\n"
      f"💡 Note:    After popping only item, stack should be empty\n"
      f"{'='*70}\n"
    )

  def test_peek_single_item(self):
    """Edge case: Peek at the only item in stack"""
    # Arrange
    stack = Stack()
    only_item = {"name": "Only", "data": "single"}
    stack.push(only_item)
    
    # Act
    result = stack.peek()
    size = stack.size()
    
    # Assert
    assert result == only_item, f"Peek should return the only item"
    assert size == 1, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Peek Single Item - Stack Should Remain\n"
      f"{'='*70}\n"
      f"✅ Expected: Size 1 (unchanged)\n"
      f"❌ Got:      Size {size}\n"
      f"💡 Note:    Peek should not remove the item\n"
      f"{'='*70}\n"
    )

  def test_alternating_peek_pop(self):
    """Common case: Alternating peek and pop operations"""
    # Arrange
    stack = Stack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    
    # Act & Assert
    assert stack.peek() == "C", "Peek should show C"
    assert stack.pop() == "C", "Pop should remove C"
    assert stack.peek() == "B", "Peek should now show B"
    assert stack.pop() == "B", "Pop should remove B"
    assert stack.peek() == "A", "Peek should now show A"
    assert stack.pop() == "A", "Pop should remove A"
    assert stack.peek() is None, "Peek on empty should return None"
    assert stack.pop() is None, "Pop on empty should return None"

  def test_pop_return_value_not_affected_by_further_pops(self):
    """Validation: Popped value is independent of stack state"""
    # Arrange
    stack = Stack()
    stack.push({"id": 1})
    stack.push({"id": 2})
    stack.push({"id": 3})
    
    # Act
    popped = stack.pop()
    original_id = popped["id"]
    
    # More pops
    stack.pop()
    stack.pop()
    
    # Assert
    assert original_id == 3, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Popped Value Independence\n"
      f"{'='*70}\n"
      f"✅ Expected: Popped value remains unchanged (id=3)\n"
      f"❌ Got:      id={original_id}\n"
      f"💡 Note:    Pop should return value that doesn't change with stack\n"
      f"{'='*70}\n"
    )

  def test_realistic_undo_feature(self):
    """Real-world scenario: LockedIn connection undo with peek preview"""
    # Arrange
    stack = Stack()
    connections = [
      {"name": "Alice Johnson", "role": "Engineer"},
      {"name": "Bob Smith", "role": "Manager"},
      {"name": "Carol White", "role": "Designer"}
    ]
    
    # Act - User adds connections
    for conn in connections:
      stack.push(conn)
    
    # User previews what would be undone (peek)
    preview = stack.peek()
    assert preview["name"] == "Carol White", (
      f"Peek should show most recent connection (Carol)"
    )
    
    # User confirms undo (pop)
    undone = stack.pop()
    assert undone["name"] == "Carol White", (
      f"Pop should remove most recent connection (Carol)"
    )
    
    # Verify stack state
    assert stack.size() == 2, "Should have 2 connections left"
    
    # Next undo preview
    next_preview = stack.peek()
    assert next_preview["name"] == "Bob Smith", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Realistic Undo Feature\n"
      f"{'='*70}\n"
      f"📊 Scenario:   After undoing Carol, peek next undo target\n"
      f"✅ Expected:   Bob Smith (current top)\n"
      f"❌ Got:        {next_preview['name']}\n"
      f"💡 Use Case:  Peek shows what undo will remove, pop actually removes it\n"
      f"{'='*70}\n"
    )

  def test_peek_and_pop_with_complex_data(self):
    """Common case: Peek and pop with nested data structures"""
    # Arrange
    stack = Stack()
    complex_item = {
      "user": "John Doe",
      "profile": {
        "connections": 500,
        "endorsements": ["Python", "JavaScript"],
        "experience": [
          {"company": "A", "years": 2},
          {"company": "B", "years": 3}
        ]
      }
    }
    stack.push(complex_item)
    
    # Act
    peeked = stack.peek()
    popped = stack.pop()
    
    # Assert
    assert peeked == complex_item, "Peek should return complex structure"
    assert popped == complex_item, "Pop should return complex structure"
    assert peeked["profile"]["connections"] == 500, "Nested data accessible"
    assert len(popped["profile"]["endorsements"]) == 2, "Nested arrays work"
