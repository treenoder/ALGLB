def solution(p: list[int], q: list[tuple[int, int, int]]) -> str:
    """
    Визначає, чи існує місто в заданому діапазоні, яке перевезло точно вказану кількість людей.

    Параметри:
    p: Список цілих чисел, де кожне число представляє кількість людей, перевезених трамваями в місті.
    q: Список запитів, де кожен запит - це кортеж (l, r, x)
        l: Початковий індекс діапазону (1-базовий індекс).
        r: Кінцевий індекс діапазону (1-базовий індекс).
        x: Кількість людей, яку потрібно перевірити в заданому діапазоні.

    Часова складність:
    O(n + k log m), де n - довжина списку p, k - кількість запитів, m - середня кількість індексів для значення x.

    Просторова складність:
    O(n + k), де n - довжина списку p, k - кількість запитів.

    Повертає:
    Рядок, де кожен символ '1', якщо існує місто в заданому діапазоні [l, r], яке перевезло точно x людей, і '0' в іншому випадку.
    """

    # Створюємо словник для зберігання індексів міст за кількістю перевезених людей
    passengers_indices = {}
    for idx, count in enumerate(p):
        if count not in passengers_indices:
            passengers_indices[count] = []
        # Додаємо індекс (1-базований) до списку індексів для цієї кількості
        passengers_indices[count].append(idx + 1)

    # Бінарний пошук індексу у визначеному діапазоні
    def binary_search(indices, low, high):
        left, right = 0, len(indices) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # Перевіряємо, чи знаходиться індекс у діапазоні [low, high]
            if low <= indices[mid] <= high:
                return True
            elif indices[mid] < low:
                left = mid + 1
            else:
                right = mid - 1
        return False

    results = []
    for l, r, x in q:
        # Якщо x немає у словнику, додаємо '0' до результатів
        if x not in passengers_indices:
            results.append('0')
        else:
            indices = passengers_indices[x]
            # Перевіряємо, чи існує індекс у заданому діапазоні [l, r]
            if binary_search(indices, l, r):
                results.append('1')
            else:
                results.append('0')

    return ''.join(results)


def main():
    input()
    p = list(map(int, input().split()))
    k = int(input())
    q = [list(map(int, input().split())) for _ in range(k)]
    print(solution(p, q))


if __name__ == '__main__':
    main()
