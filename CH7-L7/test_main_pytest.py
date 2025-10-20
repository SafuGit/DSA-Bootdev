import pytest
from main import is_balanced


class TestIsBalanced:
  """Test suite for is_balanced() function - Using Stack for balanced parentheses"""

  def test_single_opening_parenthesis_bootdev(self):
    """Boot.dev test case: Single opening parenthesis (unbalanced)"""
    # Arrange
    input_str = "("
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Single Opening Parenthesis (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Unclosed opening parenthesis is unbalanced\n"
      f"{'='*70}\n"
    )

  def test_balanced_pair_bootdev(self):
    """Boot.dev test case: Single balanced pair"""
    # Arrange
    input_str = "()"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = True
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Balanced Pair (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Single pair should be balanced\n"
      f"{'='*70}\n"
    )

  def test_nested_pair_bootdev(self):
    """Boot.dev test case: Nested parentheses"""
    # Arrange
    input_str = "(())"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = True
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Nested Pair (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Properly nested parentheses are balanced\n"
      f"{'='*70}\n"
    )

  def test_two_separate_pairs_bootdev(self):
    """Boot.dev test case: Two separate balanced pairs"""
    # Arrange
    input_str = "()()"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = True
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Two Separate Pairs (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Multiple separate pairs are balanced\n"
      f"{'='*70}\n"
    )

  def test_extra_closing_bootdev(self):
    """Boot.dev test case: Extra closing parenthesis"""
    # Arrange
    input_str = "(()))"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Extra Closing Parenthesis (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Extra closing parenthesis makes it unbalanced\n"
      f"{'='*70}\n"
    )

  def test_complex_nested_bootdev(self):
    """Boot.dev test case: Complex nested and sequential"""
    # Arrange
    input_str = "((())())"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = True
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Complex Nested (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Complex nesting with multiple levels is balanced\n"
      f"{'='*70}\n"
    )

  def test_missing_closing_bootdev(self):
    """Boot.dev test case: Missing closing parentheses"""
    # Arrange
    input_str = "(()(("
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Missing Closing (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Unclosed opening parentheses are unbalanced\n"
      f"{'='*70}\n"
    )

  def test_wrong_order_bootdev(self):
    """Boot.dev test case: Closing before opening"""
    # Arrange
    input_str = ")("
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Wrong Order (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Closing parenthesis before opening is unbalanced\n"
      f"{'='*70}\n"
    )

  def test_mixed_unbalanced_bootdev(self):
    """Boot.dev test case: Mixed balanced and unbalanced start"""
    # Arrange
    input_str = ")()(()"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Mixed Unbalanced (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Starting with closing makes it unbalanced\n"
      f"{'='*70}\n"
    )

  def test_early_closing_bootdev(self):
    """Boot.dev test case: Extra closing in middle"""
    # Arrange
    input_str = "())(()"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Early Closing (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Extra closing in middle is unbalanced\n"
      f"{'='*70}\n"
    )

  def test_empty_string(self):
    """Edge case: Empty string is balanced"""
    # Arrange
    input_str = ""
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = True
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Empty String\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}' (empty)\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Empty string has no parentheses, so it's balanced\n"
      f"{'='*70}\n"
    )

  def test_single_closing(self):
    """Edge case: Single closing parenthesis"""
    # Arrange
    input_str = ")"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Single Closing\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Closing without opening is unbalanced\n"
      f"{'='*70}\n"
    )

  def test_deeply_nested(self):
    """Common case: Deeply nested parentheses"""
    # Arrange
    input_str = "((((()))))"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = True
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Deeply Nested\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Deep nesting should be balanced if matched\n"
      f"{'='*70}\n"
    )

  def test_many_pairs(self):
    """Common case: Many sequential pairs"""
    # Arrange
    input_str = "()()()()()"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = True
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Many Sequential Pairs\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Multiple sequential pairs are balanced\n"
      f"{'='*70}\n"
    )

  def test_complex_mixed_pattern(self):
    """Common case: Complex mixed nesting and sequential"""
    # Arrange
    input_str = "((()())())(())"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = True
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Complex Mixed Pattern\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Complex patterns should work if balanced\n"
      f"{'='*70}\n"
    )

  def test_all_opening(self):
    """Edge case: All opening parentheses"""
    # Arrange
    input_str = "((((("
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: All Opening\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    All opening with no closing is unbalanced\n"
      f"{'='*70}\n"
    )

  def test_all_closing(self):
    """Edge case: All closing parentheses"""
    # Arrange
    input_str = ")))))"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: All Closing\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    All closing with no opening is unbalanced\n"
      f"{'='*70}\n"
    )

  def test_mismatched_count_opening(self):
    """Common case: More opening than closing"""
    # Arrange
    input_str = "((())"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: More Opening Than Closing\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Unequal counts mean unbalanced\n"
      f"{'='*70}\n"
    )

  def test_mismatched_count_closing(self):
    """Common case: More closing than opening"""
    # Arrange
    input_str = "(())))"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: More Closing Than Opening\n"
      f"{'='*70}\n"
      f"📊 Input:    '{input_str}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Unequal counts mean unbalanced\n"
      f"{'='*70}\n"
    )

  def test_realistic_script_balanced(self):
    """Real-world scenario: Balanced LockedIn script syntax"""
    # Arrange
    input_str = "((filter(role))(map(salary)))"
    
    # Act
    # Extract only parentheses for testing
    parens_only = "".join(c for c in input_str if c in "()")
    result = is_balanced(parens_only)
    
    # Assert
    expected = True
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Realistic Balanced Script\n"
      f"{'='*70}\n"
      f"📊 Script:   '{input_str}'\n"
      f"📊 Parens:   '{parens_only}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Use Case: Valid LockedIn HR automation script\n"
      f"{'='*70}\n"
    )

  def test_realistic_script_unbalanced(self):
    """Real-world scenario: Unbalanced LockedIn script syntax"""
    # Arrange
    input_str = "((filter(role)(map(salary))"
    
    # Act
    # Extract only parentheses for testing
    parens_only = "".join(c for c in input_str if c in "()")
    result = is_balanced(parens_only)
    
    # Assert
    expected = False
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Realistic Unbalanced Script\n"
      f"{'='*70}\n"
      f"📊 Script:   '{input_str}'\n"
      f"📊 Parens:   '{parens_only}'\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Use Case: Invalid LockedIn script (syntax error)\n"
      f"{'='*70}\n"
    )

  def test_return_type_boolean(self):
    """Validation: Function must return boolean"""
    # Arrange
    input_str = "()"
    
    # Act
    result = is_balanced(input_str)
    
    # Assert
    assert isinstance(result, bool), (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Return Type Validation\n"
      f"{'='*70}\n"
      f"✅ Expected: bool type\n"
      f"❌ Got:      {type(result).__name__}\n"
      f"💡 Note:    Function must return True or False, not {type(result).__name__}\n"
      f"{'='*70}\n"
    )
