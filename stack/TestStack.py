import unittest
from Stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        """Initialize a fresh stack before each test."""
        self.empty_stack = Stack[int]()

        # Create a pre-populated stack for some tests
        self.populated_stack = Stack[int]()
        self.populated_stack.push(10)
        self.populated_stack.push(20)
        self.populated_stack.push(30)

    def test_empty_stack(self):
        """Test the behavior of an empty stack."""
        self.assertTrue(self.empty_stack.is_empty())
        self.assertEqual(self.empty_stack.size(), 0)
        self.assertIsNone(self.empty_stack.peek())
        self.assertIsNone(self.empty_stack.pop())

    def test_push_operation(self):
        """Test the push operation and its effects on the stack."""
        stack = Stack[int]()
        stack.push(10)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.peek(), 10)

        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.peek(), 30)

        # Test peek doesn't remove items
        stack.peek()
        self.assertEqual(stack.size(), 3)

    def test_push_many_items(self):
        """Test pushing a large number of items to verify no performance issues."""
        stack = Stack[int]()
        num_items = 1000

        for i in range(num_items):
            stack.push(i)

        self.assertEqual(stack.size(), num_items)
        self.assertEqual(stack.peek(), num_items - 1)

    def test_pop_operation(self):
        """Test the pop operation and its effects on the stack."""
        # Use the pre-populated stack from setUp
        self.assertEqual(self.populated_stack.pop(), 30)
        self.assertEqual(self.populated_stack.size(), 2)
        self.assertEqual(self.populated_stack.peek(), 20)

    def test_pop_until_empty(self):
        """Test popping all elements until the stack is empty."""
        stack = self.populated_stack

        while not stack.is_empty():
            stack.pop()

        self.assertTrue(stack.is_empty())
        self.assertIsNone(stack.pop())  # Verify behavior when popping from empty stack

    def test_lifo_behavior(self):
        """Test the Last-In-First-Out behavior of the stack."""
        stack = Stack[int]()
        stack.push(10)
        stack.push(20)
        stack.push(30)

        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())

    def test_mixed_operations(self):
        """Test a mix of push and pop operations."""
        stack = Stack[int]()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.pop(), 20)

        stack.push(30)
        stack.push(40)
        self.assertEqual(stack.pop(), 40)
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.is_empty())

    def test_string_stack(self):
        """Test with string elements to verify generic type handling."""
        stack = Stack[str]()
        stack.push("apple")
        stack.push("banana")
        self.assertEqual(stack.peek(), "banana")
        stack.push("cherry")
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.pop(), "cherry")
        self.assertEqual(stack.pop(), "banana")
        self.assertEqual(stack.size(), 1)

    def test_complex_types(self):
        """Test with more complex data types."""
        stack = Stack[dict]()
        stack.push({"name": "John", "age": 30})
        stack.push({"name": "Jane", "age": 25})

        popped = stack.pop()
        self.assertEqual(popped["name"], "Jane")
        self.assertEqual(popped["age"], 25)

    def test_none_values(self):
        """Test handling of None values (which should be allowed)."""
        stack = Stack[int]()
        stack.push(None)
        self.assertEqual(stack.size(), 1)
        self.assertIsNone(stack.peek())
        self.assertIsNone(stack.pop())
        self.assertTrue(stack.is_empty())

    def test_edge_cases(self):
        """Test various edge cases."""
        stack = Stack[int]()

        # Push and pop single item multiple times
        for _ in range(10):
            stack.push(42)
            self.assertEqual(stack.pop(), 42)
            self.assertTrue(stack.is_empty())

        # Push the same value multiple times
        for _ in range(5):
            stack.push(99)
        self.assertEqual(stack.size(), 5)

        # They should all be the same value
        for _ in range(5):
            self.assertEqual(stack.pop(), 99)


if __name__ == "__main__":
    unittest.main()