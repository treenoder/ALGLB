def is_possible(distance, stalls, k):
    """
    Перевіряє, чи можливо розмістити k корів у стійлах з мінімальною відстанню distance між будь-якими двома коровами.
    Повертає True, якщо можливо розмістити k корів з мінімальною відстанню distance, інакше False.
    """
    count = 1
    last_position = stalls[0]

    # Перевірка кожного стійла
    for i in range(1, len(stalls)):
        # Якщо відстань між поточним стійлом і останнім зайнятим стійлом >= distance
        if stalls[i] - last_position >= distance:
            count += 1
            last_position = stalls[i]
            if count == k:
                return True
    return False


def solution(arr, k):
    """
    Знаходить найбільшу мінімальну відстань між k коровами, які можуть бути розміщені у стійлах.
    Складність алгоритму: O(n log d) за часом, де n - кількість стійл, d - різниця між найбільшим і найменшим стійлом (log(max(arr) - min(arr))).
    """
    left = 0
    right = arr[-1] - arr[0]
    result = 0

    # Використання бінарного пошуку для знаходження максимальної мінімальної відстані
    while left <= right:
        mid = left + (right - left) // 2
        # Перевірка, чи можливо розмістити корів з відстанню mid
        if is_possible(mid, arr, k):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


def main():
    k = int(input().split()[1])
    arr = list(map(int, input().split()))
    print(solution(arr, k))


if __name__ == '__main__':
    main()
