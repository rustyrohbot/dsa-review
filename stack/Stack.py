from typing import TypeVar, Generic, Optional, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> Optional[T]:
        if not self.items:
            return None
        return self.items.pop()

    def peek(self) -> Optional[T]:
        if not self.items:
            return None
        return self.items[-1]

    def is_empty(self) -> bool:
        return not self.items

    def size(self) -> int:
        return len(self.items)


if __name__ == "__main__":
    stack: Stack[int] = Stack()
    stack.push(10)
    print(stack.peek())
    print(stack.pop())
    print(stack.is_empty())