# Queue

## What is it?

A queue is a collection of items that follows the First-In-First-Out principle (FIFO). The first item added to the collection will also be the first item to get removed.

## Space

Memory usage is linearly proportional to the number of elements, so it will take O(n) space.

## Operations
- Enqueue: Add an element to the back of the queue - O(1) runtime
- Dequeue: Remove and return the element at the front of the queue - O(1) runtime
- Peek/Front: Return the element at the front of the queue without removing it - O(1) runtime
- isEmpty: Returns whether the queue contains no elements - O(1) runtime
- Size: Returns the count of the number of elements in the queue - O(1) runtime

## Starter Code
```python
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def enqueue(self, item: T) -> None:
        pass

    def dequeue(self) -> Optional[T]:
        pass

    def front(self) -> Optional[T]:
        pass

    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass
```