# CH8-L2: Queue Class Implementation

## 📚 Lesson Information
- **Course:** Boot.dev - Data Structures and Algorithms
- **Chapter:** 8 - Queues
- **Lesson:** Queue Class (Assignment)
- **URL:** [Boot.dev Lesson](https://www.boot.dev/lessons/73289433-96a5-4468-a977-7bbe3e731767)

## 🎯 Learning Objectives
Implement a complete Queue class using Python's list as the underlying data structure, supporting all fundamental queue operations with proper error handling.

## 📖 Description
LockedIn uses a Queue to keep track of the order that recruiters should reach out to job seekers. This lesson implements a Queue data structure that follows the FIFO (First In First Out) principle.

## 🔑 Key Concepts

### Queue Operations
| Method | Alternative Name | Description | Time Complexity |
|--------|------------------|-------------|-----------------|
| `push(item)` | `enqueue` | Adds an item to the tail of the queue (index 0) | O(n)* |
| `pop()` | `dequeue` | Removes and returns item from head (last index) | O(1) |
| `peek()` | `front` | Returns item from head without removing | O(1) |
| `size()` | `length` | Returns the number of items in queue | O(1) |

*Note: Using `.insert(0, item)` is O(n) because it shifts all elements. A more efficient implementation would use collections.deque, but this lesson focuses on understanding the concept with basic lists.

### FIFO Principle
```
Push "A"  →  Queue: [A]
Push "B"  →  Queue: [B, A]  (B at index 0, A at index -1)
Push "C"  →  Queue: [C, B, A]
Pop()     →  Returns "A", Queue: [C, B]
Pop()     →  Returns "B", Queue: [C]
```

### Error Handling
- Operations on empty queue (`pop()`, `peek()`) return `None` instead of raising IndexError
- `size()` always returns a valid integer (0 for empty queue)

## 💡 Use Case
**LockedIn Recruiter Queue:**
When job seekers sign up, recruiters need to contact them in the order they registered (fairness). A queue ensures:
- First registrants get contacted first (FIFO)
- No job seeker gets skipped
- Easy tracking of queue length

Example flow:
```python
recruiter_queue = Queue()
recruiter_queue.push("Alice")   # Alice registers
recruiter_queue.push("Bob")     # Bob registers
recruiter_queue.push("Carol")   # Carol registers

next_contact = recruiter_queue.pop()  # "Alice" gets contacted first
remaining = recruiter_queue.size()     # 2 people still waiting
who_is_next = recruiter_queue.peek()   # "Bob" is next (not removed yet)
```

## 🧪 Test Coverage
The test suite includes:
- **Basic Operations:** Push, pop, peek, size
- **Edge Cases:** Empty queue operations, single item
- **FIFO Verification:** Multiple items maintain correct order
- **State Tracking:** Size updates correctly after operations
- **Boot.dev Test Cases:** All provided run_cases and submit_cases
- **Mixed Scenarios:** Alternating operations, many items

## 🏃 Running Tests
```bash
# Navigate to lesson directory
cd CH8-L2

# Run all tests with verbose output
pytest

# Generate HTML report
pytest --html=report.html --self-contained-html

# Run specific test
pytest test_main_pytest.py::TestQueue::test_pop_fifo_order -v
```

## 📊 Implementation Notes
- Uses Python `list` as underlying data structure
- Tail of queue = index 0 (use `.insert(0, item)` for push)
- Head of queue = last index (use `.pop()` for removal)
- Guards against `IndexError` by checking list length
- Maintains O(1) pop operation at the cost of O(n) push

## 🔗 Related Concepts
- **Stack vs Queue:** Stack is LIFO, Queue is FIFO
- **Deque:** Double-ended queue (efficient push/pop at both ends)
- **Priority Queue:** Items have priorities, not just FIFO order
- **Circular Queue:** Fixed-size queue that wraps around
