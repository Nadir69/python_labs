from typing import Any


class Stack:
    def __init__(self) -> None:
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Добавить элемент на вершину стека."""
        self._data.append(item)

    def pop(self) -> Any:
        """Снять верхний элемент стека и вернуть его.
        Если стек пуст — выбросить понятное исключение (например, IndexError с вменяемым сообщением).
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        """Вернуть верхний элемент без удаления.
        Если стек пуст — вернуть None.
        """
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Вернуть True, если стек пуст, иначе False."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в стеке."""
        return len(self._data)



# Пример использования:
# stack = Stack()
# stack.push(1)
# print(stack.peek()) # Выведет: 1
# stack.push(2)
# print(stack.peek()) # Выведет: 2
# print(len(stack)) # Выведет: 2
# print(stack.pop())  # Выведет: 2
# print(stack.peek()) # Выведет: 1
# print(stack.is_empty()) # Выведет: False
# stack.pop()
# stack.pop() # Выбросит IndexError: pop from empty stack




from collections import deque
class Queue:
    def __init__(self) -> None:
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Взять элемент из начала очереди и вернуть его.
        Если очередь пустая — выбросить понятное исключение (например, IndexError).
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """Вернуть первый элемент без удаления.
        Если очередь пустая — вернуть None.
        """
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Вернуть True, если очередь пуста."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в очереди."""
        return len(self._data)


# Пример использования:
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# print(queue.peek())     # Выведет: 1
# queue.enqueue(3)
# print(queue.peek())     # Выведет: 1
# queue.enqueue(2)
# print(queue.dequeue())  # Выведет: 1
# print(queue.peek())     # Выведет: 2
# print(queue.is_empty()) # Выведет: False
# print(len(queue))      # Выведет: 3
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue() # Выбросит IndexError: dequeue from empty queue

import timeit

stack = Stack()
queue = Queue()

# Measure stack push
print("Stack push:", timeit.timeit(lambda: stack.push(1), number=100000))

# Measure stack pop
stack.push(1)
print("Stack pop:", timeit.timeit(lambda: stack.pop(), number=100000))

# Measure queue enqueue
print("Queue enqueue:", timeit.timeit(lambda: queue.enqueue(1), number=100000))

# Measure queue dequeue
queue.enqueue(1)
print("Queue dequeue:", timeit.timeit(lambda: queue.dequeue(), number=100000))

# Stack push: 0.003658958999949391
# Stack pop: 0.006326333000288287
# Queue enqueue: 0.004075875000125961
# Queue dequeue: 0.0061863749997428386