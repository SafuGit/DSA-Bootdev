"""
CH4-L6: Merge Sort - Test Suite
Testing merge sort algorithm implementation with pytest
"""

import pytest
from main import merge_sort, merge


# =============================================================================
# MERGE FUNCTION TESTS
# =============================================================================

class TestMergeFunction:
    """Test suite for the merge() function"""

    def test_merge_two_single_element_lists(self):
        """Test merging two lists with one element each"""
        # Arrange
        first = [3]
        second = [1]
        
        # Act
        result = merge(first, second)
        
        # Assert
        expected = [1, 3]
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Merge Two Single Element Lists\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • first:  {first}\n"
            f"   • second: {second}\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_merge_lists_with_multiple_elements(self):
        """Test merging two sorted lists with multiple elements"""
        first = [1, 3, 5]
        second = [2, 4, 6]
        result = merge(first, second)
        expected = [1, 2, 3, 4, 5, 6]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Merge Multiple Elements\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • first:  {first}\n"
            f"   • second: {second}\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_merge_lists_different_lengths(self):
        """Test merging two sorted lists of different lengths"""
        first = [1, 5, 9]
        second = [2, 3, 4, 6, 7]
        result = merge(first, second)
        expected = [1, 2, 3, 4, 5, 6, 7, 9]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Merge Lists of Different Lengths\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • first:  {first} (length: {len(first)})\n"
            f"   • second: {second} (length: {len(second)})\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_merge_with_duplicates(self):
        """Test merging lists that contain duplicate values"""
        first = [1, 3, 3, 5]
        second = [2, 3, 4]
        result = merge(first, second)
        expected = [1, 2, 3, 3, 3, 4, 5]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Merge With Duplicates\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • first:  {first}\n"
            f"   • second: {second}\n"
            f"\n"
            f"💡 Note: When elements are equal, elements from 'first' should\n"
            f"   come before elements from 'second' (stable sort behavior)\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_merge_empty_first_list(self):
        """Test merging when first list is empty"""
        first = []
        second = [1, 2, 3]
        result = merge(first, second)
        expected = [1, 2, 3]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Merge Empty First List\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • first:  {first} (empty)\n"
            f"   • second: {second}\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_merge_empty_second_list(self):
        """Test merging when second list is empty"""
        first = [1, 2, 3]
        second = []
        result = merge(first, second)
        expected = [1, 2, 3]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Merge Empty Second List\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • first:  {first}\n"
            f"   • second: {second} (empty)\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_merge_both_empty_lists(self):
        """Test merging when both lists are empty"""
        first = []
        second = []
        result = merge(first, second)
        expected = []
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Merge Both Empty Lists\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • first:  {first} (empty)\n"
            f"   • second: {second} (empty)\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )


# =============================================================================
# MERGE SORT TESTS
# =============================================================================

