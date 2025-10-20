import pytest
from main import last_work_experience


class TestLastWorkExperience:
  """Test suite for the last_work_experience() function - O(1) last element access"""

  def test_empty_list_bootdev(self):
    """Boot.dev test case: Empty work history returns None"""
    # Arrange
    input_data = []
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = None
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Empty Work History (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Empty list should return None (no work experience)\n"
      f"{'='*70}\n"
    )

  def test_single_job_bootdev(self):
    """Boot.dev test case: Single job in history"""
    # Arrange
    input_data = ["CEO"]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "CEO"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Single Job (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Single job should return that job as the last (and only) one\n"
      f"{'='*70}\n"
    )

  def test_three_jobs_bootdev(self):
    """Boot.dev test case: Three jobs in chronological order"""
    # Arrange
    input_data = ["Software Engineer", "Data Analyst", "Project Manager"]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "Project Manager"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Three Jobs (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should return last element (most recent job)\n"
      f"{'='*70}\n"
    )

  def test_two_jobs_bootdev(self):
    """Boot.dev test case: Two jobs - intern to junior"""
    # Arrange
    input_data = ["Intern", "Junior Developer"]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "Junior Developer"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Two Jobs (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should return second job (most recent)\n"
      f"{'='*70}\n"
    )

  def test_career_progression_bootdev(self):
    """Boot.dev test case: Four-stage career progression"""
    # Arrange
    input_data = ["Cashier", "Supervisor", "Manager", "Director"]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "Director"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Career Progression (Boot.dev)\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should return final position in career progression\n"
      f"{'='*70}\n"
    )

  def test_long_career_history(self):
    """Common case: Long career with many positions"""
    # Arrange
    input_data = [
      "Intern",
      "Junior Developer",
      "Developer",
      "Senior Developer",
      "Team Lead",
      "Engineering Manager",
      "Director of Engineering",
      "VP of Engineering"
    ]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "VP of Engineering"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Long Career History\n"
      f"{'='*70}\n"
      f"📊 Input:    {len(input_data)} positions\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should return last position regardless of list length\n"
      f"{'='*70}\n"
    )

  def test_same_job_multiple_companies(self):
    """Common case: Same title at different companies"""
    # Arrange
    input_data = [
      "Software Engineer at StartupA",
      "Software Engineer at StartupB",
      "Software Engineer at BigTech"
    ]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "Software Engineer at BigTech"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Same Job Multiple Companies\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should return most recent position (last in list)\n"
      f"{'='*70}\n"
    )

  def test_special_characters_in_title(self):
    """Edge case: Job titles with special characters"""
    # Arrange
    input_data = [
      "Jr. Developer",
      "Sr. Engineer",
      "C++ Developer",
      "DevOps Engineer (Remote)"
    ]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "DevOps Engineer (Remote)"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Special Characters in Title\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should handle special characters in job titles\n"
      f"{'='*70}\n"
    )

  def test_numeric_strings(self):
    """Edge case: Numeric values as strings"""
    # Arrange
    input_data = ["Position 1", "Position 2", "Position 3"]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "Position 3"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Numeric Strings\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should handle any string content\n"
      f"{'='*70}\n"
    )

  def test_very_long_job_title(self):
    """Edge case: Extremely long job title"""
    # Arrange
    long_title = "Senior Principal Distinguished Staff Software Engineering Architect"
    input_data = ["Developer", long_title]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = long_title
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Very Long Job Title\n"
      f"{'='*70}\n"
      f"📊 Input:    [..., '{long_title[:30]}...']\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should handle very long job titles\n"
      f"{'='*70}\n"
    )

  def test_whitespace_in_titles(self):
    """Edge case: Titles with extra whitespace"""
    # Arrange
    input_data = ["  Developer  ", "Engineer", "Manager  "]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "Manager  "
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Whitespace in Titles\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: '{expected}'\n"
      f"❌ Got:      '{result}'\n"
      f"💡 Note:    Should return exact string including whitespace\n"
      f"{'='*70}\n"
    )

  def test_empty_string_as_job(self):
    """Edge case: Empty string as a job title"""
    # Arrange
    input_data = ["Developer", "Engineer", ""]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = ""
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Empty String As Job\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: '' (empty string)\n"
      f"❌ Got:      '{result}'\n"
      f"💡 Note:    Should return empty string if it's the last element\n"
      f"{'='*70}\n"
    )

  def test_does_not_modify_input(self):
    """Validation: Function should not modify input list"""
    # Arrange
    input_data = ["Job1", "Job2", "Job3"]
    original = input_data.copy()
    
    # Act
    result = last_work_experience(input_data)
    
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
    
    # Also verify the result is correct
    assert result == "Job3", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Incorrect Result\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: 'Job3'\n"
      f"❌ Got:      '{result}'\n"
      f"{'='*70}\n"
    )

  def test_return_type_string(self):
    """Validation: Return type should be string when list has elements"""
    # Arrange
    input_data = ["Developer", "Engineer"]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    assert isinstance(result, str), (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Return Type Validation\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: str type\n"
      f"❌ Got:      {type(result).__name__}\n"
      f"💡 Note:    Function must return a string, not {type(result).__name__}\n"
      f"{'='*70}\n"
    )

  def test_return_type_none(self):
    """Validation: Return type should be None for empty list"""
    # Arrange
    input_data = []
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    assert result is None, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Return None Validation\n"
      f"{'='*70}\n"
      f"📊 Input:    {input_data}\n"
      f"✅ Expected: None\n"
      f"❌ Got:      {result} ({type(result).__name__})\n"
      f"💡 Note:    Function must return None for empty list\n"
      f"{'='*70}\n"
    )

  def test_realistic_tech_career(self):
    """Real-world scenario: Typical tech career progression"""
    # Arrange
    input_data = [
      "Software Engineering Intern",
      "Junior Software Engineer",
      "Software Engineer",
      "Senior Software Engineer",
      "Staff Engineer"
    ]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "Staff Engineer"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Realistic Tech Career\n"
      f"{'='*70}\n"
      f"📊 Input:    {len(input_data)} positions in tech career\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should return current/most recent position\n"
      f"{'='*70}\n"
    )

  def test_career_change(self):
    """Real-world scenario: Career pivot to different field"""
    # Arrange
    input_data = [
      "Teacher",
      "Private Tutor",
      "Bootcamp Student",
      "Junior Developer",
      "Software Engineer"
    ]
    
    # Act
    result = last_work_experience(input_data)
    
    # Assert
    expected = "Software Engineer"
    assert result == expected, (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: Career Change\n"
      f"{'='*70}\n"
      f"📊 Input:    {len(input_data)} positions across career change\n"
      f"✅ Expected: {expected}\n"
      f"❌ Got:      {result}\n"
      f"💡 Note:    Should return most recent position after career pivot\n"
      f"{'='*70}\n"
    )

  def test_o1_time_complexity_concept(self):
    """Performance validation: Verify O(1) access regardless of size"""
    # Arrange
    small_list = ["Job1", "Job2"]
    large_list = [f"Job{i}" for i in range(1, 1001)]  # 1000 jobs
    
    # Act
    result_small = last_work_experience(small_list)
    result_large = last_work_experience(large_list)
    
    # Assert
    assert result_small == "Job2", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: O(1) Small List\n"
      f"{'='*70}\n"
      f"📊 Input:    {len(small_list)} positions\n"
      f"✅ Expected: 'Job2'\n"
      f"❌ Got:      '{result_small}'\n"
      f"{'='*70}\n"
    )
    
    assert result_large == "Job1000", (
      f"\n{'='*70}\n"
      f"❌ TEST FAILED: O(1) Large List\n"
      f"{'='*70}\n"
      f"📊 Input:    {len(large_list)} positions\n"
      f"✅ Expected: 'Job1000'\n"
      f"❌ Got:      '{result_large}'\n"
      f"💡 Note:    Should access last element in O(1) time regardless of size\n"
      f"            This demonstrates list indexing efficiency!\n"
      f"{'='*70}\n"
    )
