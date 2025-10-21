# CH9-L1: Linked Lists - Node Implementation

## 📚 Lesson Information
- **Course:** Boot.dev - Data Structures and Algorithms
- **Chapter:** 9 - Linked Lists
- **Lesson:** Linked Lists (Introduction)
- **URL:** [Boot.dev Lesson](https://www.boot.dev/lessons/6d49ab0d-1c58-44ba-9a78-22f22178f1ba)

## 🎯 Learning Objectives
Understand the fundamental building block of linked lists - the **Node** - and how nodes link together to form a chain. Learn why linked lists solve the performance problem of queue operations.

## 📖 Description
This lesson addresses a critical performance issue: the Queue's `push()` method is O(n) because it uses `.insert(0, item)` which shifts all elements. By building a queue with a **Linked List** instead of an array, we can achieve O(1) push operations.

## 🔑 Key Concepts

### The Performance Problem
```python
# Current Queue implementation
def push(self, item):
    # Everything in self.items has to shift
    # up a position, which takes O(n) time
    self.items.insert(0, item)
```

**Why is this slow?**
- Arrays store elements **contiguously** in memory
- Inserting at index 0 requires shifting **all** existing elements
- Time complexity: O(n) where n = number of items

### Linked Lists Solution
Elements are **not stored next to each other** in memory. Instead, each item **references** the next in a chain.

```
Array/List (contiguous memory):
[Item1][Item2][Item3][Item4]
 ↑ All items stored side-by-side

Linked List (scattered memory):
[Item1] → [Item2] → [Item3] → [Item4] → None
 Each item has pointer to next
```

### Node Structure
| Field | Type | Description |
|-------|------|-------------|
| `val` | any | The data stored in the node (e.g., "Carla", "James") |
| `next` | Node or None | Reference to the next node in the chain |

### Visual Representation
```
Node 1                Node 2                Node 3
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ val: "Alice" │     │ val: "Bob"   │     │ val: "Carol" │
│ next: ────────┼────→│ next: ────────┼────→│ next: None   │
└──────────────┘     └──────────────┘     └──────────────┘
```

### Node Operations
```python
# Create a node
node1 = Node("Llewelyn Moss")
# node1.val = "Llewelyn Moss"
# node1.next = None

# Create another node
node2 = Node("Anton Chigurh")

# Link them together
node1.set_next(node2)
# Now: node1.next points to node2

# Traversal
current = node1
while current:
    print(current.val)
    current = current.next
# Output: Llewelyn Moss
#         Anton Chigurh
```

## 💡 Use Case
**LockedIn Queue Performance Optimization:**

Before (Array-based Queue):
- Push operation: O(n) - shifts all elements
- 1,000 recruiters joining queue = slow
- Poor performance as queue grows

After (Linked List Queue):
- Push operation: O(1) - just update pointers
- 1,000,000 recruiters = still fast
- Constant-time performance regardless of size

## 🧪 Test Coverage
The test suite includes:
- **Initialization:** Node created with value and next=None
- **Linking:** `set_next()` connects two nodes
- **Chaining:** Multiple nodes linked together
- **Traversal:** Walking through the linked list
- **Boot.dev Scenarios:** All test cases from the lesson
- **Edge Cases:** Empty strings, multiple set_next calls, node independence

## 🏃 Running Tests
```bash
# Navigate to lesson directory
cd CH9-L1

# Run all tests with verbose output
pytest

# Generate HTML report
pytest --html=report.html --self-contained-html

# Run specific test
pytest test_main_pytest.py::TestNode::test_set_next_links_two_nodes -v
```

## 📊 Implementation Guide

### Step 1: Constructor (`__init__`)
```python
def __init__(self, val):
    self.val = val      # Store the value
    self.next = None    # Initialize next as None (end of chain)
```

### Step 2: Set Next Method
```python
def set_next(self, node):
    self.next = node    # Link to the provided node
```

### Why This Works
- **Simple pointer manipulation** instead of array shifting
- **O(1) time complexity** for linking nodes
- **Memory efficient** - only stores what's needed
- **Dynamic size** - no pre-allocation required

## 🔗 Performance Comparison

### Array-Based Queue
| Operation | Time Complexity | Reason |
|-----------|----------------|--------|
| `push(item)` | O(n) | Shift all elements |
| `pop()` | O(1) | Remove from end |
| `peek()` | O(1) | Access last element |

### Linked List Queue (Coming Soon)
| Operation | Time Complexity | Reason |
|-----------|----------------|--------|
| `push(item)` | O(1) | Just update head pointer |
| `pop()` | O(1) | Update tail pointer |
| `peek()` | O(1) | Access head/tail |

## 🎓 Key Takeaways

1. **Nodes are the building blocks** of linked lists
2. **Each node stores data + reference** to the next node
3. **Pointers enable O(1) insertions** (no shifting required)
4. **Trade-off:** No random access (can't use `list[5]` indexing)
5. **Memory scattered** vs contiguous (arrays)

## 🔗 Related Concepts
- **Doubly Linked Lists:** Nodes have `prev` and `next` pointers
- **Circular Linked Lists:** Last node points back to first
- **Skip Lists:** Multi-level linked lists for faster search
- **Graph Adjacency Lists:** Nodes point to multiple neighbors

## 📝 Next Steps
In upcoming lessons, you'll:
- Build a complete LinkedList class
- Implement queue operations using linked lists
- Compare performance with array-based implementations
- Learn about doubly linked lists
