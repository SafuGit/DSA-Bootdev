import pytest
from main import Queue


class TestQueue:
  """Test suite for the Queue class implementation"""

  def test_push_single_item(self):
    """Test pushing a single item to the queue"""
    # Arrange
    queue = Queue()
    
    # Act
    queue.push("Rand")
    
    # Assert
    assert queue.size() == 1, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Push Single Item\n"
      f"{'='*70}\n"
      f"📊 Operation: push('Rand')\n"
      f"✅ Expected size: 1\n"
      f"❌ Got size:      {queue.size()}\n"
      f"{'='*70}\n"
    )

  def test_push_multiple_items(self):
    """Test pushing multiple items to the queue"""
    # Arrange
    queue = Queue()
    
    # Act
    queue.push("Rand")
    queue.push("Mat")
    queue.push("Perrin")
    
    # Assert
    assert queue.size() == 3, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Push Multiple Items\n"
      f"{'='*70}\n"
      f"📊 Operations: push('Rand'), push('Mat'), push('Perrin')\n"
      f"✅ Expected size: 3\n"
      f"❌ Got size:      {queue.size()}\n"
      f"{'='*70}\n"
    )

  def test_pop_single_item(self):
    """Test popping a single item from the queue (FIFO order)"""
    # Arrange
    queue = Queue()
    queue.push("Egwene")
    
    # Act
    result = queue.pop()
    
    # Assert
    assert result == "Egwene", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Pop Single Item\n"
      f"{'='*70}\n"
      f"📊 Setup:    push('Egwene')\n"
      f"📊 Operation: pop()\n"
      f"✅ Expected: 'Egwene'\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_pop_fifo_order(self):
    """Test that pop follows FIFO (First In First Out) order"""
    # Arrange
    queue = Queue()
    queue.push("Rand")
    queue.push("Mat")
    queue.push("Perrin")
    
    # Act
    first = queue.pop()
    second = queue.pop()
    third = queue.pop()
    
    # Assert
    expected_order = ["Rand", "Mat", "Perrin"]
    actual_order = [first, second, third]
    assert actual_order == expected_order, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Pop FIFO Order\n"
      f"{'='*70}\n"
      f"📊 Push order: ['Rand', 'Mat', 'Perrin']\n"
      f"✅ Expected pop order: {expected_order}\n"
      f"❌ Got pop order:      {actual_order}\n"
      f"💡 Queue should follow FIFO (First In First Out)\n"
      f"{'='*70}\n"
    )

  def test_pop_empty_queue(self):
    """Test popping from an empty queue returns None"""
    # Arrange
    queue = Queue()
    
    # Act
    result = queue.pop()
    
    # Assert
    assert result is None, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Pop Empty Queue\n"
      f"{'='*70}\n"
      f"📊 Operation: pop() on empty queue\n"
      f"✅ Expected: None\n"
      f"❌ Got:      {result}\n"
      f"💡 Should handle IndexError and return None\n"
      f"{'='*70}\n"
    )

  def test_peek_returns_head_without_removing(self):
    """Test that peek returns the head item without removing it"""
    # Arrange
    queue = Queue()
    queue.push("Nynaeve")
    queue.push("Egwene")
    
    # Act
    peeked = queue.peek()
    size_after_peek = queue.size()
    
    # Assert
    assert peeked == "Nynaeve", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Peek Returns Head\n"
      f"{'='*70}\n"
      f"📊 Queue: ['Nynaeve' (head), 'Egwene' (tail)]\n"
      f"✅ Expected peek: 'Nynaeve'\n"
      f"❌ Got peek:      {peeked}\n"
      f"{'='*70}\n"
    )
    assert size_after_peek == 2, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Peek Doesn't Remove Item\n"
      f"{'='*70}\n"
      f"📊 Operation: peek()\n"
      f"✅ Expected size after peek: 2\n"
      f"❌ Got size after peek:      {size_after_peek}\n"
      f"💡 Peek should not modify the queue\n"
      f"{'='*70}\n"
    )

  def test_peek_empty_queue(self):
    """Test peeking at an empty queue returns None"""
    # Arrange
    queue = Queue()
    
    # Act
    result = queue.peek()
    
    # Assert
    assert result is None, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Peek Empty Queue\n"
      f"{'='*70}\n"
      f"📊 Operation: peek() on empty queue\n"
      f"✅ Expected: None\n"
      f"❌ Got:      {result}\n"
      f"💡 Should handle IndexError and return None\n"
      f"{'='*70}\n"
    )

  def test_size_empty_queue(self):
    """Test size of an empty queue is 0"""
    # Arrange
    queue = Queue()
    
    # Act
    result = queue.size()
    
    # Assert
    assert result == 0, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Size Empty Queue\n"
      f"{'='*70}\n"
      f"📊 Operation: size() on empty queue\n"
      f"✅ Expected: 0\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_size_after_operations(self):
    """Test size updates correctly after push and pop operations"""
    # Arrange
    queue = Queue()
    
    # Act & Assert
    queue.push("Moiraine")
    assert queue.size() == 1, "Size should be 1 after 1 push"
    
    queue.push("Lan")
    assert queue.size() == 2, "Size should be 2 after 2 pushes"
    
    queue.pop()
    assert queue.size() == 1, "Size should be 1 after 1 pop"
    
    queue.pop()
    result = queue.size()
    assert result == 0, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Size After Operations\n"
      f"{'='*70}\n"
      f"📊 Operations: push, push, pop, pop\n"
      f"✅ Expected final size: 0\n"
      f"❌ Got final size:      {result}\n"
      f"{'='*70}\n"
    )

  def test_mixed_operations_scenario(self):
    """Test realistic scenario with mixed operations"""
    # Arrange
    queue = Queue()
    
    # Act
    queue.push("Thom")
    first_pop = queue.pop()
    queue.push("Loial")
    peek_result = queue.peek()
    final_size = queue.size()
    
    # Assert
    assert first_pop == "Thom", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Mixed Operations - First Pop\n"
      f"{'='*70}\n"
      f"📊 Operations: push('Thom'), pop()\n"
      f"✅ Expected: 'Thom'\n"
      f"❌ Got:      {first_pop}\n"
      f"{'='*70}\n"
    )
    assert peek_result == "Loial", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Mixed Operations - Peek\n"
      f"{'='*70}\n"
      f"📊 Queue state: ['Loial']\n"
      f"✅ Expected peek: 'Loial'\n"
      f"❌ Got peek:      {peek_result}\n"
      f"{'='*70}\n"
    )
    assert final_size == 1, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Mixed Operations - Final Size\n"
      f"{'='*70}\n"
      f"📊 After: push, pop, push\n"
      f"✅ Expected size: 1\n"
      f"❌ Got size:      {final_size}\n"
      f"{'='*70}\n"
    )

  def test_bootdev_example_case_1(self):
    """Test Boot.dev example: push Rand, push Mat, peek, pop"""
    # Arrange
    queue = Queue()
    
    # Act
    queue.push("Rand")
    queue.push("Mat")
    peek_result = queue.peek()
    pop_result = queue.pop()
    
    # Assert
    expected_outputs = ["Rand", "Rand"]
    actual_outputs = [peek_result, pop_result]
    assert actual_outputs == expected_outputs, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Boot.dev Example Case 1\n"
      f"{'='*70}\n"
      f"📊 Operations: push('Rand'), push('Mat'), peek(), pop()\n"
      f"✅ Expected: {expected_outputs}\n"
      f"❌ Got:      {actual_outputs}\n"
      f"💡 [peek, pop] should both return 'Rand' (head of queue)\n"
      f"{'='*70}\n"
    )

  def test_bootdev_example_case_2(self):
    """Test Boot.dev example: push, push, size, pop, size"""
    # Arrange
    queue = Queue()
    
    # Act
    queue.push("Egwene")
    queue.push("Nynaeve")
    size1 = queue.size()
    pop_result = queue.pop()
    size2 = queue.size()
    
    # Assert
    expected_outputs = [2, "Egwene", 1]
    actual_outputs = [size1, pop_result, size2]
    assert actual_outputs == expected_outputs, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Boot.dev Example Case 2\n"
      f"{'='*70}\n"
      f"📊 Operations: push('Egwene'), push('Nynaeve'), size(), pop(), size()\n"
      f"✅ Expected: {expected_outputs}\n"
      f"❌ Got:      {actual_outputs}\n"
      f"💡 [size, pop, size] = [2, 'Egwene', 1]\n"
      f"{'='*70}\n"
    )

  def test_bootdev_submit_case_empty_operations(self):
    """Test Boot.dev submit case: operations on empty queue"""
    # Arrange
    queue = Queue()
    
    # Act
    pop_result = queue.pop()
    peek_result = queue.peek()
    size_result = queue.size()
    
    # Assert
    expected_outputs = [None, None, 0]
    actual_outputs = [pop_result, peek_result, size_result]
    assert actual_outputs == expected_outputs, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Boot.dev Submit Case - Empty Operations\n"
      f"{'='*70}\n"
      f"📊 Operations on empty queue: pop(), peek(), size()\n"
      f"✅ Expected: {expected_outputs}\n"
      f"❌ Got:      {actual_outputs}\n"
      f"💡 Empty queue should return [None, None, 0]\n"
      f"{'='*70}\n"
    )

  def test_bootdev_submit_case_multiple_pops(self):
    """Test Boot.dev submit case: push 3, pop 2, peek"""
    # Arrange
    queue = Queue()
    
    # Act
    queue.push("Perrin")
    queue.push("Moiraine")
    queue.push("Lan")
    pop1 = queue.pop()
    pop2 = queue.pop()
    peek_result = queue.peek()
    
    # Assert
    expected_outputs = ["Perrin", "Moiraine", "Lan"]
    actual_outputs = [pop1, pop2, peek_result]
    assert actual_outputs == expected_outputs, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Boot.dev Submit Case - Multiple Pops\n"
      f"{'='*70}\n"
      f"📊 Push order: ['Perrin', 'Moiraine', 'Lan']\n"
      f"📊 Operations: pop(), pop(), peek()\n"
      f"✅ Expected: {expected_outputs}\n"
      f"❌ Got:      {actual_outputs}\n"
      f"💡 Should pop in FIFO order, then peek at remaining\n"
      f"{'='*70}\n"
    )

  def test_queue_maintains_order_with_many_items(self):
    """Test queue maintains FIFO order with many items"""
    # Arrange
    queue = Queue()
    items = ["Item1", "Item2", "Item3", "Item4", "Item5"]
    
    # Act
    for item in items:
      queue.push(item)
    
    popped_items = []
    for _ in range(len(items)):
      popped_items.append(queue.pop())
    
    # Assert
    assert popped_items == items, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Queue Order with Many Items\n"
      f"{'='*70}\n"
      f"📊 Push order: {items}\n"
      f"✅ Expected pop order: {items}\n"
      f"❌ Got pop order:      {popped_items}\n"
      f"💡 Queue must maintain FIFO order\n"
      f"{'='*70}\n"
    )

  def test_alternating_push_pop(self):
    """Test alternating push and pop operations"""
    # Arrange
    queue = Queue()
    
    # Act & Assert
    queue.push("A")
    assert queue.pop() == "A", "First item should be 'A'"
    
    queue.push("B")
    queue.push("C")
    assert queue.pop() == "B", "Second item should be 'B'"
    
    queue.push("D")
    assert queue.peek() == "C", "Head should be 'C'"
    assert queue.size() == 2, "Size should be 2"
    
    result1 = queue.pop()
    result2 = queue.pop()
    
    assert [result1, result2] == ["C", "D"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Alternating Push/Pop\n"
      f"{'='*70}\n"
      f"📊 Final pops after alternating operations\n"
      f"✅ Expected: ['C', 'D']\n"
      f"❌ Got:      {[result1, result2]}\n"
      f"{'='*70}\n"
    )
