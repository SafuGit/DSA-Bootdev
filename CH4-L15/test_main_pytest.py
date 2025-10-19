import pytest
from main import quick_sort, partition


class TestQuickSort:
  """Test suite for the quick_sort() function"""
  
  def test_empty_list(self):
    """Quick sort should handle empty lists gracefully"""
    # Arrange
    nums = []
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = []
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Empty List\n"
      f"{'='*70}\n"
      f"📊 Input:    {[]}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_single_element(self):
    """Quick sort should handle single-element lists"""
    # Arrange
    nums = [42]
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [42]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Single Element\n"
      f"{'='*70}\n"
      f"📊 Input:    {[42]}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_two_elements_unsorted(self):
    """Quick sort should handle two unsorted elements"""
    # Arrange
    nums = [5, 2]
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [2, 5]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Two Unsorted Elements\n"
      f"{'='*70}\n"
      f"📊 Input:    {[5, 2]}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_two_elements_sorted(self):
    """Quick sort should handle two already sorted elements"""
    # Arrange
    nums = [2, 5]
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [2, 5]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Two Sorted Elements\n"
      f"{'='*70}\n"
      f"📊 Input:    {[2, 5]}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_already_sorted_list(self):
    """Quick sort should handle already sorted lists efficiently"""
    # Arrange
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Already Sorted List\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_reverse_sorted_list(self):
    """Quick sort should handle reverse sorted lists (worst case)"""
    # Arrange
    nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Reverse Sorted List\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_list_with_duplicates(self):
    """Quick sort should handle lists with duplicate values"""
    # Arrange
    nums = [5, 2, 8, 2, 9, 1, 5, 5]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [1, 2, 2, 5, 5, 5, 8, 9]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: List With Duplicates\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_all_identical_elements(self):
    """Quick sort should handle lists where all elements are identical"""
    # Arrange
    nums = [7, 7, 7, 7, 7]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [7, 7, 7, 7, 7]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: All Identical Elements\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_random_order_small(self):
    """Quick sort should handle small random lists"""
    # Arrange
    nums = [3, 7, 1, 4, 2]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [1, 2, 3, 4, 7]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Random Order Small\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_random_order_medium(self):
    """Quick sort should handle medium-sized random lists"""
    # Arrange
    nums = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 13, 5, 77]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [5, 11, 12, 13, 22, 25, 34, 45, 50, 64, 77, 88, 90]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Random Order Medium\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_negative_numbers(self):
    """Quick sort should handle lists with negative numbers"""
    # Arrange
    nums = [3, -1, 4, -5, 2, 0, -3]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [-5, -3, -1, 0, 2, 3, 4]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Negative Numbers\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_mixed_positive_negative(self):
    """Quick sort should handle mixed positive and negative numbers"""
    # Arrange
    nums = [10, -5, 20, -10, 5, 0, 15, -15]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [-15, -10, -5, 0, 5, 10, 15, 20]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Mixed Positive/Negative\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_influencer_follower_counts(self):
    """Quick sort should handle realistic LockedIn influencer follower counts"""
    # Arrange
    nums = [15000, 2500, 98000, 45000, 12000, 67000, 3400, 125000]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [2500, 3400, 12000, 15000, 45000, 67000, 98000, 125000]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Influencer Follower Counts\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"💡 Context:  Sorting LockedIn influencers by follower count\n"
      f"{'='*70}\n"
    )
  
  def test_influencer_revenue_amounts(self):
    """Quick sort should handle LockedIn influencer revenue amounts"""
    # Arrange
    nums = [5000, 12000, 3500, 25000, 8000, 15000, 2000, 50000]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [2000, 3500, 5000, 8000, 12000, 15000, 25000, 50000]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Influencer Revenue Amounts\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"💡 Context:  Sorting LockedIn influencers by revenue\n"
      f"{'='*70}\n"
    )
  
  def test_large_dataset(self):
    """Quick sort should efficiently handle large datasets"""
    # Arrange
    nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 19, 37, 25, 11, 72, 58, 94, 31, 50]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    quick_sort(nums, low, high)
    
    # Assert
    expected = [0, 1, 2, 4, 5, 6, 11, 19, 25, 31, 37, 44, 50, 58, 63, 72, 87, 94, 99, 283]
    assert nums == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Large Dataset\n"
      f"{'='*70}\n"
      f"📊 Input:    {original_input}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {nums}\n"
      f"{'='*70}\n"
    )


class TestPartition:
  """Test suite for the partition() function"""
  
  def test_partition_simple_case(self):
    """Partition should correctly partition a simple list"""
    # Arrange
    nums = [3, 1, 4, 1, 5]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    pivot_index = partition(nums, low, high)
    
    # Assert - elements before pivot should be <= pivot, after should be >= pivot
    pivot_value = nums[pivot_index]
    left_side = nums[:pivot_index]
    right_side = nums[pivot_index + 1:]
    
    left_valid = all(x <= pivot_value for x in left_side)
    right_valid = all(x >= pivot_value for x in right_side)
    
    assert left_valid and right_valid, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Partition Simple Case\n"
      f"{'='*70}\n"
      f"📊 Input:        {original_input}\n"
      f"📍 Pivot Index:  {pivot_index}\n"
      f"🎯 Pivot Value:  {pivot_value}\n"
      f"⬅️  Left Side:    {left_side}\n"
      f"➡️  Right Side:   {right_side}\n"
      f"❌ After:        {nums}\n"
      f"💡 Issue:        {'Left side has values > pivot' if not left_valid else 'Right side has values < pivot'}\n"
      f"{'='*70}\n"
    )
  
  def test_partition_all_less_than_pivot(self):
    """Partition should handle when all elements are less than pivot"""
    # Arrange
    nums = [1, 2, 3, 4, 10]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    pivot_index = partition(nums, low, high)
    
    # Assert
    pivot_value = nums[pivot_index]
    assert pivot_index == high, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: All Less Than Pivot\n"
      f"{'='*70}\n"
      f"📊 Input:        {original_input}\n"
      f"📍 Pivot Index:  {pivot_index} (expected {high})\n"
      f"🎯 Pivot Value:  {pivot_value}\n"
      f"❌ After:        {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_partition_all_greater_than_pivot(self):
    """Partition should handle when all elements are greater than pivot"""
    # Arrange
    nums = [10, 9, 8, 7, 1]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    pivot_index = partition(nums, low, high)
    
    # Assert
    pivot_value = nums[pivot_index]
    assert pivot_index == low, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: All Greater Than Pivot\n"
      f"{'='*70}\n"
      f"📊 Input:        {original_input}\n"
      f"📍 Pivot Index:  {pivot_index} (expected {low})\n"
      f"🎯 Pivot Value:  {pivot_value}\n"
      f"❌ After:        {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_partition_with_duplicates(self):
    """Partition should correctly handle duplicate values"""
    # Arrange
    nums = [3, 5, 3, 7, 3]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    pivot_index = partition(nums, low, high)
    
    # Assert
    pivot_value = nums[pivot_index]
    left_side = nums[:pivot_index]
    right_side = nums[pivot_index + 1:]
    
    left_valid = all(x <= pivot_value for x in left_side)
    right_valid = all(x >= pivot_value for x in right_side)
    
    assert left_valid and right_valid, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Partition With Duplicates\n"
      f"{'='*70}\n"
      f"📊 Input:        {original_input}\n"
      f"📍 Pivot Index:  {pivot_index}\n"
      f"🎯 Pivot Value:  {pivot_value}\n"
      f"⬅️  Left Side:    {left_side}\n"
      f"➡️  Right Side:   {right_side}\n"
      f"❌ After:        {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_partition_two_elements(self):
    """Partition should handle two-element lists"""
    # Arrange
    nums = [5, 2]
    original_input = nums.copy()
    low = 0
    high = len(nums) - 1
    
    # Act
    pivot_index = partition(nums, low, high)
    
    # Assert
    pivot_value = nums[pivot_index]
    left_side = nums[:pivot_index]
    right_side = nums[pivot_index + 1:]
    
    left_valid = all(x <= pivot_value for x in left_side)
    right_valid = all(x >= pivot_value for x in right_side)
    
    assert left_valid and right_valid and nums[0] <= nums[1], (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Partition Two Elements\n"
      f"{'='*70}\n"
      f"📊 Input:        {original_input}\n"
      f"📍 Pivot Index:  {pivot_index}\n"
      f"🎯 Pivot Value:  {pivot_value}\n"
      f"❌ After:        {nums}\n"
      f"{'='*70}\n"
    )
  
  def test_partition_subrange(self):
    """Partition should correctly partition a subrange of a list"""
    # Arrange
    nums = [1, 5, 3, 7, 2, 9]
    original_input = nums.copy()
    low = 1  # Start from index 1
    high = 4  # End at index 4
    
    # Act
    pivot_index = partition(nums, low, high)
    
    # Assert - only check the subrange
    pivot_value = nums[pivot_index]
    subrange = nums[low:high + 1]
    left_side = subrange[:pivot_index - low]
    right_side = subrange[pivot_index - low + 1:]
    
    left_valid = all(x <= pivot_value for x in left_side)
    right_valid = all(x >= pivot_value for x in right_side)
    
    assert left_valid and right_valid and low <= pivot_index <= high, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Partition Subrange\n"
      f"{'='*70}\n"
      f"📊 Original:     {original_input}\n"
      f"🎯 Range:        [{low}:{high}] = {original_input[low:high+1]}\n"
      f"📍 Pivot Index:  {pivot_index}\n"
      f"🎯 Pivot Value:  {pivot_value}\n"
      f"⬅️  Left Side:    {left_side}\n"
      f"➡️  Right Side:   {right_side}\n"
      f"❌ After:        {nums}\n"
      f"{'='*70}\n"
    )
