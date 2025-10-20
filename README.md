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

### CH5-L4: Power Set - O(2^n) Exponential Time
- **URL**: https://www.boot.dev/lessons/54b128ea-626d-4cf7-be1d-b719d4a65787
- **Description**: Computing all possible subsets (power set) of a given set - demonstrating true exponential O(2^n) time complexity
- **Key Concepts**:
  - Exponential time complexity: O(2^n)
  - Power set: all possible combinations including empty set and original set
  - Each new element doubles the power set size
  - Combinatorial explosion: 25 items = ~9 hours, 40 items = 34+ years!
  - Demonstrates why exponential algorithms are impractical for large inputs
- **Algorithm Steps**:
  1. If input is empty, return [[]] (power set of empty set)
  2. Initialize `all_subsets` with an empty list [[]]
  3. For each element in input:
     - Create `new_subsets` list
     - For each existing subset, add current element to create new subset
     - Extend `all_subsets` with all `new_subsets`
  4. Return `all_subsets`
- **Growth Rate**: Power set size = 2^n (n=1→2, n=2→4, n=3→8, n=4→16)
- **Use Case**: LockedIn ad targeting segments - computing all possible combinations of influencers for audience targeting. Limited to small sets due to exponential growth making larger computations impossible.

### CH5-L10: Exponential Growth Sequences
- **URL**: https://www.boot.dev/lessons/25218dea-5472-4326-abeb-c653730716e8
- **Description**: Simulating exponential growth of an influencer's followers over time with an adjustable growth factor - demonstrating how sequences grow multiplicatively
- **Key Concepts**:
  - Exponential growth: each value is previous value multiplied by growth factor
  - Sequence generation: building a list of values over time
  - Time complexity: O(n) where n is the number of days
  - Space complexity: O(n) to store the sequence
  - Real-world modeling: viral growth, compound interest, population growth
- **Algorithm Steps**:
  1. Initialize sequence with the starting follower count
  2. For each day in the growth period:
     - Multiply the current count by the growth factor
     - Append the new count to the sequence
  3. Return the complete sequence (length = days + 1)
- **Growth Pattern**: 
  - Factor of 2: 10 → 20 → 40 → 80 (doubling)
  - Factor of 3: 30 → 90 → 270 → 810 (tripling)
  - Factor of 10: 40 → 400 → 4000 → 40000 (10x growth)
- **Use Case**: LockedIn influencer analytics - predicting follower growth for viral content campaigns, modeling best-case growth scenarios for marketing projections. Helps influencers visualize potential reach over time periods.

## CH-6 Data Structures Introduction

### CH6-L1: Introduction to Data Structures - Count Marketers
- **URL**: https://www.boot.dev/lessons/d2176e10-f96b-4f57-af5c-e03e5c46fc88
- **Description**: Introduction to data structures and their role in building efficient algorithms. First lesson focuses on basic list iteration and counting with case-insensitive string matching
- **Key Concepts**:
  - Data structures as organizational tools for algorithms
  - List iteration and element counting
  - Case-insensitive string comparison
  - Time complexity: O(n) where n is the number of job titles
  - Space complexity: O(1) constant space (only storing count)
- **Data Structures Overview**:
  - Stacks: Last in, first out (LIFO)
  - Queues: First in, first out (FIFO)
  - Linked Lists: Chain of nodes, efficient inserts/deletes
  - Binary Trees: Tree with up to two children per node
  - Red Black Trees: Self-balancing binary tree
  - Hashmaps: Key-value mapping structure
  - Tries: Word storage and search optimization
  - Graphs: Nodes connected by edges
- **Algorithm Steps**:
  1. Initialize a counter to 0
  2. Iterate through each job title in the list
  3. Compare each title to "marketer" (case-insensitive)
  4. Increment counter when match is found
  5. Return the final count
- **Use Case**: LockedIn user analytics - counting users by job title to generate demographic reports. Handles inconsistent casing in user-entered job titles (e.g., "Marketer", "marketer", "MARKETER" all count as matches).

### CH6-L4: Lists - Last Work Experience
- **URL**: https://www.boot.dev/lessons/21630e80-ca7b-40d1-b552-926d84bd783b
- **Description**: Deep dive into list data structure performance characteristics and time complexity of common operations. Implements retrieving the last element from a work history list
- **Key Concepts**:
  - List operation time complexities:
    - Append: O(1) - add to end
    - Index access: O(1) - direct access by position
    - Delete from middle: O(n) - requires shifting elements
    - Search: O(n) - must iterate through list
  - Negative indexing in Python (`list[-1]` gets last element)
  - Empty list handling (return None when no data)
  - Lists struggle with: frequent middle deletions and full-list searches
- **Algorithm Steps**:
  1. Check if work history list is empty
  2. If empty, return None
  3. Otherwise, return the last element (most recent job)
  4. Can use `list[-1]` for O(1) access to last element
- **Performance Analysis**:
  - Time complexity: O(1) - direct index access to last element
  - Space complexity: O(1) - no additional storage needed
  - Optimal solution: negative indexing avoids iteration
- **Use Case**: LockedIn user profiles - displaying the most recent job title on a user's profile page. Work history is stored chronologically (oldest to newest), and the last position represents current/most recent employment. Fast O(1) lookup ensures profile pages load instantly.

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
