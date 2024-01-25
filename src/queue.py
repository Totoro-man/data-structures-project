from src.node import Node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if not self.tail:
            self.tail = node
            self.head = node
        else:
            self.tail.next_node = node
            self.tail = node


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next_node
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:
            return ''
        temp = self.head
        result = ''
        while temp:
            result += f'{temp.data}'
            temp = temp.next_node
            if temp:
                result += '\n'
        return result