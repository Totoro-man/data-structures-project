import unittest
from src.node import Node


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node0 = Node(0, None)
        self.node1 = Node(1, self.node0)

    def test_node_init(self):
        self.assertEqual(isinstance(self.node0, Node), True)
        self.assertEqual(self.node0.data, 0)
        self.assertEqual(isinstance(self.node1.next_node, Node), True)
        self.assertEqual(self.node1.next_node.data, 0)