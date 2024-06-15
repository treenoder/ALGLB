import sys


def compare(x, y):
    return int(y + x) - int(x + y)


def bubble_sort(arr, cmp):
    """
    Виконує сортування бульбашковим методом для заданого списку рядків чисел з використанням
    заданої функції порівняння.
    Складність: O(n^2)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cmp(arr[j], arr[j + 1]) > 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def solution(arr):
    sorted_arr = bubble_sort(arr, compare)
    return ''.join(sorted_arr)


def main():
    arr = []
    for line in sys.stdin:
        if line.strip() == '':
            break
        arr.append(line.strip())
    print(solution(arr))


if __name__ == '__main__':
    main()
