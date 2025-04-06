from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> Optional[T]:
        if not self.items:
            return None
        return self.items.pop(0)

    def peek(self) -> Optional[T]:
        if not self.items:
            return None
        return self.items[0]

    def is_empty(self) -> bool:
        return not self.items

    def size(self) -> int:
        return len(self.items)