# DSA Boot.dev Course Lessons

This workspace contains lessons from Boot.dev's Data Structures and Algorithms course.

## Lessons

### CH4-L1: Introduction to Sorting
- **URL**: https://www.boot.dev/lessons/d4b077d7-3d68-4cd6-8996-ff54bccf7585
- **Description**: Introduction to sorting algorithms and their importance in computer science

### CH4-L2: Bubble Sort Implementation
- **URL**: https://www.boot.dev/lessons/ad175094-e40d-4d49-baf7-d364da42216c
- **Description**: Implementation of the bubble sort algorithm with testing

### CH4-L6: Merge Sort
- **URL**: https://www.boot.dev/lessons/5066e081-58bf-4d24-a218-cd267f04948b
- **Description**: Implementation of the merge sort algorithm - a divide and conquer sorting algorithm that's much faster than bubble sort, especially for large datasets (1000+ elements)
- **Key Concepts**:
  - Divide and conquer strategy
  - Recursive sorting
  - Merging sorted lists
  - Time complexity: O(n log n) vs Bubble Sort's O(n²)
- **Use Case**: Sorting LockedIn influencer followers by follower count efficiently

### CH4-L10: Insertion Sort
- **URL**: https://www.boot.dev/lessons/83e64b78-29cd-4b5d-8fec-6f910475d4e5
- **Description**: Implementation of the insertion sort algorithm - builds a sorted list one item at a time by inserting each element into its proper position
- **Key Concepts**:
  - In-place sorting algorithm
  - Time complexity: O(n²) - less efficient than merge sort on large lists
  - Faster than merge sort on small lists (due to smaller constants)
  - Better memory efficiency than merge sort
  - Stable sort (maintains relative order of equal elements)
- **Algorithm Steps**:
  1. Start from the second element (index 1)
  2. Compare with elements to its left
  3. Swap with larger elements until finding correct position
  4. Repeat for all elements
- **Use Case**: Sorting influencer affiliate deals by revenue (small datasets of ~200 items where insertion sort is faster and uses less server memory)

## Running Tests

Each lesson includes pytest tests. To run tests for a specific lesson:

```bash
cd CH4-L1
pytest

# Or with HTML report
pytest --html=report.html --self-contained-html
```

## Repository

- **Owner**: SafuGit
- **Repository**: [DSA-Bootdev](https://github.com/SafuGit/DSA-Bootdev)
