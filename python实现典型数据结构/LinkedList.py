# python实现链表数据结构


class Node(object):
    """声明节点类"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self, node):
        self.head = node

    def append_element(self, data):
        """
        在链表最后添加节点
        :param data: 节点的数据
        :return:
        """
        node = Node(data)
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def insert_by_index(self, data, index):
        """
        通过下标插入节点
        :param data: 节点的数据
        :param index: 插入目标节点的下标
        :return:
        """
        node = Node(data)
        if type(index) is int:
            if index == 0:
                behind_node = self.head
                self.head = node
                self.head.next = behind_node
            elif 0 < index < self.get_size():
                before_node = self.head
                for _ in range(index-1):
                    before_node = before_node.next
                behind_node = before_node.next
                before_node.next = node
                node.next = behind_node
            else:
                print('下标越界，插入失败')
        else:
            print('下标输入有误,插入失败')

    def insert_by_data(self, insert_data, exist_data):
        """
        通过指定的数据插入节点
        :param insert_data: 需要插入的节点的数据值
        :param exist_data: 插入链表中指定的目标节点的数据值
        :return:
        """
        index_list = self.get_index(exist_data)
        if not index_list:
            print('该链表未找到您指定的数据，插入失败')
            return None
        index_l = [index_list[i]+i for i in range(len(index_list))]
        for i in index_l:
            self.insert_by_index(insert_data, i)

    def remove_by_data(self, data):
        """
        通过节点的数据值删除节点
        :param data: 要删除节点的数据值
        :return:
        """
        before_node = self.head
        while before_node:
            if before_node.data == data:
                index = self.get_index(data)
                index_list = [index[i]-i for i in range(len(index))]
                for i in index_list:
                    self.remove_by_index(i)
                break
            before_node = before_node.next
        else:
            print(f'该链表没有与数据：{data}，匹配的节点，删除失败')
            return None

    def remove_by_index(self, index):
        """
        通过下标删除节点
        :param index: 待删除节点的下标
        :return:
        """
        before_node = self.head
        size = self.get_size()
        if type(index) is int:
            if index == 0:
                self.head = self.head.next
                return 1
            elif 0 < index < size:
                for i in range(index - 1):
                    before_node = before_node.next
                behind_node = before_node.next.next
                before_node.next = behind_node
                return 1
            else:
                print('下标越界,删除失败')
                return 0
        else:
            print('下标输入有误,删除失败')

    def get_data(self, index):
        """
        通过下标获取目标节点的数据值
        :param index: 目标节点的下标
        :return: 节点的数据值
        """
        if type(index) is int:
            if index == 0:
                return self.head.data
            if 0 < index < self.get_size():
                node = self.head
                for _ in range(index):
                    node = node.next
                return node.data
            else:
                print('下标超出范围，获取节点数据失败')
        else:
            print('请输入int类型下标')

    def get_index(self, data):
        """
        通过指定的节点数据值获取节点的下标
        :param data: 目标节点的数据值
        :return: 元素是目标节点下标的列表（可能存在多个下标）
        """
        node = self.head
        index_list = []
        for i in range(self.get_size()):
            if node.data == data:
                index_list.append(i)
            node = node.next
        if not index_list:
            print(f'此链表并无与{data}相等的节点，获取节点下标失败')
        return index_list

    def get_size(self):
        """
        获取当前链表的宽度（链表节点的个数）
        :return: 链表的宽度（int类型）
        """
        node = self.head
        size = 0
        while node:
            node = node.next
            size += 1
        return size

    def __repr__(self):
        node = self.head
        list_data = []
        while node:
            list_data.append(node.data)
            node = node.next
        return str(list_data)


def main_test():
    head = Node(4)
    link = LinkedList(head)
    # link.append_element(6)
    # link.append_element(12)
    # link.append_element(300)
    # link.append_element(6)
    # print(link)
    # # print(link.get_size())
    # print(link.get_index(6))
    # # print(link.get_data(0))
    # # link.remove_by_data(6)
    # # print(link)
    # # link.remove_by_index(1)
    # # print(link)
    # link.insert_by_index(44444, 0)
    # print(link)
    # # link.insert_by_index(33333, 2)
    # # print(link)
    link.insert_by_data(33333, 6)
    print(link)


if __name__ == '__main__':
   main_test()
