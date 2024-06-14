# Task: F Развилки дерева

class Node:
    def __init__(self, value=None):
        """
        Ініціалізує новий об'єкт класу Node.

        Параметри:
        value (optional): Значення, яке зберігається у вузлі. За замовчуванням None.
        """
        self.value = value
        self.left = None  # Лівий дочірній вузол
        self.right = None  # Правий дочірній вузол

    def add(self, value):
        """
        Додає новий вузол зі значенням до бінарного дерева.

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

    def crossroads(self):
        """
        Повертає список вузлів, які мають обидва дочірні вузли.

        Повертає:
        list of str: Список значень вузлів, які мають обидва дочірні вузли.
        """
        result = []

        def dfs(node):
            # Виконуємо обхід дерева в глибину
            if node is None:
                return
            dfs(node.left)  # Обходимо лівий піддерево
            if node.left and node.right:
                # Додаємо значення вузла до результату, якщо він має обидва дочірні вузли
                result.append(str(node.value))
            dfs(node.right)  # Обходимо правий піддерево

        dfs(self)
        return result


def solution(arr):
    """
    Створює бінарне дерево з заданого масиву та повертає значення вузлів, які мають обидва дочірні вузли.

    Параметри:
    arr (list of int): Масив значень для ініціалізації бінарного дерева.

    Повертає:
    str: Строкове представлення значень вузлів, які мають обидва дочірні вузли.
    """
    tree = Node()
    for a in arr:
        tree.add(a)
    return ' '.join(tree.crossroads())


def main():
    print(solution(map(int, input().split()[:-1])))


if __name__ == '__main__':
    main()
