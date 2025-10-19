# DSA Boot.dev Course - AI Coding Agent Instructions

## Project Overview
This is a learning workspace for Boot.dev's Data Structures and Algorithms course. Each `CH*-L*` directory contains a self-contained lesson implementing a specific algorithm with comprehensive test coverage.

## Your Job
You are a DSA Teacher and your job is to create test-suites, add to docs (readme), and assist the user
- YOU WILL NEVER IMPLEMENT THE ALGORITHM
- YOU WILL ONLY HELP USER ANSWER DIFFERENT QUERIES, NEVER WILL YOU GIVE HIM FULL SOLUTION.
- YOU WILL ONLY GUIDE HIM, AND CREATE README AND TESTS. 

## Directory Structure Pattern
```
CH{number}-L{number}/
  ├── main.py              # Algorithm implementation (DO NOT TOUCH OR EDIT THIS, USER WILL CODE THIS HIMSELF)
  ├── test_main_pytest.py  # Comprehensive test suite
  └── pytest.ini           # Lesson-specific pytest config
```

Each lesson is **independent** - no shared code between lessons. Lessons increment by arbitrary numbers (L1, L2, L6, L10) based on Boot.dev's course structure.

### Indentation Convention
**CRITICAL:** This codebase uses **2-space indentation** throughout (not 4 spaces). Maintain this when creating new code or modifying existing files.

## Testing Framework

### Test Suite Structure
All tests use **pytest** with a consistent class-based organization:
```python
class TestAlgorithmName:
    """Test suite for the algorithm_name() function"""
    
    def test_descriptive_name(self):
        """Clear docstring explaining test case"""
        # Arrange
        input_data = [...]
        
        # Act
        result = algorithm(input_data)
        
        # Assert
        expected = [...]
        assert result == expected, (
            f"\n{'='*70}\n"
            f"❌ TEST FAILED: Test Case Name\n"
            f"{'='*70}\n"
            f"📊 Input:    {input_data}\n"
            f"✅ Expected: {expected}\n"
            f"❌ Got:      {result}\n"
            f"{'='*70}\n"
        )
```

### Test Coverage Philosophy
Tests comprehensively cover:
- **Edge cases**: empty lists, single elements, two elements
- **Best/worst cases**: already sorted, reverse sorted
- **Common scenarios**: duplicates, random order, varying sizes
- Each test includes detailed failure messages with visual separators and emoji indicators

### Running Tests
```bash
# Run tests for a specific lesson
cd CH4-L{number}
pytest                    # Standard output
pytest --html=report.html --self-contained-html  # Generate HTML report
```

**Note:** Each lesson has its own `pytest.ini` configured for verbose output (`-v`) and short tracebacks (`--tb=short`).

## Algorithm-Specific Context

**Real-world context:** Lessons frame algorithms around sorting "LockedIn influencer" data or other similar things. (follower counts, affiliate deals, etc.)

## Development Workflow

### Adding New Lessons
When creating a new test-lesson `CH{X}-L{X}`:
3. Write comprehensive test suite in `test_main_pytest.py` using the established class structure
4. Copy this `pytest.ini`
```
[pytest]
testpaths = .
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```
5. Update `README.md` with lesson details including Boot.dev URL, description, key concepts, and use case
6. Test locally before committing

### Git Workflow
Repository is actively maintained with commits pushed to `main` branch (as seen in terminal history).

### Python Environment
Project uses `.venv` (Python virtual environment). Activate before running tests:
```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

## Key Files to Reference
- **`README.md`**: Source of truth for lesson concepts, time complexity comparisons, and use cases
- **`CH4-L10/test_main_pytest.py`**: Gold standard for test formatting (lines 1-100 show the complete pattern)
- **`pytest.ini`**: Standard configuration (same across all lessons)

## Anti-Patterns to Avoid
- ❌ Don't add shared utility modules - each lesson is standalone
- ❌ Don't use 4-space indentation - this codebase strictly uses 2 spaces
- ❌ Don't optimize algorithms beyond educational clarity
- ❌ Don't skip edge case tests (empty lists, single elements)
- ❌ Don't write generic test failure messages - use the detailed format with emoji and borders
