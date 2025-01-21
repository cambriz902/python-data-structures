import unittest

from models.LinkedList import LinkedList

class LinkedListUnitTests(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_linked_list_init(self):
        self.assertEqual(self.linked_list.head, None)
        self.assertEqual(self.linked_list.tail, None)
        self.assertEqual(self.linked_list.length, 0)

    def test_add_to_front(self):
        for index in range(1, 5):
            self.linked_list.add_value_to_front(index)

        self.assertEqual(self.linked_list.head.value, 4)
        self.linked_list.add_value_to_front(10)
        self.assertEqual(self.linked_list.head.value, 10)

    def test_get_value_at_index(self):
        for value in range(1, 5):
            self.linked_list.add_value_to_front(value)
        for index in range(0, 4):  
            self.assertEqual(4 - index, self.linked_list.get_value_at_index(index))

      
        



