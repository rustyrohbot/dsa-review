import unittest
from Queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        """Initialize a fresh queue before each test."""
        self.empty_queue = Queue[int]()

        # Create a pre-populated queue for some tests
        self.populated_queue = Queue[int]()
        self.populated_queue.enqueue(10)
        self.populated_queue.enqueue(20)
        self.populated_queue.enqueue(30)

    def test_empty_queue(self):
        """Test the behavior of an empty queue."""
        self.assertTrue(self.empty_queue.is_empty())
        self.assertEqual(self.empty_queue.size(), 0)
        self.assertIsNone(self.empty_queue.peek())
        self.assertIsNone(self.empty_queue.dequeue())

    def test_enqueue_operation(self):
        """Test the enqueue operation and its effects on the queue."""
        queue = Queue[int]()
        queue.enqueue(10)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.peek(), 10)

        queue.enqueue(20)
        queue.enqueue(30)
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.peek(), 10)  # First in, still at front

        # Test front doesn't remove items
        queue.peek()
        self.assertEqual(queue.size(), 3)

    def test_enqueue_many_items(self):
        """Test enqueueing a large number of items to verify no performance issues."""
        queue = Queue[int]()
        num_items = 1000

        for i in range(num_items):
            queue.enqueue(i)

        self.assertEqual(queue.size(), num_items)
        self.assertEqual(queue.peek(), 0)  # First item should still be at front

    def test_dequeue_operation(self):
        """Test the dequeue operation and its effects on the queue."""
        # Use the pre-populated queue from setUp
        self.assertEqual(self.populated_queue.dequeue(), 10)
        self.assertEqual(self.populated_queue.size(), 2)
        self.assertEqual(self.populated_queue.peek(), 20)

    def test_dequeue_until_empty(self):
        """Test dequeuing all elements until the queue is empty."""
        queue = self.populated_queue

        while not queue.is_empty():
            queue.dequeue()

        self.assertTrue(queue.is_empty())
        self.assertIsNone(queue.dequeue())  # Verify behavior when dequeuing from empty queue

    def test_fifo_behavior(self):
        """Test the First-In-First-Out behavior of the queue."""
        queue = Queue[int]()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)
        self.assertTrue(queue.is_empty())

    def test_mixed_operations(self):
        """Test a mix of enqueue and dequeue operations."""
        queue = Queue[int]()
        queue.enqueue(10)
        queue.enqueue(20)
        self.assertEqual(queue.dequeue(), 10)

        queue.enqueue(30)
        queue.enqueue(40)
        self.assertEqual(queue.dequeue(), 20)
        self.assertEqual(queue.dequeue(), 30)
        self.assertEqual(queue.dequeue(), 40)
        self.assertTrue(queue.is_empty())

    def test_string_queue(self):
        """Test with string elements to verify generic type handling."""
        queue = Queue[str]()
        queue.enqueue("apple")
        queue.enqueue("banana")
        self.assertEqual(queue.peek(), "apple")
        queue.enqueue("cherry")
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), "apple")
        self.assertEqual(queue.dequeue(), "banana")
        self.assertEqual(queue.size(), 1)

    def test_complex_types(self):
        """Test with more complex data types."""
        queue = Queue[dict]()
        queue.enqueue({"name": "John", "age": 30})
        queue.enqueue({"name": "Jane", "age": 25})

        dequeued = queue.dequeue()
        self.assertEqual(dequeued["name"], "John")
        self.assertEqual(dequeued["age"], 30)

    def test_none_values(self):
        """Test handling of None values (which should be allowed)."""
        queue = Queue[int]()
        queue.enqueue(None)
        self.assertEqual(queue.size(), 1)
        self.assertIsNone(queue.peek())
        self.assertIsNone(queue.dequeue())
        self.assertTrue(queue.is_empty())

    def test_edge_cases(self):
        """Test various edge cases."""
        queue = Queue[int]()

        # Enqueue and dequeue single item multiple times
        for _ in range(10):
            queue.enqueue(42)
            self.assertEqual(queue.dequeue(), 42)
            self.assertTrue(queue.is_empty())

        # Enqueue the same value multiple times
        for _ in range(5):
            queue.enqueue(99)
        self.assertEqual(queue.size(), 5)

        # They should all be the same value and in order
        for _ in range(5):
            self.assertEqual(queue.dequeue(), 99)


if __name__ == "__main__":
    unittest.main()