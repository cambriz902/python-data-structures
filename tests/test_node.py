import unittest
from models.Node import Node

class NodeUnitTests(unittest.TestCase):
    def test_node_creation(self):
        node = Node(10)
        self.assertEqual(node.value, 10) 

    def test_node_update(self):
        node = Node(5)
        node.value = 20
        self.assertEqual(node.value, 20)  

if __name__ == '__main__':
    unittest.main()