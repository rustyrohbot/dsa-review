# Stack

## What is it?

A stack is a collection of items that follows the Last-In-First-Out principle (LIFO). The most recent item added to the collection will also be the first item to get removed. In other words, items are removed in reverse order to which they were added.

## Space

Memory usage is linearly proportional to the number of elements, so it will take O(n) space.

## Operations
- Push: Add an element to the stack - O(1) runtime
- Pop: Remove and return the most recently added element from the stack - O(1) runtime
- Peek/Top: Return the most recently added element to the stack without removing it - O(1) runtime
- isEmpty: Returns whether the stack contains no elements - O(1) runtime
- Size: Returns the count of the number of elements in the stack - O(1) runtime

## Starter Code
```python
from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        pass

    def pop(self) -> Optional[T]:
        pass

    def peek(self) -> Optional[T]:
        pass

    def is_empty(self) -> bool:
        pass

    def size(self) -> int:
        pass
```