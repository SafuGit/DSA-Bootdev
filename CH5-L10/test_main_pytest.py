import pytest
from main import exponential_growth


class TestExponentialGrowth:
  """Test suite for the exponential_growth() function - Simulating follower growth"""

  def test_zero_initial_followers(self):
    """Edge case: Zero initial followers (no growth possible)"""
    # Arrange
    n = 0
    factor = 2
    days = 2
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [0, 0, 0]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Zero Initial Followers\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Zero followers multiplied by any factor stays zero\n"
      f"{'='*70}\n"
    )

  def test_zero_days(self):
    """Edge case: Zero days of growth (only initial count)"""
    # Arrange
    n = 10
    factor = 5
    days = 0
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [10]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Zero Days Growth\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Zero days means only the initial follower count\n"
      f"{'='*70}\n"
    )

  def test_growth_factor_one(self):
    """Edge case: Growth factor of 1 (no growth, stays same)"""
    # Arrange
    n = 1
    factor = 1
    days = 5
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [1, 1, 1, 1, 1, 1]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Growth Factor of 1\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Factor of 1 means no growth (1 * 1 = 1)\n"
      f"{'='*70}\n"
    )

  def test_basic_example_bootdev(self):
    """Boot.dev example: Small influencer doubling followers"""
    # Arrange
    n = 10
    factor = 2
    days = 4
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [10, 20, 40, 80, 160]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Basic Doubling Example (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Sequence: 10 → 20 → 40 → 80 → 160 (doubles each day)\n"
      f"{'='*70}\n"
    )

  def test_larger_doubling_bootdev(self):
    """Boot.dev test case: Larger starting point with doubling"""
    # Arrange
    n = 20
    factor = 2
    days = 6
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [20, 40, 80, 160, 320, 640, 1280]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Larger Doubling Sequence (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Sequence: 20 → 40 → 80 → 160 → 320 → 640 → 1280\n"
      f"{'='*70}\n"
    )

  def test_tripling_growth_bootdev(self):
    """Boot.dev test case: Tripling followers each day"""
    # Arrange
    n = 30
    factor = 3
    days = 3
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [30, 90, 270, 810]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Tripling Growth (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Sequence: 30 → 90 → 270 → 810 (triples each day)\n"
      f"{'='*70}\n"
    )

  def test_extreme_growth_10x_bootdev(self):
    """Boot.dev test case: Extreme 10x growth over 10 days"""
    # Arrange
    n = 40
    factor = 10
    days = 10
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [
      40,
      400,
      4000,
      40000,
      400000,
      4000000,
      40000000,
      400000000,
      4000000000,
      40000000000,
      400000000000,
    ]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Extreme 10x Growth (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected[:3]}... (11 values total)\n"
      f"❌ Got:      {result[:3] if len(result) >= 3 else result}...\n"
      f"💡 Note:    Demonstrates explosive exponential growth\n"
      f"            Final value: 400,000,000,000 followers!\n"
      f"{'='*70}\n"
    )

  def test_sequence_length_consistency(self):
    """Verify sequence length: should be days + 1 (including initial)"""
    # Arrange
    test_cases = [
      (10, 2, 0, 1),   # 0 days = 1 value (initial)
      (10, 2, 1, 2),   # 1 day = 2 values
      (10, 2, 5, 6),   # 5 days = 6 values
      (10, 2, 10, 11), # 10 days = 11 values
    ]
    
    # Act & Assert
    for n, factor, days, expected_length in test_cases:
      result = exponential_growth(n, factor, days)
      assert len(result) == expected_length, (
        f"\n{'='*70}\n"
        f"❌ TEST FAILED: Sequence Length Consistency\n"
        f"{'='*70}\n"
        f"📊 Input:    n={n}, factor={factor}, days={days}\n"
        f"✅ Expected: {expected_length} values (days + 1)\n"
        f"❌ Got:      {len(result)} values\n"
        f"💡 Note:    Sequence must include initial count plus all growth days\n"
        f"{'='*70}\n"
      )

  def test_growth_factor_2(self):
    """Common case: Growth factor of 2 (doubling)"""
    # Arrange
    n = 100
    factor = 2
    days = 3
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [100, 200, 400, 800]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Doubling Growth Factor\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Sequence: 100 → 200 → 400 → 800\n"
      f"{'='*70}\n"
    )

  def test_growth_factor_5(self):
    """Common case: Growth factor of 5 (quintupling)"""
    # Arrange
    n = 5
    factor = 5
    days = 3
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [5, 25, 125, 625]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Quintupling Growth Factor\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Sequence: 5 → 25 → 125 → 625 (5^1, 5^2, 5^3, 5^4)\n"
      f"{'='*70}\n"
    )

  def test_single_day_growth(self):
    """Edge case: Only one day of growth"""
    # Arrange
    n = 50
    factor = 3
    days = 1
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [50, 150]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Single Day Growth\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    One day means initial count + one multiplication\n"
      f"{'='*70}\n"
    )

  def test_first_value_always_initial(self):
    """Verify first value in sequence is always the initial count"""
    # Arrange
    test_cases = [
      (10, 2, 3),
      (25, 5, 2),
      (100, 10, 1),
      (1, 1, 5),
    ]
    
    # Act & Assert
    for n, factor, days in test_cases:
      result = exponential_growth(n, factor, days)
      assert result[0] == n, (
        f"\n{'='*70}\n"
        f"❌ TEST FAILED: First Value Must Equal Initial Count\n"
        f"{'='*70}\n"
        f"📊 Input:    n={n}, factor={factor}, days={days}\n"
        f"✅ Expected: result[0] = {n}\n"
        f"❌ Got:      result[0] = {result[0] if result else 'empty list'}\n"
        f"💡 Note:    The sequence always starts with the initial follower count\n"
        f"{'='*70}\n"
      )

  def test_exponential_calculation_accuracy(self):
    """Verify each value is previous value multiplied by factor"""
    # Arrange
    n = 7
    factor = 3
    days = 4
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [7, 21, 63, 189, 567]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Exponential Calculation Accuracy\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Formula:  Each value = previous_value * factor\n"
      f"            7 → 7*3=21 → 21*3=63 → 63*3=189 → 189*3=567\n"
      f"{'='*70}\n"
    )
    
    # Additional check: verify multiplication relationship
    if len(result) == len(expected):
      for i in range(1, len(result)):
        assert result[i] == result[i-1] * factor, (
          f"\n{'='*70}\n"
          f"❌ TEST FAILED: Multiplication Relationship Broken\n"
          f"{'='*70}\n"
          f"📊 Position:  Day {i}\n"
          f"✅ Expected:  result[{i}] = result[{i-1}] * {factor} = {result[i-1] * factor}\n"
          f"❌ Got:       result[{i}] = {result[i]}\n"
          f"{'='*70}\n"
        )

  def test_large_growth_factor(self):
    """Stress test: Very large growth factor"""
    # Arrange
    n = 2
    factor = 10
    days = 5
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert
    expected = [2, 20, 200, 2000, 20000, 200000]
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Large Growth Factor\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Growth factor of 10 causes rapid exponential increase\n"
      f"{'='*70}\n"
    )

  def test_realistic_viral_scenario(self):
    """Real-world scenario: Viral influencer with 2.5x daily growth"""
    # Arrange
    n = 1000  # Starting with 1K followers
    factor = 2.5
    days = 7  # One week of growth
    
    # Act
    result = exponential_growth(n, factor, days)
    
    # Assert - manually calculating expected values
    expected = [
      1000,
      2500,      # Day 1: 1000 * 2.5
      6250,      # Day 2: 2500 * 2.5
      15625,     # Day 3: 6250 * 2.5
      39062.5,   # Day 4: 15625 * 2.5
      97656.25,  # Day 5: 39062.5 * 2.5
      244140.625,    # Day 6: 97656.25 * 2.5
      610351.5625,   # Day 7: 244140.625 * 2.5
    ]
    
    # Allow for floating point comparison
    assert len(result) == len(expected), (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Realistic Viral Scenario - Length Mismatch\n"
      f"{'='*70}\n"
      f"📊 Input:    n={n}, factor={factor}, days={days}\n"
      f"✅ Expected: {len(expected)} values\n"
      f"❌ Got:      {len(result)} values\n"
      f"{'='*70}\n"
    )
    
    for i in range(len(expected)):
      assert abs(result[i] - expected[i]) < 0.001, (
        f"\n{'='*70}\n"
        f"❌ TEST FAILED: Realistic Viral Scenario - Value Mismatch\n"
        f"{'='*70}\n"
        f"📊 Position:  Day {i}\n"
        f"✅ Expected:  {expected[i]}\n"
        f"❌ Got:       {result[i]}\n"
        f"💡 Note:     1000 followers growing 2.5x daily for a week\n"
        f"{'='*70}\n"
      )
