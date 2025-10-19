import pytest
from main import fib


class TestFibonacci:
  """Test suite for the fib() function - Polynomial time implementation"""

  def test_fib_zero(self):
    """Edge case: First Fibonacci number (base case)"""
    # Arrange
    n = 0
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 0
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 0\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_fib_one(self):
    """Edge case: Second Fibonacci number (base case)"""
    # Arrange
    n = 1
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 1
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 1\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_fib_two(self):
    """Edge case: Third Fibonacci number (first computed value)"""
    # Arrange
    n = 2
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 1
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 2\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected} (0 + 1)\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_fib_three(self):
    """Common case: Fourth Fibonacci number"""
    # Arrange
    n = 3
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 2
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 3\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected} (1 + 1)\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_fib_four(self):
    """Common case: Fifth Fibonacci number"""
    # Arrange
    n = 4
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 3
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 4\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected} (1 + 2)\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_fib_five(self):
    """Common case: Sixth Fibonacci number"""
    # Arrange
    n = 5
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 5
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 5\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected} (2 + 3)\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_fib_six(self):
    """Real-world case: 6 weeks of influencer growth"""
    # Arrange
    n = 6
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 8
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 6 (6 weeks of growth)\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected} followers (3 + 5)\n"
      f"❌ Got:      {result}\n"
      f"💡 Context:  After 6 weeks, influencer should have 8 followers\n"
      f"{'='*70}\n"
    )

  def test_fib_seven(self):
    """Real-world case: 7 weeks of influencer growth"""
    # Arrange
    n = 7
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 13
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 7 (7 weeks of growth)\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected} followers (5 + 8)\n"
      f"❌ Got:      {result}\n"
      f"💡 Context:  After 7 weeks, influencer should have 13 followers\n"
      f"{'='*70}\n"
    )

  def test_fib_ten(self):
    """Common case: Double-digit index"""
    # Arrange
    n = 10
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 55
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 10\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_fib_fifteen(self):
    """Common case: Mid-range Fibonacci number"""
    # Arrange
    n = 15
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 610
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 15\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_fib_twenty(self):
    """Performance test: Larger index (polynomial time should handle easily)"""
    # Arrange
    n = 20
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 6765
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 20\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Polynomial algorithm should compute this quickly\n"
      f"{'='*70}\n"
    )

  def test_fib_thirty(self):
    """Performance test: Large index (exponential time would be too slow)"""
    # Arrange
    n = 30
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 832040
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 30\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Exponential algorithm would take forever!\n"
      f"{'='*70}\n"
    )

  def test_fib_sequence_first_ten(self):
    """Validation test: First 10 Fibonacci numbers in sequence"""
    # Arrange
    expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    # Act
    result_sequence = [fib(i) for i in range(10)]
    
    # Assert
    assert result_sequence == expected_sequence, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: First 10 Fibonacci Numbers\n"
      f"{'='*70}\n"
      f"📊 Indices:  0, 1, 2, 3, 4, 5, 6, 7, 8, 9\n"
      f"✅ Expected: {expected_sequence}\n"
      f"❌ Got:      {result_sequence}\n"
      f"{'='*70}\n"
    )

  def test_fib_influencer_growth_realistic(self):
    """Real-world scenario: 12 weeks of influencer analytics"""
    # Arrange
    weeks = 12
    
    # Act
    result = fib(weeks)
    
    # Assert
    expected = 144
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: 12-Week Influencer Growth Analytics\n"
      f"{'='*70}\n"
      f"📊 Weeks:    {weeks}\n"
      f"✅ Expected: {expected} followers\n"
      f"❌ Got:      {result} followers\n"
      f"💡 Context:  Analytics page should load quickly with O(n) time\n"
      f"{'='*70}\n"
    )

  def test_fib_performance_large_index(self):
    """Performance test: Very large index (proves polynomial efficiency)"""
    # Arrange
    n = 50
    
    # Act
    result = fib(n)
    
    # Assert
    expected = 12586269025
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Fibonacci at Index 50\n"
      f"{'='*70}\n"
      f"📊 Input:    fib({n})\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    This would never complete with exponential algorithm!\n"
      f"            Polynomial O(n) makes this instant.\n"
      f"{'='*70}\n"
    )
