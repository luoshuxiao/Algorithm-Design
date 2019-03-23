import unittest

from LinkedList import LinkedList, Node

head = Node(1)


class TestLinkedList(unittest.TestCase):

    def test_size(self):
        """测试获取链表大小"""
        link1 = LinkedList(head)
        self.assertTrue(link1.get_size() == 1)

    def test_append(self):
        """测试添加节点（尾部）"""
        link = LinkedList(head)
        node1 = Node(2)
        link.append_element(node1)
        self.assertTrue(link.get_size() == 2)

    def test_index(self):
        """测试链表结构的正确性（一个节点指向下一个节点）"""
        link = LinkedList(head)
        link.append_element(2)
        link.append_element(3)
        self.assertTrue(link.get_size() == 3)

    def test_data(self):
        """测试通过输入下标(下标超出范围，下标为字符串，下标对应的值)获取数据"""
        link = LinkedList(head)
        link.append_element(2)
        link.append_element(3)
        self.assertTrue(link.get_data(0) == 1)
        self.assertTrue(link.get_data(2) == 3)
        self.assertTrue(link.get_data(-1) == None)
        self.assertTrue(link.get_data(100) == None)
        self.assertTrue(link.get_data('0') == None)
        self.assertTrue(link.get_data('iidh') == None)

    def test_remove_index(self):
        """测试删除（通过下标）节点"""
        link = LinkedList(head)
        link.append_element(2)
        link.append_element(3)
        link.append_element(4)
        link.remove_by_index(-1)
        self.assertTrue(link.get_size() == 4)
        link.remove_by_index(0)
        self.assertTrue(link.head.data == 2)
        self.assertTrue(link.remove_by_index(100) == False)
        self.assertTrue(link.get_size() == 3)

    def test_remove_data(self):
        """测试删除（通过数据值）节点"""
        link = LinkedList(head)
        node1 = Node(3)
        node2 = Node(3)
        node3 = Node(2)
        link.head.next = node1
        node1.next = node2
        node2.next = node3
        link.remove_by_data(3)
        self.assertTrue(link.get_size() == 2)
        self.assertTrue(link.get_data(2) == None)
        self.assertTrue(link.get_data(1) == 2)
        link.remove_by_data('ddd')
        self.assertTrue(link.get_size() == 2)

    def test_insert_index(self):
        """测试插入（通过下标）节点"""
        link = LinkedList(head)
        node1 = Node(2)
        node2 = Node(3)
        node3 = Node(4)
        link.head.next = node1
        node1.next = node2
        node2.next = node3
        link.insert_by_index(2, 1)
        self.assertTrue(link.get_size() == 5)
        self.assertTrue(link.get_data(1) == 2)
        self.assertTrue(link.get_data(2) == 2)
        link.insert_by_index(2, -1)
        link.insert_by_index(2, 100)
        link.insert_by_index(2, 'ddddw')
        self.assertTrue(link.get_size() == 5)

    def test_insert_data(self):
        """测试插入（通过数据值）节点"""
        link = LinkedList(head)
        node1 = Node(2)
        node2 = Node(3)
        node3 = Node(3)
        link.head.next = node1
        node1.next = node2
        node2.next = node3
        link.insert_by_data(10, 3)
        self.assertTrue(link.get_size() == 6)
        self.assertTrue(link.get_data(2) == 10)
        self.assertTrue(link.get_data(4) == 10)
        node4 = Node(1)
        link.insert_by_data(node4, 10)
        self.assertTrue(link.get_index(node4) == [2, 5])


if __name__ == '__main__':
    unittest.main()