# DSA Boot.dev Course Lessons

This workspace contains lessons from Boot.dev's Data Structures and Algorithms course.

## Lessons

## CH-4 Sorting Algorithms

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

### CH4-L15: Quick Sort
- **URL**: https://www.boot.dev/lessons/5f62f856-53bf-47aa-a5b0-ada9381e3e57
- **Description**: Implementation of the quick sort algorithm - an efficient divide and conquer sorting algorithm widely used in production systems
- **Key Concepts**:
  - Divide and conquer strategy with pivot-based partitioning
  - In-place sorting (better memory usage than merge sort)
  - Time complexity: O(n log n) average case, O(n²) worst case
  - Faster than merge sort in practice due to better cache locality
  - Recursive partitioning around a pivot element
- **Algorithm Steps**:
  1. Choose a pivot element (typically the last element)
  2. Partition: move elements smaller than pivot to the left, larger to the right
  3. Recursively apply quick sort to left and right partitions
  4. Base case: lists with 0 or 1 elements are already sorted
- **Use Case**: Unified sorting solution for both follower counts and revenue - efficient on large datasets while using less memory than merge sort

### CH4-L22: Selection Sort
- **URL**: https://www.boot.dev/lessons/e30cadd2-5610-4b47-bcf3-e54bb44d07a6
- **Description**: Implementation of the selection sort algorithm - a simple comparison-based sorting algorithm that improves upon bubble sort by making only one swap per iteration
- **Key Concepts**:
  - In-place sorting algorithm
  - Time complexity: O(n²) - similar to bubble sort but with fewer swaps
  - Only one swap per iteration (vs multiple in bubble sort)
  - Not adaptive (doesn't benefit from partially sorted data)
  - Predictable performance (always O(n²) regardless of input)
- **Algorithm Steps**:
  1. For each position in the list, find the minimum element in the unsorted portion
  2. Swap the minimum element with the element at the current position
  3. Repeat until the entire list is sorted
- **Use Case**: Sorting LockedIn influencer data when write operations are expensive and datasets are small (fewer swaps than bubble sort)

## CH-5 Exponential Time

### CH5-L3: Fibonacci - Reduction to Polynomial Time
- **URL**: https://www.boot.dev/lessons/87a81b0e-e6e8-442e-b418-c077658c195a
- **Description**: Optimizing the Fibonacci sequence calculation from exponential O(2^n) time to polynomial O(n) time using an iterative approach
- **Key Concepts**:
  - Time complexity optimization: O(2^n) → O(n)
  - Iterative vs recursive algorithms
  - Space complexity: O(1) constant space
  - Dynamic programming fundamentals (avoiding redundant calculations)
  - The Fibonacci sequence: each number is the sum of the two preceding ones
- **Algorithm Steps**:
  1. Initialize `grandparent = 0` and `parent = 1`
  2. Loop `n - 1` times, calculating `current = parent + grandparent`
  3. Update ancestor values: shift `parent` to `grandparent`, `current` to `parent`
  4. Return `current` after loop completes
- **Use Case**: LockedIn influencer analytics - calculating follower growth patterns that follow Fibonacci sequence (6 weeks = 8 followers, 7 weeks = 13 followers). The polynomial algorithm ensures analytics pages load instantly instead of timing out with exponential runtime.

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
