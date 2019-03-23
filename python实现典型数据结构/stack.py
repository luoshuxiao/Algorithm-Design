# python实现堆栈数据结构


class Stack(object):

    def __init__(self, maxsize):
        self.s_list = []
        self.maxsize = maxsize

    def push_element(self, data):
        """
        压栈（压入数据）
        :param data: 数据
        :return:
        """
        if self.current_size() < self.maxsize:
            return self.s_list.append(data)

    def pop_element(self):
        """
        弹栈（取出数据）
        :return:
        """
        if self.s_list:
            element = self.s_list[0]
            self.s_list.remove(self.s_list[0])
            return element
        else:
            return None

    def select_data(self, data):
        """
        获取目标数据在该容器中的下标
        :param data: 目标数据
        :return: 元素是下标的列表（可能有多个符合条件的下标）
        """
        index_list = []
        for i in self.s_list:
            if i == data:
                index_list.append(self.s_list.index(i))
        return index_list

    def select_index(self, num):
        """
        通过下标获取数据
        :param num: 目标数据的下标
        :return: 目标数据
        """
        if 0 <= num < self.maxsize:
            return self.s_list[num]
        else:
            return None

    def current_size(self):
        """
        获取当前堆栈的数据大小（数据个数）
        :return: 数据的个数（int类型）
        """
        return len(self.s_list)

    def __repr__(self):
        return str(self.s_list)


def main_test():
    stack1 = Stack(5)  # 创建一个宽度为5的堆栈数据结构对象
    stack1.push_element(1)
    print(f'此时堆栈为：{stack1.s_list}')
    stack1.push_element(2)
    print(f'此时堆栈为：{stack1.s_list}')
    stack1.push_element(3)
    print(f'此时堆栈为：{stack1.s_list}')
    stack1.push_element(4)
    print(f'此时堆栈为：{stack1.s_list}')
    stack1.push_element(5)
    print(f'此堆栈刚满，堆栈为：{stack1.s_list}')
    print(stack1.current_size())
    print(f'此时堆栈为：{stack1.s_list}')
    stack1.push_element(4)
    stack1.push_element(4)
    print(f'此堆栈满了后，再压入元素后，堆栈为：{stack1.current_size()}')
    print(f'第一次取出元素：{stack1.pop_element()}')
    print(f'第二次取出元素：{stack1.pop_element()}')
    print(f'取出两个元素后：{stack1.s_list}')


if __name__ == '__main__':
    main_test()
