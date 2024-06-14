def reverse_merge_sort(arr, start, end, di):
    """
    Виконує зворотнє сортування злиттям масиву за заданим індексом di.

    Складність: O(n * log(n)), де n - кількість елементів у масиві.
    """
    if start >= end:
        return

    mid = start + (end - start) // 2

    # Рекурсивно сортуємо ліву та праву половини масиву
    reverse_merge_sort(arr, start, mid, di)
    reverse_merge_sort(arr, mid + 1, end, di)

    # Злиття двох відсортованих половин
    i, j = start, mid + 1
    temp = []
    while i <= mid and j <= end:
        # Додаємо більший елемент з двох половин у тимчасовий масив
        if arr[i][di] >= arr[j][di]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # Додаємо залишкові елементи з лівої половини
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # Додаємо залишкові елементи з правої половини
    while j <= end:
        temp.append(arr[j])
        j += 1

    # Копіюємо відсортовані елементи назад у вихідний масив
    for i in range(len(temp)):
        arr[start + i] = temp[i]


def solution(records, queries):
    """
    Знаходить i-й за рахунком запис у базі даних після сортування за спаданням за j-м елементом.

    Складність: O(m * n * log(n)), де n - кількість записів у базі даних, m - кількість запитів.
    """
    results = []

    for ci, di in queries:
        # Сортуємо записи за заданим індексом di (після перетворення на 0-індексацію)
        reverse_merge_sort(records, 0, len(records) - 1, di - 1)

        # Додаємо ci-й за рахунком запис у результати (після перетворення на 0-індексацію)
        results.append(records[ci - 1])

    return results


def main():
    N, M = map(int, input().split())

    records = [list(map(int, input().split())) for _ in range(N)]

    K = int(input())

    queries = [tuple(map(int, input().split())) for _ in range(K)]

    results = solution(records, queries)
    for result in results:
        print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
