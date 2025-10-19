"""
CH4-L1: Sorting Algorithms - Test Suite
Testing vanity calculation and sorting functionality with pytest
"""

import pytest
from main import Influencer, vanity, vanity_sort


# =============================================================================
# VANITY CALCULATION TESTS
# =============================================================================

class TestVanityCalculation:
    """Test suite for the vanity() function"""

    def test_basic_vanity_calculation(self):
        """Test basic vanity calculation with typical values"""
        # Arrange
        influencer = Influencer(num_selfies=10, num_bio_links=2)
        
        # Act
        result = vanity(influencer)
        
        # Assert
        expected = 20
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Basic Vanity Calculation\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • Influencer(num_selfies=10, num_bio_links=2)\n"
            f"\n"
            f"📐 Formula:\n"
            f"   vanity = (num_bio_links × 5) + num_selfies\n"
            f"   vanity = (2 × 5) + 10\n"
            f"   vanity = 10 + 10\n"
            f"   vanity = 20\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_vanity_with_no_selfies(self):
        """Test vanity when influencer has no selfies"""
        influencer = Influencer(num_selfies=0, num_bio_links=3)
        result = vanity(influencer)
        expected = 15
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Vanity with No Selfies\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • num_selfies = 0\n"
            f"   • num_bio_links = 3\n"
            f"\n"
            f"📐 Calculation:\n"
            f"   vanity = (3 × 5) + 0 = 15\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_vanity_with_no_bio_links(self):
        """Test vanity when influencer has no bio links"""
        influencer = Influencer(num_selfies=7, num_bio_links=0)
        result = vanity(influencer)
        expected = 7
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Vanity with No Bio Links\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • num_selfies = 7\n"
            f"   • num_bio_links = 0\n"
            f"\n"
            f"📐 Calculation:\n"
            f"   vanity = (0 × 5) + 7 = 7\n"
            f"\n"
            f"💡 Note: With no bio links, vanity equals selfies\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_vanity_all_zeros_edge_case(self):
        """Test vanity with both values at zero (edge case)"""
        influencer = Influencer(num_selfies=0, num_bio_links=0)
        result = vanity(influencer)
        expected = 0
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Edge Case - All Zeros\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • num_selfies = 0\n"
            f"   • num_bio_links = 0\n"
            f"\n"
            f"📐 Calculation:\n"
            f"   vanity = (0 × 5) + 0 = 0\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_vanity_with_large_numbers(self):
        """Test vanity calculation with large values"""
        influencer = Influencer(num_selfies=100, num_bio_links=50)
        result = vanity(influencer)
        expected = 350
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Large Numbers Test\n"
            f"{'='*70}\n"
            f"📊 Input:\n"
            f"   • num_selfies = 100\n"
            f"   • num_bio_links = 50\n"
            f"\n"
            f"📐 Calculation:\n"
            f"   vanity = (50 × 5) + 100\n"
            f"   vanity = 250 + 100\n"
            f"   vanity = 350\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )

    def test_bio_links_weighted_more_than_selfies(self):
        """Verify that bio links contribute more to vanity than selfies"""
        inf1 = Influencer(num_selfies=10, num_bio_links=1)
        inf2 = Influencer(num_selfies=1, num_bio_links=2)
        
        vanity1 = vanity(inf1)
        vanity2 = vanity(inf2)
        
        assert vanity1 > vanity2, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Bio Links Weight Verification\n"
            f"{'='*70}\n"
            f"📊 Influencer 1:\n"
            f"   • num_selfies = 10, num_bio_links = 1\n"
            f"   • vanity = (1 × 5) + 10 = 15\n"
            f"\n"
            f"📊 Influencer 2:\n"
            f"   • num_selfies = 1, num_bio_links = 2\n"
            f"   • vanity = (2 × 5) + 1 = 11\n"
            f"\n"
            f"📝 Analysis:\n"
            f"   Even with 9 more selfies, Influencer 1 should have\n"
            f"   HIGHER vanity because the extra bio link is weighted 5×\n"
            f"\n"
            f"✅ Expected: vanity1 ({vanity1}) > vanity2 ({vanity2})\n"
            f"❌ Got:      This relationship doesn't hold!\n"
            f"{'='*70}\n"
        )

    @pytest.mark.parametrize("selfies,links,expected", [
        (10, 2, 20),   # Basic case
        (0, 3, 15),    # No selfies
        (7, 0, 7),     # No links
        (0, 0, 0),     # All zeros
        (100, 50, 350), # Large numbers
        (5, 1, 10),    # Small numbers
        (1, 1, 6),     # Equal values
    ])
    def test_vanity_parametrized(self, selfies, links, expected):
        """Test vanity with multiple input combinations"""
        influencer = Influencer(num_selfies=selfies, num_bio_links=links)
        result = vanity(influencer)
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ PARAMETRIZED TEST FAILED\n"
            f"{'='*70}\n"
            f"📊 Input:  selfies={selfies}, links={links}\n"
            f"📐 Formula: ({links} × 5) + {selfies}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )


