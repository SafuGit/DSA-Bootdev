import pytest
from main import power_set


class TestPowerSet:
  """Test suite for the power_set() function - O(2^n) exponential algorithm"""

  def test_empty_set(self):
    """Edge case: Empty set returns power set containing only empty set"""
    # Arrange
    input_data = []
    
    # Act
    result = power_set(input_data)
    
    # Assert
    expected = [[]]
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected = sorted([sorted(inner) for inner in expected])
    assert sorted_result == sorted_expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Empty Set Power Set\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Power set of empty set is [[]] (set containing empty set)\n"
      f"{'='*70}\n"
    )

  def test_single_element(self):
    """Edge case: Single element set"""
    # Arrange
    input_data = [1]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    expected = [[], [1]]
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected = sorted([sorted(inner) for inner in expected])
    assert sorted_result == sorted_expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Single Element Power Set\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Power set has 2^1 = 2 subsets\n"
      f"{'='*70}\n"
    )

  def test_two_elements_bootdev(self):
    """Boot.dev test case: Two elements"""
    # Arrange
    input_data = [1, 2]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    expected = [[], [1], [2], [1, 2]]
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected = sorted([sorted(inner) for inner in expected])
    assert sorted_result == sorted_expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Two Elements Power Set (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Power set has 2^2 = 4 subsets\n"
      f"{'='*70}\n"
    )

  def test_three_elements_bootdev(self):
    """Boot.dev test case: Three elements"""
    # Arrange
    input_data = [1, 2, 3]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected = sorted([sorted(inner) for inner in expected])
    assert sorted_result == sorted_expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Three Elements Power Set (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Power set has 2^3 = 8 subsets\n"
      f"{'='*70}\n"
    )

  def test_four_elements_bootdev(self):
    """Boot.dev test case: Four elements - demonstrates exponential growth"""
    # Arrange
    input_data = [1, 2, 3, 4]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    expected = [
      [],
      [1],
      [2],
      [1, 2],
      [3],
      [1, 3],
      [2, 3],
      [1, 2, 3],
      [4],
      [1, 4],
      [2, 4],
      [1, 2, 4],
      [3, 4],
      [1, 3, 4],
      [2, 3, 4],
      [1, 2, 3, 4],
    ]
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected = sorted([sorted(inner) for inner in expected])
    assert sorted_result == sorted_expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Four Elements Power Set (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Power set has 2^4 = 16 subsets (doubled from n=3!)\n"
      f"{'='*70}\n"
    )

  def test_correct_size_two_elements(self):
    """Validation: Power set size should be 2^n"""
    # Arrange
    input_data = [5, 10]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    expected_size = 2 ** len(input_data)  # 2^2 = 4
    assert len(result) == expected_size, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Power Set Size Validation (n=2)\n"
      f"{'='*70}\n"
      f"📊 Input:        {input_data}\n"
      f"✅ Expected Size: {expected_size} subsets (2^{len(input_data)})\n"
      f"❌ Got Size:      {len(result)} subsets\n"
      f"{'='*70}\n"
    )

  def test_correct_size_three_elements(self):
    """Validation: Power set size should be 2^n"""
    # Arrange
    input_data = [7, 8, 9]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    expected_size = 2 ** len(input_data)  # 2^3 = 8
    assert len(result) == expected_size, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Power Set Size Validation (n=3)\n"
      f"{'='*70}\n"
      f"📊 Input:        {input_data}\n"
      f"✅ Expected Size: {expected_size} subsets (2^{len(input_data)})\n"
      f"❌ Got Size:      {len(result)} subsets\n"
      f"{'='*70}\n"
    )

  def test_contains_empty_subset(self):
    """Validation: Power set must always contain empty subset"""
    # Arrange
    input_data = [10, 20, 30]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    assert [] in result, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Empty Subset Must Be Present\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"❌ Result:   {result}\n"
      f"💡 Note:    Power set must always include [] (empty subset)\n"
      f"{'='*70}\n"
    )

  def test_contains_original_set(self):
    """Validation: Power set must contain the original set"""
    # Arrange
    input_data = [100, 200]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    sorted_result = [sorted(inner) for inner in result]
    assert sorted(input_data) in sorted_result, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Original Set Must Be Present\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"❌ Result:   {result}\n"
      f"💡 Note:    Power set must include the original set itself\n"
      f"{'='*70}\n"
    )

  def test_negative_numbers(self):
    """Edge case: Power set with negative numbers"""
    # Arrange
    input_data = [-1, -2]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    expected = [[], [-1], [-2], [-1, -2]]
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected = sorted([sorted(inner) for inner in expected])
    assert sorted_result == sorted_expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Power Set With Negative Numbers\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"{'='*70}\n"
    )

  def test_influencer_targeting_two(self):
    """Real-world: LockedIn ad targeting with 2 influencers"""
    # Arrange
    influencers = [101, 102]  # Influencer IDs
    
    # Act
    result = power_set(influencers)
    
    # Assert
    expected = [[], [101], [102], [101, 102]]
    sorted_result = sorted([sorted(inner) for inner in result])
    sorted_expected = sorted([sorted(inner) for inner in expected])
    assert sorted_result == sorted_expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Influencer Ad Targeting (2 influencers)\n"
      f"{'='*70}\n"
      f"📊 Influencers: {influencers}\n"
      f"✅ Expected:    {expected} targeting segments\n"
      f"❌ Got:         {result}\n"
      f"💡 Context:     2 influencers = 2^2 = 4 ad targeting combinations\n"
      f"{'='*70}\n"
    )

  def test_influencer_targeting_three(self):
    """Real-world: LockedIn ad targeting with 3 influencers"""
    # Arrange
    influencers = [201, 202, 203]  # Influencer IDs
    
    # Act
    result = power_set(influencers)
    
    # Assert
    expected_size = 8  # 2^3
    assert len(result) == expected_size, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Influencer Ad Targeting (3 influencers)\n"
      f"{'='*70}\n"
      f"📊 Influencers: {influencers}\n"
      f"✅ Expected:    {expected_size} targeting segments (2^3)\n"
      f"❌ Got:         {len(result)} segments\n"
      f"💡 Context:     Each new influencer DOUBLES targeting options!\n"
      f"{'='*70}\n"
    )

  def test_five_elements_performance_warning(self):
    """Performance test: 5 elements = 32 subsets (starting to get large)"""
    # Arrange
    input_data = [1, 2, 3, 4, 5]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    expected_size = 32  # 2^5
    assert len(result) == expected_size, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Five Elements Power Set\n"
      f"{'='*70}\n"
      f"📊 Input:        {input_data}\n"
      f"✅ Expected Size: {expected_size} subsets (2^5)\n"
      f"❌ Got Size:      {len(result)} subsets\n"
      f"⚠️  Warning:     Exponential growth is starting to show!\n"
      f"{'='*70}\n"
    )

  def test_exponential_growth_demonstration(self):
    """Educational: Demonstrates exponential growth rate"""
    # Arrange & Act
    sizes = {
      1: len(power_set([1])),
      2: len(power_set([1, 2])),
      3: len(power_set([1, 2, 3])),
      4: len(power_set([1, 2, 3, 4])),
    }
    
    # Assert
    expected_sizes = {1: 2, 2: 4, 3: 8, 4: 16}
    assert sizes == expected_sizes, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Exponential Growth Demonstration\n"
      f"{'='*70}\n"
      f"📊 Growth Pattern:\n"
      f"   n=1: {sizes.get(1, '?')} subsets (expected 2^1 = 2)\n"
      f"   n=2: {sizes.get(2, '?')} subsets (expected 2^2 = 4)\n"
      f"   n=3: {sizes.get(3, '?')} subsets (expected 2^3 = 8)\n"
      f"   n=4: {sizes.get(4, '?')} subsets (expected 2^4 = 16)\n"
      f"💡 Notice: Each element DOUBLES the power set size!\n"
      f"⚠️  Warning: n=25 would create 33+ million subsets!\n"
      f"            n=40 would take 34+ YEARS at 1ms per subset!\n"
      f"{'='*70}\n"
    )

  def test_no_duplicate_subsets(self):
    """Validation: Ensure no duplicate subsets in power set"""
    # Arrange
    input_data = [5, 6, 7]
    
    # Act
    result = power_set(input_data)
    
    # Assert
    sorted_result = [tuple(sorted(inner)) for inner in result]
    unique_subsets = set(sorted_result)
    assert len(sorted_result) == len(unique_subsets), (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Duplicate Subsets Detected\n"
      f"{'='*70}\n"
      f"📊 Input:           {input_data}\n"
      f"❌ Total Subsets:   {len(sorted_result)}\n"
      f"✅ Unique Subsets:  {len(unique_subsets)}\n"
      f"💡 Note:           Power set should not contain duplicates\n"
      f"{'='*70}\n"
    )
