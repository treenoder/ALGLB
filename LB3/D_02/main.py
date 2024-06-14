class Node:
    def __init__(self, value=None):
        """
        Ініціалізує новий об'єкт класу Node.

        Параметри:
        value (optional): Значення, яке зберігається у вузлі. За замовчуванням None.
        """
        self.value = value
        self.next = None

    def add(self, value):
        """
        Додає новий вузол зі значенням до кінця зв'язаного списку.

        Параметри:
        value: Значення, яке потрібно додати до списку.
        """
        if self.value is None:
            # Якщо вузол пустий, присвоюємо значення цьому вузлу
            self.value = value
            return
        current = self
        # Проходимо до кінця списку
        while current.next is not None:
            current = current.next
        # Додаємо новий вузол в кінець списку
        current.next = Node(value)

    def remove(self, value):
        """
        Видаляє всі вузли зі списку, які мають задане значення.

        Параметри:
        value: Значення, яке потрібно видалити зі списку.
        """
        # Видаляємо елементи з початку списку, які мають значення value
        while self.value == value:
            self.value = self.next.value
            self.next = self.next.next
        current = self
        # Видаляємо елементи в середині та в кінці списку, які мають значення value
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
            else:
                current = current.next

    def __str__(self):
        """
        Повертає строкове представлення зв'язаного списку.

        Повертає:
        str: Строкове представлення зв'язаного списку.
        """
        current = self
        result = []
        # Проходимо по всіх вузлах і додаємо їх значення до списку result
        while current is not None:
            result.append(str(current.value))
            current = current.next
        # Повертаємо значення вузлів через пробіл
        return ' '.join(result)


def solution(arr, n):
    """
    Створює зв'язаний список з заданого масиву та видаляє всі вузли з вказаним значенням.

    Параметри:
    arr (list of int): Масив значень для ініціалізації зв'язаного списку.
    n (int): Значення, яке потрібно видалити зі списку.

    Повертає:
    str: Строкове представлення зв'язаного списку після видалення елементів.
    """
    lst = Node()
    # Додаємо всі елементи масиву до зв'язаного списку
    for a in arr:
        lst.add(a)
    # Видаляємо всі елементи зі значенням n
    lst.remove(n)
    # Повертаємо строкове представлення списку
    return str(lst)


def main():
    input()
    print(solution(input().split(), input()))


if __name__ == '__main__':
    main()