# =============================================================================
# SORTING TESTS
# =============================================================================

class TestVanitySorting:
    """Test suite for the vanity_sort() function"""

    def test_basic_sorting_least_to_greatest(self):
        """Test basic sorting from least to greatest vanity"""
        # Arrange
        influencers = [
            Influencer(num_selfies=10, num_bio_links=2),  # vanity: 20
            Influencer(num_selfies=5, num_bio_links=1),   # vanity: 10
            Influencer(num_selfies=8, num_bio_links=3),   # vanity: 23
        ]
        
        # Act
        result = vanity_sort(influencers)
        
        # Assert
        vanities = [vanity(inf) for inf in result]
        expected_vanities = [10, 20, 23]
        
        assert vanities == expected_vanities, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Basic Sorting\n"
            f"{'='*70}\n"
            f"📊 Input (unsorted):\n"
            f"   [0] (selfies=10, links=2) → vanity = 20\n"
            f"   [1] (selfies=5,  links=1) → vanity = 10\n"
            f"   [2] (selfies=8,  links=3) → vanity = 23\n"
            f"\n"
            f"✅ Expected Output (sorted least to greatest):\n"
            f"   [0] vanity = 10  ⬆️ LEAST\n"
            f"   [1] vanity = 20\n"
            f"   [2] vanity = 23  ⬇️ GREATEST\n"
            f"\n"
            f"❌ Actual Output:\n"
            f"   {vanities}\n"
            f"{'='*70}\n"
        )

    def test_sorting_already_sorted_list(self):
        """Test sorting when list is already in correct order"""
        influencers = [
            Influencer(num_selfies=1, num_bio_links=0),   # vanity: 1
            Influencer(num_selfies=3, num_bio_links=1),   # vanity: 8
            Influencer(num_selfies=5, num_bio_links=2),   # vanity: 15
        ]
        
        result = vanity_sort(influencers)
        vanities = [vanity(inf) for inf in result]
        expected = [1, 8, 15]
        
        assert vanities == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Already Sorted List\n"
            f"{'='*70}\n"
            f"📊 Input (already sorted):\n"
            f"   {[vanity(inf) for inf in influencers]}\n"
            f"\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {vanities}\n"
            f"\n"
            f"💡 Note: List was already sorted, should remain unchanged\n"
            f"{'='*70}\n"
        )

    def test_sorting_reverse_order_list(self):
        """Test sorting when list is in reverse order (worst case)"""
        influencers = [
            Influencer(num_selfies=10, num_bio_links=5),  # vanity: 35
            Influencer(num_selfies=5, num_bio_links=2),   # vanity: 15
            Influencer(num_selfies=2, num_bio_links=1),   # vanity: 7
        ]
        
        result = vanity_sort(influencers)
        vanities = [vanity(inf) for inf in result]
        expected = [7, 15, 35]
        
        assert vanities == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Reverse Order Sorting\n"
            f"{'='*70}\n"
            f"📊 Input (reverse sorted):\n"
            f"   [35, 15, 7]  ⬇️ Greatest to least\n"
            f"\n"
            f"✅ Expected (reversed):\n"
            f"   [7, 15, 35]  ⬆️ Least to greatest\n"
            f"\n"
            f"❌ Got:\n"
            f"   {vanities}\n"
            f"{'='*70}\n"
        )

    def test_sorting_single_influencer(self):
        """Test sorting with a single element (edge case)"""
        influencers = [Influencer(num_selfies=5, num_bio_links=2)]
        result = vanity_sort(influencers)
        
        assert len(result) == 1, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Single Element\n"
            f"{'='*70}\n"
            f"📊 Input:  1 influencer\n"
            f"✅ Expected: 1 influencer returned\n"
            f"❌ Got:      {len(result)} influencer(s)\n"
            f"{'='*70}\n"
        )
        
        assert vanity(result[0]) == 15, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Single Element Vanity\n"
            f"{'='*70}\n"
            f"✅ Expected vanity: 15\n"
            f"❌ Got vanity:      {vanity(result[0])}\n"
            f"{'='*70}\n"
        )

    def test_sorting_empty_list(self):
        """Test sorting with an empty list (edge case)"""
        influencers = []
        result = vanity_sort(influencers)
        
        assert len(result) == 0, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Empty List\n"
            f"{'='*70}\n"
            f"📊 Input:  Empty list []\n"
            f"✅ Expected: Empty list [] returned\n"
            f"❌ Got:      List with {len(result)} elements\n"
            f"{'='*70}\n"
        )

    def test_sorting_equal_vanity_scores(self):
        """Test sorting when multiple influencers have equal vanity"""
        influencers = [
            Influencer(num_selfies=10, num_bio_links=1),  # vanity: 15
            Influencer(num_selfies=5, num_bio_links=2),   # vanity: 15
            Influencer(num_selfies=0, num_bio_links=3),   # vanity: 15
            Influencer(num_selfies=20, num_bio_links=0),  # vanity: 20
        ]
        
        result = vanity_sort(influencers)
        vanities = [vanity(inf) for inf in result]
        
        # First three should be 15, last should be 20
        assert vanities[:3] == [15, 15, 15] and vanities[3] == 20, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Equal Vanity Scores\n"
            f"{'='*70}\n"
            f"📊 Input vanities:\n"
            f"   [15, 15, 15, 20]  (3 influencers with same vanity)\n"
            f"\n"
            f"✅ Expected pattern:\n"
            f"   First 3 elements = 15\n"
            f"   Last element = 20\n"
            f"\n"
            f"❌ Got:\n"
            f"   {vanities}\n"
            f"\n"
            f"💡 Note: Influencers with equal vanity can be in any order\n"
            f"{'='*70}\n"
        )

    def test_sorting_many_influencers(self):
        """Test sorting with many influencers (performance check)"""
        influencers = [
            Influencer(num_selfies=i * 2, num_bio_links=i)
            for i in range(10, 0, -1)
        ]
        
        result = vanity_sort(influencers)
        vanities = [vanity(inf) for inf in result]
        
        # Check that list is properly sorted (ascending)
        is_sorted = all(vanities[i] <= vanities[i+1] for i in range(len(vanities)-1))
        
        assert is_sorted, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Many Influencers Sorting\n"
            f"{'='*70}\n"
            f"📊 Input:  10 influencers in reverse order\n"
            f"📊 Output: {vanities}\n"
            f"\n"
            f"✅ Expected: All elements in ascending order\n"
            f"❌ Got:      List is NOT properly sorted\n"
            f"\n"
            f"🔍 Check: Each vanity[i] should be ≤ vanity[i+1]\n"
            f"{'='*70}\n"
        )

    def test_sorting_returns_new_list(self):
        """Test that vanity_sort returns a new list (immutability)"""
        influencers = [
            Influencer(num_selfies=10, num_bio_links=2),
            Influencer(num_selfies=5, num_bio_links=1),
        ]
        original_first = influencers[0]
        original_first_vanity = vanity(influencers[0])
        
        result = vanity_sort(influencers)
        
        # Check original list is unchanged
        still_first = influencers[0] is original_first
        result_is_new = result is not influencers
        
        assert still_first and result_is_new, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Immutability Check\n"
            f"{'='*70}\n"
            f"📊 Original list first element: vanity = {vanity(influencers[0])}\n"
            f"📊 Original first vanity before:  {original_first_vanity}\n"
            f"\n"
            f"✅ Expected:\n"
            f"   • Original list unchanged: True\n"
            f"   • New list returned: True\n"
            f"\n"
            f"❌ Got:\n"
            f"   • Original list unchanged: {still_first}\n"
            f"   • New list returned: {result_is_new}\n"
            f"\n"
            f"💡 Note: sorted() should return a NEW list\n"
            f"{'='*70}\n"
        )


