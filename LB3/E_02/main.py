# Task: E Обход дерева

class Node:
    def __init__(self, value=None):
        """
        Ініціалізує новий об'єкт класу Node.

        Параметри:
        value (optional): Значення, яке зберігається у вузлі. За замовчуванням None.
        """
        self.value = value
        # Лівий дочірній вузол
        self.left = None
        # Правий дочірній вузол
        self.right = None

    def add(self, value):
        """
        Додає новий вузол зі значенням до бінарного дерева пошуку.

        Параметри:
        value: Значення, яке потрібно додати до дерева.
        """
        if self.value is None:
            # Якщо вузол пустий, присвоюємо значення цьому вузлу
            self.value = value
            return
        current = self
        while True:
            if value < current.value:
                # Якщо значення менше поточного, йдемо в лівий дочірній вузол
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            elif value > current.value:
                # Якщо значення більше поточного, йдемо в правий дочірній вузол
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                # Якщо значення вже існує, не додаємо його
                return

    def __str__(self):
        """
        Повертає строкове представлення елементів дерева в порядку зростання.

        Повертає:
        str: Строкове представлення елементів дерева.
        """
        result = []

        def dfs(node):
            # Виконуємо обхід дерева в глибину
            if node is None:
                return
            # Обходимо лівий піддерево
            dfs(node.left)
            # Додаємо значення вузла до результату
            result.append(str(node.value))
            # Обходимо правий піддерево
            dfs(node.right)

        dfs(self)
        return ' '.join(result)


def solution(arr):
    """
    Створює бінарне дерево пошуку з заданого масиву та повертає його елементи в порядку зростання.

    Параметри:
    arr (list of int): Масив значень для ініціалізації бінарного дерева пошуку.

    Повертає:
    str: Строкове представлення елементів дерева в порядку зростання.
    """
    tree = Node()
    for a in arr:
        tree.add(a)
    return str(tree)


def main():
    print(solution(map(int, input().split()[:-1])))


if __name__ == '__main__':
    main()
