"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_queue_init(self):
        self.assertEqual(isinstance(self.queue, Queue), True)
        self.assertEqual(self.queue.head, None)
        self.assertEqual(self.queue.tail, None)

    def test_enqueue(self):
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.head.data, 0)
        self.assertEqual(self.queue.head.next_node.data, 1)
        self.assertEqual(self.queue.head.next_node.next_node, None)
        self.assertEqual(self.queue.tail.data, 1)

    def test_dequeue(self):
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.dequeue(), 1)

    def test_str(self):
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.assertEqual(str(self.queue),"0\n1")