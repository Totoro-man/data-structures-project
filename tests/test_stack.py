"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_stack_init(self):
        self.assertEqual(isinstance(self.stack, Stack), True)
        self.assertEqual(self.stack.top, None)

    def test_push(self):
        self.stack.push(0)
        self.stack.push(1)
        self.assertEqual(self.stack.top.data, 1)
        self.assertEqual(self.stack.top.next_node.data, 0)
        self.assertEqual(self.stack.top.next_node.next_node, None)

    def test_pop(self):
        self.stack.push(0)
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 0)

        with self.assertRaises(AttributeError):
            self.stack.pop()

    def test_str(self):
        self.stack.push(0)
        self.stack.push(1)
        self.assertEqual(str(self.stack), "1\n0")
