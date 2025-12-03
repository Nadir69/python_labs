from typing import Any, Optional
class Node:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Optional[Node] = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка."""
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self._size == 0:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Вставить элемент по индексу idx."""
        if idx < 0 or idx > self._size:
            raise IndexError("Index out of range")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(idx - 1):
            current = current.next  # type: ignore
        new_node.next = current.next  # type: ignore
        current.next = new_node  # type: ignore
        self._size += 1

    def remove_at(self, idx: int) -> None:
        """Удалить элемент по индексу idx."""
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")
        if idx == 0:
            if self.head:
                self.head = self.head.next
                if self._size == 1:
                    self.tail = None
            self._size -= 1
            return
        current = self.head
        for _ in range(idx - 1):
            current = current.next  # type: ignore
        if current.next:
            current.next = current.next.next
            if idx == self._size - 1:
                self.tail = current
        self._size -= 1

    def __iter__(self):
        """Возвращает итератор по значениям в списке."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        """Возвращает количество элементов в списке."""
        return self._size

    def __repr__(self) -> str:
        """Возвращает строковое представление списка."""
        return str(list(self))


# Пример использования:
# sll = SinglyLinkedList()
# sll.append(1)
# print(sll)
# sll.append(2)
# print(sll)
# sll.prepend(0)
# print(sll)
# sll.insert(1, 0.5)  # Список теперь: 0, 0.5, 1, 2
# print(sll)
# sll.remove_at(2)  # Список теперь: 0, 0.5, 2
# print(sll)
# print(len(sll))  # Выведет: 3
# sll.remove_at(2)
# sll.remove_at(2) # Выведет IndexError: Index out of range