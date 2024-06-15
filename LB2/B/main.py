def solution(p, q):
    passengers_indices = {}
    for idx, count in enumerate(p):
        if count not in passengers_indices:
            passengers_indices[count] = []
        passengers_indices[count].append(idx + 1)  # Use 1-based indexing

    def binary_search(indices, low, high):
        left, right = 0, len(indices) - 1
        while left <= right:
            mid = (left + right) // 2
            if low <= indices[mid] <= high:
                return True
            elif indices[mid] < low:
                left = mid + 1
            else:
                right = mid - 1
        return False

    results = []
    for l, r, x in q:
        if x not in passengers_indices:
            results.append('0')
        else:
            indices = passengers_indices[x]
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
