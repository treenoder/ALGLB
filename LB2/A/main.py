import sys


def right_binary_search(arr, target):
    """
    Дано масив цілих чисел, відсортованих у неубуваючому порядку.
    Написати програму, яка обробляє запити на знаходження позиції
    самого правого входження числа target у масив.

    Використовуємо бінарний пошук для знаходження позиції самого правого входження числа target у масив.
    Складність алгоритму:
    - Середній випадок: O(log n) за часом, O(n) за пам'яттю
    - Найкращий випадок: O(1) за часом (якщо target знайдено відразу), O(n) за пам'яттю
    - Найгірший випадок: O(log n) за часом, O(n) за пам'яттю
    """
    left, right = 0, len(arr) - 1

    # Якщо найбільший елемент масиву менший за target або найменший елемент більший за target, то target не може бути в масиві
    if arr[right] < target or arr[left] > target:
        return -1

    result = -1
    while left <= right:
        # Знаходимо середній елемент
        mid = left + (right - left) // 2

        # Якщо середній елемент більший за target, шукаємо у лівій половині
        if arr[mid] > target:
            right = mid - 1
        # Якщо середній елемент менший за target, шукаємо у правій половині
        elif arr[mid] < target:
            left = mid + 1
        # Якщо знайшли target, записуємо його позицію і продовжуємо пошук у правій половині, щоб знайти останнє входження
        else:
            result = mid
            left = mid + 1

    return result


def solution(arr, idx):
    results = []
    for id in idx:
        res = right_binary_search(arr, id) + 1
        results.append(res)
    return results


def main():
    input()
    arr = list(map(int, input().split()))
    idx = []
    for i, line in enumerate(sys.stdin):
        idx.append(int(line))
    result = solution(arr, idx)
    for r in result:
        print(r)


if __name__ == '__main__':
    main()
