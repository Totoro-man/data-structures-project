from src.node import Node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        """Конструктор класса односвязного списка"""
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data,self.head)
        if not self.head:
            self.tail = node
        self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data,None)
        if not self.tail:
            self.tail = node
            self.head = node
        else:
            self.tail.next_node = node
            self.tail = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self) -> list:
        if not self.head:
            return None
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next_node
        return result

    def get_data_by_id(self, id) -> dict:
        data_list = self.to_list()
        for data in data_list:
            try:
                if data["id"] == int(id):
                    return data
            except TypeError:
                print('TypeError: Данные не являются словарем или в словаре нет id.')

