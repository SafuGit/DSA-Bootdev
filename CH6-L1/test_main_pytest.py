import pytest
from main import count_marketers


class TestCountMarketers:
  """Test suite for the count_marketers() function - Case-insensitive job title counting"""

  def test_empty_list(self):
    """Edge case: Empty list of job titles"""
    # Arrange
    input_data = []
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 0
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Empty List\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Empty list should return 0 marketers\n"
      f"{'='*70}\n"
    )

  def test_single_marketer(self):
    """Edge case: Single marketer in list"""
    # Arrange
    input_data = ["marketer"]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 1
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Single Marketer\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    List with one marketer should return 1\n"
      f"{'='*70}\n"
    )

  def test_no_marketers(self):
    """Edge case: No marketers in list"""
    # Arrange
    input_data = ["developer", "designer", "product manager"]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 0
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: No Marketers\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    List with no marketers should return 0\n"
      f"{'='*70}\n"
    )

  def test_mixed_titles_one_marketer_bootdev(self):
    """Boot.dev test case: Mixed job titles with one marketer"""
    # Arrange
    input_data = ["developer", "marketer", "designer"]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 1
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Mixed Titles - One Marketer (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should find the single 'marketer' among other titles\n"
      f"{'='*70}\n"
    )

  def test_multiple_marketers_bootdev(self):
    """Boot.dev test case: Multiple marketers with other titles"""
    # Arrange
    input_data = ["marketer", "marketer", "developer", "marketer"]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 3
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Multiple Marketers (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should count all 3 marketers in the list\n"
      f"{'='*70}\n"
    )

  def test_case_insensitive_all_uppercase_bootdev(self):
    """Boot.dev test case: Case-insensitive matching with various cases"""
    # Arrange
    input_data = ["MARKETER", "Marketer", "marketer"]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 3
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Case Insensitive Matching (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Must handle MARKETER, Marketer, and marketer as same\n"
      f"{'='*70}\n"
    )

  def test_case_variations_extended(self):
    """Common case: Various case combinations"""
    # Arrange
    input_data = ["MaRkEtEr", "MARKETER", "marketer", "Marketer", "MarKETer"]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 5
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Extended Case Variations\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    All variations should be counted regardless of casing\n"
      f"{'='*70}\n"
    )

  def test_similar_but_not_marketer(self):
    """Common case: Similar job titles that aren't 'marketer'"""
    # Arrange
    input_data = ["marketing manager", "market analyst", "marketer", "marketing"]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 1
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Similar But Not Marketer\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Only exact match 'marketer' counts, not partial matches\n"
      f"            'marketing manager', 'market analyst', 'marketing' ≠ 'marketer'\n"
      f"{'='*70}\n"
    )

  def test_all_marketers(self):
    """Common case: List where everyone is a marketer"""
    # Arrange
    input_data = ["marketer", "MARKETER", "Marketer", "marketer", "MarKeTer"]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 5
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: All Marketers\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should count all 5 when everyone is a marketer\n"
      f"{'='*70}\n"
    )

  def test_large_list_few_marketers(self):
    """Common case: Large list with few marketers"""
    # Arrange
    input_data = [
      "developer", "designer", "marketer", "engineer", 
      "analyst", "MARKETER", "architect", "consultant",
      "manager", "Marketer", "director"
    ]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 3
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Large List Few Marketers\n"
      f"{'='*70}\n"
      f"📊 Input:    {len(input_data)} job titles\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should find 3 marketers among 11 titles\n"
      f"{'='*70}\n"
    )

  def test_whitespace_sensitivity(self):
    """Edge case: Whitespace should not affect matching"""
    # Arrange
    input_data = ["marketer", " marketer", "marketer ", " marketer "]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    # Note: Based on typical implementation, whitespace may or may not be trimmed
    # This test documents expected behavior - adjust if Boot.dev expects different
    expected = 1  # Only exact "marketer" without spaces
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Whitespace Sensitivity\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected} (exact match only)\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Strings with leading/trailing spaces may not match\n"
      f"            If this fails, implementation might need .strip()\n"
      f"{'='*70}\n"
    )

  def test_duplicate_titles_with_marketers(self):
    """Common case: Many duplicates including marketers"""
    # Arrange
    input_data = [
      "developer", "developer", "marketer", "developer",
      "marketer", "designer", "marketer", "designer"
    ]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 3
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Duplicate Titles With Marketers\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should count all 3 marketer occurrences\n"
      f"{'='*70}\n"
    )

  def test_return_type(self):
    """Validation: Ensure function returns an integer"""
    # Arrange
    input_data = ["marketer", "developer"]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    assert isinstance(result, int), (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Return Type Validation\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: Integer type\n"
      f"❌ Got:      {type(result).__name__}\n"
      f"💡 Note:    Function must return an int, not {type(result).__name__}\n"
      f"{'='*70}\n"
    )

  def test_case_preservation_in_input(self):
    """Validation: Ensure function doesn't modify input list"""
    # Arrange
    input_data = ["MARKETER", "Developer", "Marketer"]
    original = input_data.copy()
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    assert input_data == original, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Input List Modified\n"
      f"{'='*70}\n"
      f"📊 Original: {original}\n"
      f"❌ Modified: {input_data}\n"
      f"💡 Note:    Function should not modify the input list\n"
      f"{'='*70}\n"
    )
    
    # Also verify the count is correct
    assert result == 2, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Case Preservation Count\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: 2\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_realistic_linkedin_scenario(self):
    """Real-world scenario: Typical LockedIn user job titles"""
    # Arrange
    input_data = [
      "Software Engineer",
      "Product Manager",
      "Marketing Manager",
      "marketer",
      "Data Scientist",
      "MARKETER",
      "UX Designer",
      "Marketer",
      "DevOps Engineer",
      "marketer"
    ]
    
    # Act
    result = count_marketers(input_data)
    
    # Assert
    expected = 4
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Realistic LockedIn Scenario\n"
      f"{'='*70}\n"
      f"📊 Input:    {len(input_data)} diverse job titles\n"
      f"✅ Expected: {expected} marketers\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should find 4 'marketer' titles (case-insensitive)\n"
      f"            'Marketing Manager' is NOT 'marketer'\n"
      f"{'='*70}\n"
    )