class TestMergeSortFunction:
    """Test suite for the merge_sort() function"""

    def test_sort_empty_list(self):
        """Test sorting an empty list"""
        # Arrange
        nums = []
        
        # Act
        result = merge_sort(nums)
        
        # Assert
        expected = []
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Empty List\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_single_element(self):
        """Test sorting a list with one element"""
        nums = [42]
        result = merge_sort(nums)
        expected = [42]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Single Element\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"💡 Base case: A list with < 2 elements is already sorted\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_two_elements_unsorted(self):
        """Test sorting two unsorted elements"""
        nums = [5, 3]
        result = merge_sort(nums)
        expected = [3, 5]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Two Unsorted Elements\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_already_sorted_list(self):
        """Test sorting a list that's already sorted"""
        nums = [1, 2, 3, 4, 5]
        result = merge_sort(nums)
        expected = [1, 2, 3, 4, 5]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Already Sorted List\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"💡 An already sorted list should remain sorted\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_reverse_sorted_list(self):
        """Test sorting a list in reverse order"""
        nums = [5, 4, 3, 2, 1]
        result = merge_sort(nums)
        expected = [1, 2, 3, 4, 5]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Reverse Sorted List\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_unsorted_list(self):
        """Test sorting a typical unsorted list"""
        nums = [3, 7, 1, 9, 2, 5]
        result = merge_sort(nums)
        expected = [1, 2, 3, 5, 7, 9]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Unsorted List\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_list_with_duplicates(self):
        """Test sorting a list with duplicate values"""
        nums = [4, 2, 7, 2, 9, 4, 1]
        result = merge_sort(nums)
        expected = [1, 2, 2, 4, 4, 7, 9]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort List With Duplicates\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"💡 Duplicate values should all appear in the sorted result\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_all_same_elements(self):
        """Test sorting a list where all elements are the same"""
        nums = [5, 5, 5, 5, 5]
        result = merge_sort(nums)
        expected = [5, 5, 5, 5, 5]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort All Same Elements\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_negative_numbers(self):
        """Test sorting a list with negative numbers"""
        nums = [3, -1, 4, -5, 2, 0]
        result = merge_sort(nums)
        expected = [-5, -1, 0, 2, 3, 4]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Negative Numbers\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"💡 Negative numbers should be sorted correctly\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_large_list(self):
        """Test sorting a larger list (1000+ elements as mentioned in assignment)"""
        nums = [42, 17, 93, 8, 55, 31, 76, 2, 64, 19, 88, 45, 11, 99, 3, 
                71, 26, 58, 14, 82, 37, 69, 5, 91, 48, 23, 77, 34, 60, 16]
        result = merge_sort(nums)
        expected = sorted(nums)  # Use Python's built-in sort for validation
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Large List\n"
            f"{'='*70}\n"
            f"📊 Input: {nums}\n"
            f"\n"
            f"💡 Merge sort should efficiently handle larger lists\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )


# =============================================================================
# INFLUENCER USE CASE TESTS (LockedIn scenario)
# =============================================================================

class TestInfluencerUseCase:
    """Test merge sort with the LockedIn influencer scenario"""

    def test_sort_follower_counts_small(self):
        """Test sorting a small list of follower counts"""
        # Simulating follower counts
        follower_counts = [1500, 300, 2500, 100, 1800]
        result = merge_sort(follower_counts)
        expected = [100, 300, 1500, 1800, 2500]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Follower Counts (Small)\n"
            f"{'='*70}\n"
            f"📊 Scenario: LockedIn influencer sorting followers\n"
            f"\n"
            f"📊 Input follower counts: {follower_counts}\n"
            f"\n"
            f"✅ Expected (ascending): {expected}\n"
            f"❌ Got:                  {result}\n"
            f"{'='*70}\n"
        )

    def test_sort_follower_counts_over_1000(self):
        """Test that merge sort works efficiently with >1000 followers"""
        # Generate a list with more than 1000 elements
        import random
        random.seed(42)  # For reproducible tests
        follower_counts = [random.randint(1, 10000) for _ in range(1500)]
        
        result = merge_sort(follower_counts)
        expected = sorted(follower_counts)
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Sort Follower Counts (>1000)\n"
            f"{'='*70}\n"
            f"📊 Scenario: LockedIn influencer with 1500 followers\n"
            f"📊 This tests the performance improvement over Bubble Sort\n"
            f"\n"
            f"💡 List size: {len(follower_counts)} followers\n"
            f"💡 Merge sort should handle this much faster than Bubble Sort\n"
            f"\n"
            f"✅ First 10 expected: {expected[:10]}\n"
            f"❌ First 10 got:      {result[:10]}\n"
            f"\n"
            f"✅ Last 10 expected:  {expected[-10:]}\n"
            f"❌ Last 10 got:       {result[-10:]}\n"
            f"{'='*70}\n"
        )


# =============================================================================
# PARAMETRIZED TESTS
# =============================================================================

class TestMergeSortParametrized:
    """Parametrized tests for comprehensive coverage"""

    @pytest.mark.parametrize("input_list,expected", [
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([0], [0]),
        ([-1, -2, -3], [-3, -2, -1]),
    ])
    def test_various_inputs(self, input_list, expected):
        """Test merge sort with various input scenarios"""
        result = merge_sort(input_list)
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
# RUN TESTS
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
