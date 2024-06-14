class Synonyms:
    def __init__(self, size: int):
        """
        Ініціалізує новий об'єкт класу Synonyms з вказаним розміром хеш-таблиці.

        Параметри:
        size (int): Розмір хеш-таблиці.
        """
        self.size = size
        # Таблиця для зберігання пар слов - синонімів (ключ: слово, значення: синонім)
        self.left_map = [None] * self.size
        # Таблиця для зберігання пар синонім - слово (ключ: синонім, значення: слово)
        self.right_map = [None] * self.size

    def _get_hash(self, key):
        """
        Обчислює хеш значення для заданого ключа.

        Параметри:
        key (str): Ключ для хешування.

        Повертає:
        int: Хеш значення ключа.
        """
        return hash(key) % self.size

    def add(self, w1, w2):
        """
        Додає пару синонімів до хеш-таблиці.

        Параметри:
        w1 (str): Перше слово.
        w2 (str): Друге слово (синонім до першого слова).
        """
        self._add(self.left_map, w1, w2)
        self._add(self.right_map, w2, w1)

    def _add(self, m: list, key, value):
        """
        Додає пару ключ-значення до вказаної хеш-таблиці.

        Параметри:
        m (list): Хеш-таблиця для додавання.
        key (str): Ключ для додавання.
        value (str): Значення для додавання.
        """
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if m[key_hash] is None:
            # Якщо слот хеш-таблиці порожній, створюємо новий список
            m[key_hash] = [key_value]
        else:
            # Якщо слот зайнятий, перевіряємо наявність ключа в списку
            for pair in m[key_hash]:
                if pair[0] == key:
                    # Якщо ключ вже існує, оновлюємо значення
                    pair[1] = value
                    return
            # Якщо ключ не знайдено, додаємо нову пару до списку
            m[key_hash].append(key_value)

    def get(self, key):
        """
        Повертає синонім для заданого слова.

        Параметри:
        key (str): Слово для пошуку синоніму.

        Повертає:
        str: Синонім для заданого слова або None, якщо слово не знайдено.
        """
        # Спочатку шукаємо слово в left_map, якщо не знайдено, шукаємо в right_map
        return self._get(self.left_map, key) or self._get(self.right_map, key)

    def _get(self, m: list, key):
        """
        Шукає значення для заданого ключа у вказаній хеш-таблиці.

        Параметри:
        m (list): Хеш-таблиця для пошуку.
        key (str): Ключ для пошуку.

        Повертає:
        str: Значення для заданого ключа або None, якщо ключ не знайдено.
        """
        key_hash = self._get_hash(key)
        if m[key_hash] is not None:
            # Перевіряємо кожну пару в слоті
            for pair in m[key_hash]:
                if pair[0] == key:
                    # Якщо знайдено ключ, повертаємо відповідне значення
                    return pair[1]
        # Якщо ключ не знайдено, повертаємо None
        return None


def solution(n, words, query):
    """
    Створює словник синонімів та шукає синонім для заданого слова.

    Параметри:
    n (int): Кількість пар синонімів.
    words (list of tuple): Список пар синонімів.
    query (str): Слово, для якого потрібно знайти синонім.

    Повертає:
    str: Синонім для заданого слова або None, якщо слово не знайдено.
    """
    # Ініціалізуємо об'єкт класу Synonyms з розміром n
    synonyms = Synonyms(n)
    # Додаємо кожну пару слів з списку words до словника синонімів
    for word, syn in words:
        synonyms.add(word, syn)
    # Шукаємо синонім для заданого слова query
    return synonyms.get(query)


def main():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().split())
    query = input()
    print(solution(n, words, query))


if __name__ == '__main__':
    main()
