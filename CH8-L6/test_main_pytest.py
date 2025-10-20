import pytest
from queue import Queue
from main import matchmake


class TestMatchmake:
  """Test suite for the matchmake() function"""

  def test_first_user_joins_queue(self):
    """Test first user joining an empty queue"""
    # Arrange
    queue = Queue()
    user = ("Ted", "join")
    
    # Act
    result = matchmake(queue, user)
    
    # Assert
    assert queue.items == ["Ted"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: First User Joins Queue\n"
      f"{'='*70}\n"
      f"📊 User: {user}\n"
      f"✅ Expected queue: ['Ted']\n"
      f"❌ Got queue:      {queue.items}\n"
      f"{'='*70}\n"
    )
    assert result == "No match found", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: First User Join Return Value\n"
      f"{'='*70}\n"
      f"📊 Queue size: 1 user\n"
      f"✅ Expected: 'No match found'\n"
      f"❌ Got:      '{result}'\n"
      f"💡 Need at least 4 users for a match\n"
      f"{'='*70}\n"
    )

  def test_multiple_users_join_no_match(self):
    """Test multiple users joining but not enough for a match (< 4)"""
    # Arrange
    queue = Queue()
    
    # Act
    matchmake(queue, ("Ted", "join"))
    matchmake(queue, ("Barney", "join"))
    result = matchmake(queue, ("Marshall", "join"))
    
    # Assert
    assert queue.items == ["Marshall", "Barney", "Ted"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Multiple Users Join - Queue State\n"
      f"{'='*70}\n"
      f"📊 Users joined: Ted, Barney, Marshall (3 users)\n"
      f"✅ Expected queue: ['Marshall', 'Barney', 'Ted']\n"
      f"❌ Got queue:      {queue.items}\n"
      f"💡 Queue should maintain FIFO order (tail → head)\n"
      f"{'='*70}\n"
    )
    assert result == "No match found", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Multiple Users Join - Return Value\n"
      f"{'='*70}\n"
      f"📊 Queue size: 3 users\n"
      f"✅ Expected: 'No match found'\n"
      f"❌ Got:      '{result}'\n"
      f"💡 Need at least 4 users for a match\n"
      f"{'='*70}\n"
    )

  def test_fourth_user_triggers_match(self):
    """Test that the 4th user triggers a match (pops first 2)"""
    # Arrange
    queue = Queue()
    matchmake(queue, ("Ted", "join"))
    matchmake(queue, ("Barney", "join"))
    matchmake(queue, ("Marshall", "join"))
    
    # Act
    result = matchmake(queue, ("Lily", "join"))
    
    # Assert
    assert queue.items == ["Lily", "Marshall"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fourth User Match - Queue State\n"
      f"{'='*70}\n"
      f"📊 After 4th user joins and match is made\n"
      f"✅ Expected queue: ['Lily', 'Marshall']\n"
      f"❌ Got queue:      {queue.items}\n"
      f"💡 First 2 users (Ted, Barney) should be popped\n"
      f"{'='*70}\n"
    )
    assert result == "Ted matched Barney!", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fourth User Match - Return Value\n"
      f"{'='*70}\n"
      f"📊 Queue had 4 users, first 2 matched\n"
      f"✅ Expected: 'Ted matched Barney!'\n"
      f"❌ Got:      '{result}'\n"
      f"💡 Format: '{'{user1} matched {user2}!'}'\n"
      f"{'='*70}\n"
    )

  def test_user_leaves_queue(self):
    """Test user leaving the queue using search_and_remove"""
    # Arrange
    queue = Queue()
    matchmake(queue, ("Carl", "join"))
    matchmake(queue, ("Robin", "join"))
    
    # Act
    result = matchmake(queue, ("Carl", "leave"))
    
    # Assert
    assert queue.items == ["Robin"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: User Leaves Queue - Queue State\n"
      f"{'='*70}\n"
      f"📊 Carl left the queue\n"
      f"✅ Expected queue: ['Robin']\n"
      f"❌ Got queue:      {queue.items}\n"
      f"💡 search_and_remove should remove Carl\n"
      f"{'='*70}\n"
    )
    assert result == "No match found", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: User Leaves Queue - Return Value\n"
      f"{'='*70}\n"
      f"📊 Queue size: 1 user after leave\n"
      f"✅ Expected: 'No match found'\n"
      f"❌ Got:      '{result}'\n"
      f"{'='*70}\n"
    )

  def test_user_leaves_empty_queue(self):
    """Test user leaving when queue becomes empty"""
    # Arrange
    queue = Queue()
    matchmake(queue, ("Robin", "join"))
    
    # Act
    result = matchmake(queue, ("Robin", "leave"))
    
    # Assert
    assert queue.items == [], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Leave Empty Queue - Queue State\n"
      f"{'='*70}\n"
      f"📊 Last user (Robin) left\n"
      f"✅ Expected queue: []\n"
      f"❌ Got queue:      {queue.items}\n"
      f"{'='*70}\n"
    )
    assert result == "No match found", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Leave Empty Queue - Return Value\n"
      f"{'='*70}\n"
      f"📊 Queue is now empty\n"
      f"✅ Expected: 'No match found'\n"
      f"❌ Got:      '{result}'\n"
      f"{'='*70}\n"
    )

  def test_bootdev_full_scenario(self):
    """Test complete Boot.dev scenario with joins, leaves, and matches"""
    # Arrange
    queue = Queue()
    expected_results = [
      (["Ted"], "No match found"),
      (["Barney", "Ted"], "No match found"),
      (["Marshall", "Barney", "Ted"], "No match found"),
      (["Lily", "Marshall"], "Ted matched Barney!"),
      (["Robin", "Lily", "Marshall"], "No match found"),
      (["Carl", "Robin"], "Marshall matched Lily!"),
      (["Robin"], "No match found"),
      ([], "No match found"),
    ]
    
    actions = [
      ("Ted", "join"),
      ("Barney", "join"),
      ("Marshall", "join"),
      ("Lily", "join"),
      ("Robin", "join"),
      ("Carl", "join"),
      ("Carl", "leave"),
      ("Robin", "leave"),
    ]
    
    # Act & Assert
    for i, (user, (expected_queue, expected_result)) in enumerate(zip(actions, expected_results)):
      result = matchmake(queue, user)
      
      assert queue.items == expected_queue, (
        f"\n{'='*70}\n"
        f"❌ TEST FAILED: Boot.dev Scenario Step {i+1} - Queue\n"
        f"{'='*70}\n"
        f"📊 Action: {user}\n"
        f"✅ Expected queue: {expected_queue}\n"
        f"❌ Got queue:      {queue.items}\n"
        f"{'='*70}\n"
      )
      assert result == expected_result, (
        f"\n{'='*70}\n"
        f"❌ TEST FAILED: Boot.dev Scenario Step {i+1} - Result\n"
        f"{'='*70}\n"
        f"📊 Action: {user}\n"
        f"✅ Expected: '{expected_result}'\n"
        f"❌ Got:      '{result}'\n"
        f"{'='*70}\n"
      )

  def test_sequential_matches(self):
    """Test multiple matches happening in sequence"""
    # Arrange
    queue = Queue()
    matchmake(queue, ("Ranjit", "join"))
    
    # Act
    result1 = matchmake(queue, ("Ranjit", "leave"))
    result2 = matchmake(queue, ("Victoria", "join"))
    result3 = matchmake(queue, ("Quinn", "join"))
    result4 = matchmake(queue, ("Zoey", "join"))
    result5 = matchmake(queue, ("Stella", "join"))
    
    # Assert - After Ranjit leaves
    assert result1 == "No match found", "Empty queue should return no match"
    
    # Assert - First match (Victoria & Quinn matched)
    assert result5 == "Victoria matched Quinn!", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Sequential Matches - First Match\n"
      f"{'='*70}\n"
      f"📊 4 users in queue: Victoria, Quinn, Zoey, Stella\n"
      f"✅ Expected: 'Victoria matched Quinn!'\n"
      f"❌ Got:      '{result5}'\n"
      f"💡 First 2 in queue should match (FIFO)\n"
      f"{'='*70}\n"
    )
    
    assert queue.items == ["Stella", "Zoey"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Sequential Matches - Final Queue\n"
      f"{'='*70}\n"
      f"📊 After Victoria & Quinn matched\n"
      f"✅ Expected queue: ['Stella', 'Zoey']\n"
      f"❌ Got queue:      {queue.items}\n"
      f"{'='*70}\n"
    )

  def test_leave_user_not_in_queue(self):
    """Test leaving when user is not in the queue"""
    # Arrange
    queue = Queue()
    matchmake(queue, ("Ted", "join"))
    
    # Act
    result = matchmake(queue, ("Barney", "leave"))
    
    # Assert
    assert queue.items == ["Ted"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Leave Non-Existent User - Queue State\n"
      f"{'='*70}\n"
      f"📊 Barney not in queue, tried to leave\n"
      f"✅ Expected queue: ['Ted']\n"
      f"❌ Got queue:      {queue.items}\n"
      f"💡 Queue should remain unchanged\n"
      f"{'='*70}\n"
    )
    assert result == "No match found", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Leave Non-Existent User - Return Value\n"
      f"{'='*70}\n"
      f"📊 Queue still has only 1 user\n"
      f"✅ Expected: 'No match found'\n"
      f"❌ Got:      '{result}'\n"
      f"{'='*70}\n"
    )

  def test_exactly_four_users_triggers_match(self):
    """Test that exactly 4 users triggers a match"""
    # Arrange
    queue = Queue()
    
    # Act
    matchmake(queue, ("A", "join"))
    matchmake(queue, ("B", "join"))
    matchmake(queue, ("C", "join"))
    result = matchmake(queue, ("D", "join"))
    
    # Assert
    assert result == "A matched B!", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Exactly 4 Users - Match Result\n"
      f"{'='*70}\n"
      f"📊 Queue reached exactly 4 users\n"
      f"✅ Expected: 'A matched B!'\n"
      f"❌ Got:      '{result}'\n"
      f"💡 First 2 users (A, B) should match\n"
      f"{'='*70}\n"
    )
    assert queue.items == ["D", "C"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Exactly 4 Users - Queue State\n"
      f"{'='*70}\n"
      f"📊 After matching first 2 users\n"
      f"✅ Expected queue: ['D', 'C']\n"
      f"❌ Got queue:      {queue.items}\n"
      f"{'='*70}\n"
    )

  def test_five_users_triggers_match(self):
    """Test that 5+ users triggers a match"""
    # Arrange
    queue = Queue()
    matchmake(queue, ("A", "join"))
    matchmake(queue, ("B", "join"))
    matchmake(queue, ("C", "join"))
    matchmake(queue, ("D", "join"))
    
    # Act
    result = matchmake(queue, ("E", "join"))
    
    # Assert
    assert result == "A matched B!", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Five Users - Match Result\n"
      f"{'='*70}\n"
      f"📊 Queue has 5 users\n"
      f"✅ Expected: 'A matched B!'\n"
      f"❌ Got:      '{result}'\n"
      f"{'='*70}\n"
    )
    assert queue.items == ["E", "D", "C"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Five Users - Queue State\n"
      f"{'='*70}\n"
      f"📊 After matching first 2 of 5 users\n"
      f"✅ Expected queue: ['E', 'D', 'C']\n"
      f"❌ Got queue:      {queue.items}\n"
      f"💡 Should have 3 users remaining\n"
      f"{'='*70}\n"
    )

  def test_match_format_string(self):
    """Test that match result string is formatted correctly"""
    # Arrange
    queue = Queue()
    matchmake(queue, ("Alice", "join"))
    matchmake(queue, ("Bob", "join"))
    matchmake(queue, ("Charlie", "join"))
    
    # Act
    result = matchmake(queue, ("Diana", "join"))
    
    # Assert
    assert result == "Alice matched Bob!", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Match Format String\n"
      f"{'='*70}\n"
      f"📊 Matching Alice and Bob\n"
      f"✅ Expected: 'Alice matched Bob!'\n"
      f"❌ Got:      '{result}'\n"
      f"💡 Format must be: '{'{user1} matched {user2}!'}'\n"
      f"   - user1 = first popped user\n"
      f"   - user2 = second popped user\n"
      f"   - Must include exclamation mark!\n"
      f"{'='*70}\n"
    )

  def test_user_leaves_from_middle_of_queue(self):
    """Test that search_and_remove can remove from middle of queue"""
    # Arrange
    queue = Queue()
    matchmake(queue, ("A", "join"))
    matchmake(queue, ("B", "join"))
    matchmake(queue, ("C", "join"))
    
    # Act
    result = matchmake(queue, ("B", "leave"))
    
    # Assert
    assert queue.items == ["C", "A"], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Leave From Middle - Queue State\n"
      f"{'='*70}\n"
      f"📊 B (middle user) left queue\n"
      f"✅ Expected queue: ['C', 'A']\n"
      f"❌ Got queue:      {queue.items}\n"
      f"💡 search_and_remove should work for any position\n"
      f"{'='*70}\n"
    )
    assert result == "No match found", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Leave From Middle - Return Value\n"
      f"{'='*70}\n"
      f"📊 Only 2 users remain\n"
      f"✅ Expected: 'No match found'\n"
      f"❌ Got:      '{result}'\n"
      f"{'='*70}\n"
    )