# =============================================================================
# INFLUENCER CLASS TESTS
# =============================================================================

class TestInfluencerClass:
    """Test suite for the Influencer class"""

    def test_influencer_initialization(self):
        """Test that Influencer class initializes correctly"""
        influencer = Influencer(num_selfies=5, num_bio_links=3)
        
        assert influencer.num_selfies == 5, (
            f"Expected num_selfies=5, got {influencer.num_selfies}"
        )
        assert influencer.num_bio_links == 3, (
            f"Expected num_bio_links=3, got {influencer.num_bio_links}"
        )

    def test_influencer_repr(self):
        """Test the string representation of Influencer"""
        influencer = Influencer(num_selfies=7, num_bio_links=2)
        result = repr(influencer)
        expected = "(7, 2)"
        
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Influencer __repr__\n"
            f"{'='*70}\n"
            f"✅ Expected: '{expected}'\n"
            f"❌ Got:      '{result}'\n"
            f"\n"
            f"💡 Format: (num_selfies, num_bio_links)\n"
            f"{'='*70}\n"
        )


# =============================================================================
# TEST CONFIGURATION
# =============================================================================

if __name__ == "__main__":
    pytest.main([
        __file__,
        "-v",                    # Verbose output
        "--tb=short",            # Shorter traceback format
        "--html=report.html",    # Generate HTML report
        "--self-contained-html", # Single HTML file
    ])
