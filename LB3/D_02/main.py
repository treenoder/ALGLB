# Task: D. Удаление элемента из односвязного списка
# На вход подается массив чисел и число n. Удалите из списка все элементы, равные n.
#
# Формат входных данных
# В первой строке вводится массив чисел. Во второй строке вводится число n.
#
# Формат выходных данных
# Необходимо вывести список без элементов, равных n.
#

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def add(self, value):
        if self.value is None:
            self.value = value
            return
        current = self
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def remove(self, value):
        while self.value == value:
            self.value = self.next.value
            self.next = self.next.next
        current = self
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
            else:
                current = current.next

    def __str__(self):
        current = self
        result = []
        while current is not None:
            result.append(str(current.value))
            current = current.next
        return ' '.join(result)


def solution(arr, n):
    lst = Node()
    for a in arr:
        lst.add(a)
    lst.remove(n)
    return str(lst)


def main():
    input()
    print(solution(input().split(), input()))


if __name__ == '__main__':
    main()
