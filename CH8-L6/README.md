# CH8-L6: Matchmaking Queue

## 📚 Lesson Information
- **Course:** Boot.dev - Data Structures and Algorithms
- **Chapter:** 8 - Queues
- **Lesson:** Matchmaking Queue
- **URL:** [Boot.dev Lesson](https://www.boot.dev/lessons/cd2268ff-f75b-4e02-ae47-148818efced1)

## 🎯 Learning Objectives
Implement a real-world matchmaking system using a queue data structure, demonstrating how to extend traditional queue operations to solve practical problems (adding `search_and_remove` to handle user departures).

## 📖 Description
LockedIn users who are founding companies can join a matchmaking queue to find potential co-founders. When the queue has at least 4 users, the first 2 are automatically matched. Users can also leave the queue at any time.

## 🔑 Key Concepts

### Queue with Extended Functionality
This lesson demonstrates **pragmatic software engineering** - breaking academic constraints when necessary:
- Traditional Queue: Only push/pop from specific ends
- Real-World Queue: Adds `search_and_remove()` to handle departures
- Trade-off: Violates pure FIFO constraint but solves real user needs

### Matchmaking Algorithm
```python
1. Process user action:
   - If "leave" → search_and_remove(name)
   - If "join" → push(name)

2. Check queue size:
   - If size >= 4:
     - Pop first user → user1
     - Pop second user → user2
     - Return "user1 matched user2!"
   - Else:
     - Return "No match found"
```

### Operation Details
| Operation | Method | Purpose | Time Complexity |
|-----------|--------|---------|-----------------|
| Join queue | `push(name)` | Add user to tail | O(n)* |
| Leave queue | `search_and_remove(name)` | Remove user from anywhere | O(n) |
| Match users | `pop()` × 2 | Remove first 2 users | O(1) each |
| Check size | `size()` | Determine if match possible | O(1) |

*O(n) due to `.insert(0, item)` shifting elements

### User Actions
```python
user = ('Bob', 'join')    # Bob joins the queue
user = ('Alice', 'leave') # Alice leaves the queue
```

## 💡 Use Case
**LockedIn Co-Founder Matchmaking:**

1. **Scenario:** Founders need co-founders for their startups
2. **Queue Behavior:**
   - Users join queue as they register interest
   - When 4+ users waiting → match first 2 (FIFO fairness)
   - Users can leave anytime (changed mind, found match elsewhere)
3. **Why Queue Works:**
   - FIFO ensures longest-waiting users matched first (fairness)
   - Automatic matching when threshold reached (efficiency)
   - Search & remove handles real-world cancellations

**Example Flow:**
```python
queue = Queue()
matchmake(queue, ("Alice", "join"))   # Queue: [Alice]
matchmake(queue, ("Bob", "join"))     # Queue: [Bob, Alice]
matchmake(queue, ("Carol", "join"))   # Queue: [Carol, Bob, Alice]
matchmake(queue, ("Dave", "join"))    # Returns: "Alice matched Bob!"
                                       # Queue: [Dave, Carol]
matchmake(queue, ("Carol", "leave"))  # Queue: [Dave]
```

## 🧪 Test Coverage
The test suite includes:
- **Basic Operations:** Join queue, leave queue
- **Match Triggering:** 4th user triggers match, 5th user triggers match
- **Leave Scenarios:** Leave from empty, leave from middle, leave non-existent user
- **Match Format:** Correct string format with user names and exclamation
- **Boot.dev Scenarios:** All run_cases and submit_cases
- **Sequential Matches:** Multiple matches happening in sequence
- **Edge Cases:** Exactly 4 users, empty queue operations

## 🏃 Running Tests
```bash
# Navigate to lesson directory
cd CH8-L6

# Run all tests with verbose output
pytest

# Generate HTML report
pytest --html=report.html --self-contained-html

# Run specific test
pytest test_main_pytest.py::TestMatchmake::test_fourth_user_triggers_match -v
```

## 📊 Implementation Strategy

### Step-by-Step Approach
1. **Extract user data:** `name, action = user`
2. **Handle "leave" action:**
   - Call `queue.search_and_remove(name)`
   - Removes user from any position in queue
3. **Handle "join" action:**
   - Call `queue.push(name)`
   - Adds user to tail of queue
4. **Check for match:**
   - If `queue.size() >= 4`:
     - `user1 = queue.pop()` (first in line)
     - `user2 = queue.pop()` (second in line)
     - Return `f"{user1} matched {user2}!"`
   - Else:
     - Return `"No match found"`

### Queue Class Extensions
The provided `Queue` class includes a special method:

```python
def search_and_remove(self, item):
    """Remove item from anywhere in queue (non-traditional)"""
    if item not in self.items:
        return None
    self.items.remove(item)  # O(n) operation
    return item
```

**Why this violates traditional queues:**
- Standard queues only allow removal from head (pop)
- This method removes from **any position**
- Necessary for real-world "cancel request" functionality

**Trade-offs understood:**
- ✅ Solves real user need (can leave queue anytime)
- ❌ Breaks pure FIFO abstraction
- ⚖️ Acceptable in production when requirements demand it

## 🔗 Related Concepts
- **Priority Queue:** Users could have priorities (premium members matched first)
- **Batch Processing:** Matching users in batches of 2 from pools of 4+
- **Threshold-Based Triggering:** Actions happen when conditions met (size >= 4)
- **Search & Remove Pattern:** Common in real-world queues (cancel orders, requests)

## 🎓 Key Takeaways
1. **Academic vs Real-World:** Sometimes violating pure data structure constraints is necessary
2. **Understand Trade-offs:** Know what you're sacrificing (FIFO purity) and why (user experience)
3. **Threshold Logic:** Automatic actions when conditions met (4+ users → match)
4. **Hybrid Operations:** Combining queue operations (push, pop) with search (search_and_remove)
