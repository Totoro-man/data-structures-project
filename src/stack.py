from src.node import Node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        data = self.top.data
        self.top = self.top.next_node
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.top:
            return ''
        temp = self.top
        result = ''
        while temp:
            result += f'{temp.data}'
            temp = temp.next_node
            if temp:
                result += '\n'
        return result