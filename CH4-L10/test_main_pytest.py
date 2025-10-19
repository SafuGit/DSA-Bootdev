"""
CH4-L10: Insertion Sort - Test Suite
Testing insertion sort algorithm implementation with pytest
"""

import pytest
from main import insertion_sort


# =============================================================================
# INSERTION SORT FUNCTION TESTS
# =============================================================================

class TestInsertionSort:
    """Test suite for the insertion_sort() function"""

    def test_empty_list(self):
        """Test sorting an empty list"""
        # Arrange
        nums = []
        
        # Act
        result = insertion_sort(nums)
        
        # Assert
        expected = []
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Empty List\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_single_element(self):
        """Test sorting a list with one element"""
        nums = [42]
        result = insertion_sort(nums)
        expected = [42]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Single Element\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_already_sorted(self):
        """Test sorting an already sorted list"""
        nums = [1, 2, 3, 4, 5]
        result = insertion_sort(nums)
        expected = [1, 2, 3, 4, 5]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Already Sorted List\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_reverse_sorted(self):
        """Test sorting a reverse sorted list (worst case)"""
        nums = [5, 4, 3, 2, 1]
        result = insertion_sort(nums)
        expected = [1, 2, 3, 4, 5]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Reverse Sorted List\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_unsorted_list(self):
        """Test sorting an unsorted list"""
        nums = [3, 1, 4, 1, 5, 9, 2, 6]
        result = insertion_sort(nums)
        expected = [1, 1, 2, 3, 4, 5, 6, 9]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Unsorted List\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_duplicates(self):
        """Test sorting a list with duplicate values"""
        nums = [3, 3, 1, 2, 2, 1]
        result = insertion_sort(nums)
        expected = [1, 1, 2, 2, 3, 3]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: List with Duplicates\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_negative_numbers(self):
        """Test sorting a list with negative numbers"""
        nums = [3, -1, 4, -5, 2, 0]
        result = insertion_sort(nums)
        expected = [-5, -1, 0, 2, 3, 4]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Negative Numbers\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_two_elements_unsorted(self):
        """Test sorting two unsorted elements"""
        nums = [2, 1]
        result = insertion_sort(nums)
        expected = [1, 2]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Two Unsorted Elements\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_two_elements_sorted(self):
        """Test sorting two already sorted elements"""
        nums = [1, 2]
        result = insertion_sort(nums)
        expected = [1, 2]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Two Sorted Elements\n"
            f"{'='*70}\n"
            f"📊 Input:    {nums}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_affiliate_deals_by_revenue(self):
        """Test sorting affiliate deals by revenue (real-world scenario)"""
        # Revenue values for affiliate deals
        nums = [1500, 300, 5000, 150, 2500, 800, 100, 3200]
        result = insertion_sort(nums)
        expected = [100, 150, 300, 800, 1500, 2500, 3200, 5000]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Affiliate Deals by Revenue\n"
            f"{'='*70}\n"
            f"📊 Input (revenue):    {nums}\n"
            f"✅ Expected (sorted):  {expected}\n"
            f"❌ Got:                {result}\n"
            f"{'='*70}\n"
        )

    def test_large_list_100_elements(self):
        """Test sorting a larger list with 100 elements"""
        import random
        nums = list(range(100, 0, -1))  # [100, 99, 98, ..., 2, 1]
        result = insertion_sort(nums)
        expected = list(range(1, 101))  # [1, 2, 3, ..., 99, 100]
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Large List (100 elements)\n"
            f"{'='*70}\n"
            f"📊 Input:    Reverse sorted list [100, 99, ..., 1]\n"
            f"✅ Expected: Sorted list [1, 2, ..., 100]\n"
            f"❌ Got:      Different result\n"
            f"{'='*70}\n"
        )


# =============================================================================
# PARAMETRIZED TESTS
# =============================================================================

class TestInsertionSortParametrized:
    """Parametrized tests for comprehensive coverage"""

    @pytest.mark.parametrize("nums,expected", [
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 2], [1, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 3, 2], [1, 2, 3]),
        ([5, 2, 8, 1, 9], [1, 2, 5, 8, 9]),
        ([0, 0, 0], [0, 0, 0]),
        ([-3, -1, -2], [-3, -2, -1]),
    ])
    def test_various_inputs(self, nums, expected):
        """Test insertion sort with various input combinations"""
        result = insertion_sort(nums)
        assert result == expected, (
            f"Failed for input {nums}: expected {expected}, got {result}"
        )


# =============================================================================
# RUN TESTS
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
