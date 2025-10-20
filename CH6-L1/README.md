# Introduction to Data Structures
URL: https://www.boot.dev/lessons/d2176e10-f96b-4f57-af5c-e03e5c46fc88

Starting with this chapter, we're going to focus on how we can store and organize data in a way that allows for even better algorithms.

Data structures are just organizational tools that allow for more advanced algorithms. Some examples:

- **Stacks**: Last in, first out.  
- **Queues**: First in, first out.  
- **Linked Lists**: A chain of nodes, efficient for inserts and deletes.  
- **Binary Trees**: A tree where each node has up to two children.  
- **Red Black Trees**: A self-balancing binary tree using colors.  
- **Hashmaps**: A data structure that maps keys to values.  
- **Tries**: A tree used for storing and searching words efficiently.  
- **Graphs**: A collection of nodes connected by edges.  

---

## Assignment

Implement the `count_marketers` function. It should accept a list of strings (job titles) and return the number of users who've set their title to `"marketer"`. LockedIn users sometimes use different casing in their titles, so make sure to account for that.

```python
count = count_marketers(['programmer', 'marketer', 'doctor', 'marketer'])
print(count)
# prints "2"
```