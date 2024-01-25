"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_linked_list_init(self):
        self.assertEqual(isinstance(self.linked_list, LinkedList), True)
        self.assertEqual(self.linked_list.head, None)
        self.assertEqual(self.linked_list.tail, None)

    def test_insert_beginning(self):
        self.linked_list.insert_beginning({'id': 2})
        self.linked_list.insert_beginning({'id': 1})
        self.linked_list.insert_beginning({'id': 0})

        self.assertEqual(self.linked_list.head.data['id'], 0)
        self.assertEqual(self.linked_list.head.next_node.data['id'], 1)
        self.assertEqual(self.linked_list.tail.data['id'], 2)

    def test_insert_at_end(self):
        self.linked_list.insert_at_end({'id': 0})
        self.linked_list.insert_at_end({'id': 1})
        self.linked_list.insert_at_end({'id': 2})

        self.assertEqual(self.linked_list.head.data['id'], 0)
        self.assertEqual(self.linked_list.head.next_node.data['id'], 1)
        self.assertEqual(self.linked_list.tail.data['id'], 2)

    def test_to_list(self):
        self.linked_list.insert_at_end({'id': 0})
        self.linked_list.insert_at_end({'id': 1})
        self.linked_list.insert_at_end({'id': 2})
        self.linked_list.insert_at_end({'id': 3})
        self.data_list = self.linked_list.to_list()

        self.assertEqual(self.data_list[0]['id'], 0)
        self.assertEqual(self.data_list[1]['id'], 1)
        self.assertEqual(self.data_list[2]['id'], 2)
        self.assertEqual(self.data_list[3]['id'], 3)

    def test_get_data_by_id(self):
        self.linked_list.insert_at_end({'id': 0})
        self.linked_list.insert_at_end({'id': 1})
        self.linked_list.insert_at_end({'id': 2})
        self.linked_list.insert_at_end({'id': 3})

        self.assertEqual(self.linked_list.get_data_by_id(0), {'id': 0})
        self.assertEqual(self.linked_list.get_data_by_id(3), {'id': 3})

    def test_str(self):
        self.linked_list.insert_at_end({'id': 0})
        self.linked_list.insert_at_end({'id': 1})
        self.linked_list.insert_at_end({'id': 2})
        self.linked_list.insert_at_end({'id': 3})

        self.assertEqual(str(self.linked_list), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")