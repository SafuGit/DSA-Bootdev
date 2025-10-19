import pytest
from main import selection_sort


class TestSelectionSort:
  """Test suite for the selection_sort() function"""

  def test_empty_list(self):
    """Edge case: Empty list should return empty list"""
    # Arrange
    input_data = []
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = []
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Empty List\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_single_element(self):
    """Edge case: Single element list should return unchanged"""
    # Arrange
    input_data = [42]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [42]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Single Element\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_two_elements_unsorted(self):
    """Edge case: Two elements requiring a swap"""
    # Arrange
    input_data = [5, 2]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [2, 5]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Two Elements Unsorted\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_two_elements_sorted(self):
    """Edge case: Two elements already in order"""
    # Arrange
    input_data = [3, 7]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [3, 7]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Two Elements Already Sorted\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_already_sorted(self):
    """Best case: List already in ascending order"""
    # Arrange
    input_data = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Already Sorted List\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_reverse_sorted(self):
    """Worst case: List in descending order (reverse sorted)"""
    # Arrange
    input_data = [9, 7, 5, 3, 1]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [1, 3, 5, 7, 9]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Reverse Sorted List\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_random_order(self):
    """Common case: Random order list"""
    # Arrange
    input_data = [64, 25, 12, 22, 11]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [11, 12, 22, 25, 64]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Random Order List\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_with_duplicates(self):
    """Common case: List with duplicate values"""
    # Arrange
    input_data = [5, 2, 8, 2, 9, 1, 5, 5]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [1, 2, 2, 5, 5, 5, 8, 9]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: List With Duplicates\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_all_same_values(self):
    """Edge case: All elements are identical"""
    # Arrange
    input_data = [7, 7, 7, 7, 7]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [7, 7, 7, 7, 7]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: All Same Values\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_negative_numbers(self):
    """Common case: List with negative numbers"""
    # Arrange
    input_data = [3, -1, 4, -5, 2, 0]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [-5, -1, 0, 2, 3, 4]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Negative Numbers\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_influencer_follower_counts_small(self):
    """Real-world scenario: Sorting influencer follower counts (small dataset)"""
    # Arrange
    input_data = [15000, 2500, 50000, 8000, 1200]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [1200, 2500, 8000, 15000, 50000]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Influencer Follower Counts (Small)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_influencer_follower_counts_medium(self):
    """Real-world scenario: Sorting influencer follower counts (medium dataset)"""
    # Arrange
    input_data = [100000, 5000, 250000, 75000, 15000, 500000, 30000, 10000]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [5000, 10000, 15000, 30000, 75000, 100000, 250000, 500000]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Influencer Follower Counts (Medium)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_large_dataset(self):
    """Performance test: Larger dataset"""
    # Arrange
    input_data = [89, 34, 21, 78, 45, 12, 67, 90, 23, 56, 1, 99, 44, 33, 77]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [1, 12, 21, 23, 33, 34, 44, 45, 56, 67, 77, 78, 89, 90, 99]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Large Dataset\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_partially_sorted(self):
    """Common case: Partially sorted list"""
    # Arrange
    input_data = [1, 2, 3, 9, 5, 6, 4, 8, 7]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Partially Sorted List\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_alternating_high_low(self):
    """Common case: Alternating high and low values"""
    # Arrange
    input_data = [10, 1, 9, 2, 8, 3, 7, 4]
    
    # Act
    result = selection_sort(input_data)
    
    # Assert
    expected = [1, 2, 3, 4, 7, 8, 9, 10]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Alternating High/Low Values\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )
