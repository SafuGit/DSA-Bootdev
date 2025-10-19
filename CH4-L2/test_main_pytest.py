"""
CH4-L2: Bubble Sort Algorithm - Test Suite
Testing bubble sort implementation with pytest
"""

import pytest
from main import bubble_sort


# =============================================================================
# BUBBLE SORT TESTS
# =============================================================================

class TestBubbleSort:
    """Test suite for the bubble_sort() function"""

    def test_basic_sorting(self):
        """Test basic bubble sort with unsorted list"""
        # Arrange
        nums = [5, 2, 8, 1, 9]
        
        # Act
        result = bubble_sort(nums)
        
        # Assert
        expected = [1, 2, 5, 8, 9]
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Basic Bubble Sort\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"\n"
            f"💡 The bubble sort should arrange numbers in ascending order\n"
            f"{'='*70}\n"
        )

    def test_already_sorted_list(self):
        """Test bubble sort with already sorted list"""
        nums = [1, 2, 3, 4, 5]
        result = bubble_sort(nums)
        expected = [1, 2, 3, 4, 5]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Already Sorted List\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"\n"
            f"💡 An already sorted list should remain unchanged\n"
            f"{'='*70}\n"
        )

    def test_reverse_sorted_list(self):
        """Test bubble sort with reverse sorted list (worst case)"""
        nums = [9, 7, 5, 3, 1]
        result = bubble_sort(nums)
        expected = [1, 3, 5, 7, 9]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Reverse Sorted List\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"\n"
            f"💡 This is the worst case for bubble sort - requires maximum swaps\n"
            f"{'='*70}\n"
        )

    def test_list_with_duplicates(self):
        """Test bubble sort with duplicate values"""
        nums = [5, 2, 8, 2, 9, 5, 1]
        result = bubble_sort(nums)
        expected = [1, 2, 2, 5, 5, 8, 9]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: List with Duplicates\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"\n"
            f"💡 Duplicate values should maintain their relative positions\n"
            f"{'='*70}\n"
        )

    def test_single_element_list(self):
        """Test bubble sort with single element (edge case)"""
        nums = [42]
        result = bubble_sort(nums)
        expected = [42]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Single Element List\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"\n"
            f"💡 A single element list is already sorted\n"
            f"{'='*70}\n"
        )

    def test_empty_list(self):
        """Test bubble sort with empty list (edge case)"""
        nums = []
        result = bubble_sort(nums)
        expected = []
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Empty List\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"\n"
            f"💡 An empty list should remain empty\n"
            f"{'='*70}\n"
        )

    def test_two_elements_sorted(self):
        """Test bubble sort with two elements already sorted"""
        nums = [1, 2]
        result = bubble_sort(nums)
        expected = [1, 2]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Two Elements (Sorted)\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_two_elements_unsorted(self):
        """Test bubble sort with two elements needing swap"""
        nums = [2, 1]
        result = bubble_sort(nums)
        expected = [1, 2]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Two Elements (Unsorted)\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"\n"
            f"💡 The algorithm should swap these two elements\n"
            f"{'='*70}\n"
        )

    def test_all_identical_elements(self):
        """Test bubble sort with all identical elements"""
        nums = [7, 7, 7, 7, 7]
        result = bubble_sort(nums)
        expected = [7, 7, 7, 7, 7]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: All Identical Elements\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"\n"
            f"💡 When all elements are the same, no swaps should occur\n"
            f"{'='*70}\n"
        )

    def test_negative_numbers(self):
        """Test bubble sort with negative numbers"""
        nums = [3, -1, 4, -5, 2, 0]
        result = bubble_sort(nums)
        expected = [-5, -1, 0, 2, 3, 4]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Negative Numbers\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"\n"
            f"💡 Algorithm should handle negative numbers correctly\n"
            f"{'='*70}\n"
        )

    def test_large_numbers(self):
        """Test bubble sort with large numbers"""
        nums = [1000, 500, 1500, 250, 2000]
        result = bubble_sort(nums)
        expected = [250, 500, 1000, 1500, 2000]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Large Numbers\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_follower_count_scenario(self):
        """Test bubble sort with realistic follower counts"""
        # Simulating the avocado toast influencer scenario
        follower_counts = [15420, 2341, 87654, 1234, 45678]
        result = bubble_sort(follower_counts)
        expected = [1234, 2341, 15420, 45678, 87654]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Follower Count Scenario\n"
            f"{'='*70}\n"
            f"📊 Unsorted Follower Counts: {follower_counts}\n"
            f"✅ Expected Sorted Order:    {expected}\n"
            f"❌ Got:                      {result}\n"
            f"\n"
            f"💡 This simulates sorting influencers by follower count\n"
            f"{'='*70}\n"
        )


# =============================================================================
# PARAMETRIZED TESTS
# =============================================================================

class TestBubbleSortParametrized:
    """Parametrized tests for bubble_sort() function"""

    @pytest.mark.parametrize("input_list,expected", [
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([5, 3, 8, 1, 9, 2], [1, 2, 3, 5, 8, 9]),
        ([0, -1, 1], [-1, 0, 1]),
        ([10, 10, 10], [10, 10, 10]),
    ])
    def test_various_inputs(self, input_list, expected):
        """Test bubble sort with various inputs using parametrization"""
        result = bubble_sort(input_list)
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ PARAMETRIZED TEST FAILED\n"
            f"{'='*70}\n"
            f"📊 Input:    {input_list}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )


# =============================================================================
# BUBBLE SORT BEHAVIOR TESTS
# =============================================================================

class TestBubbleSortBehavior:
    """Test specific bubble sort behavior and requirements"""

    def test_returns_sorted_list(self):
        """Test that bubble sort returns a list (not modifying in place)"""
        nums = [3, 1, 2]
        result = bubble_sort(nums)
        
        assert isinstance(result, list), (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Return Type Check\n"
            f"{'='*70}\n"
            f"❌ bubble_sort() should return a list\n"
            f"   Got type: {type(result)}\n"
            f"{'='*70}\n"
        )

    def test_sorting_stability(self):
        """Test that bubble sort correctly sorts without losing elements"""
        nums = [5, 2, 8, 1, 9, 3]
        result = bubble_sort(nums)
        
        # Check length preservation
        assert len(result) == len(nums), (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Length Preservation\n"
            f"{'='*70}\n"
            f"❌ Sorted list should have same length as input\n"
            f"   Input length:  {len(nums)}\n"
            f"   Result length: {len(result)}\n"
            f"{'='*70}\n"
        )
        
        # Check all elements present
        assert sorted(result) == sorted(nums), (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Element Preservation\n"
            f"{'='*70}\n"
            f"❌ Result should contain all original elements\n"
            f"   Input:  {nums}\n"
            f"   Result: {result}\n"
            f"{'='*70}\n"
        )

    def test_ascending_order(self):
        """Test that result is in ascending order"""
        nums = [8, 3, 9, 1, 5]
        result = bubble_sort(nums)
        
        # Check if sorted in ascending order
        is_sorted = all(result[i] <= result[i+1] for i in range(len(result)-1))
        
        assert is_sorted, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Ascending Order Check\n"
            f"{'='*70}\n"
            f"❌ Result is not in ascending order\n"
            f"   Input:  {nums}\n"
            f"   Result: {result}\n"
            f"\n"
            f"💡 Each element should be ≤ the next element\n"
            f"{'='*70}\n"
        )


# =============================================================================
# EDGE CASE TESTS
# =============================================================================

class TestBubbleSortEdgeCases:
    """Edge case tests for bubble_sort() function"""

    @pytest.mark.edge_case
    def test_zero_in_list(self):
        """Test bubble sort with zero in the list"""
        nums = [3, 0, 2, 0, 1]
        result = bubble_sort(nums)
        expected = [0, 0, 1, 2, 3]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Zero in List\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    @pytest.mark.edge_case
    def test_mixed_positive_negative_zero(self):
        """Test with mix of positive, negative, and zero"""
        nums = [-5, 0, 5, -3, 3, 0]
        result = bubble_sort(nums)
        expected = [-5, -3, 0, 0, 3, 5]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Mixed Positive/Negative/Zero\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    @pytest.mark.edge_case
    def test_long_list(self):
        """Test bubble sort with a longer list"""
        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        result = bubble_sort(nums)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Long List (11 elements)\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
