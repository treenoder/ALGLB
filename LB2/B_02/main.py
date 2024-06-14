def solution(w: int, h: int, n: int) -> int:
    """
    Обчислює мінімальний розмір сторони квадратної дошки, на яку Стасик зможе розмістити всі свої дипломи.

    Параметри:
    w: Ширина диплому.
    h: Висота диплому.
    n: Кількість дипломів.

    Складність:
    O(log(max(w, h) * n) * log(n))

    Повертає:
    Мінімальний розмір сторони квадратної дошки.
    """

    # Для перевірки, чи можна розмістити n дипломів на дошці розміру size x size
    def can_fit(size):
        return (size // w) * (size // h) >= n

    # Початкові значення для бінарного пошуку
    left, right = 0, max(w, h) * n
    while left < right:
        mid = left + (right - left) // 2
        # Якщо на дошці розміру mid x mid можна розмістити n дипломів, звужуємо праву межу
        if can_fit(mid):
            right = mid
        else:
            # Інакше звужуємо ліву межу
            left = mid + 1
    # Повертаємо мінімальний розмір сторони квадратної дошки
    return left


def main():
    w, h, n = tuple(map(int, input().split()))
    print(solution(w, h, n))


if __name__ == '__main__':
    main()
