def solution(w, h, n):
    def can_fit(size):
        return (size // w) * (size // h) >= n

    left, right = 0, max(w, h) * n
    while left < right:
        mid = (left + right) // 2
        if can_fit(mid):
            right = mid
        else:
            left = mid + 1
    return left


def main():
    w, h, n = tuple(map(int, input().split()))
    print(solution(w, h, n))


if __name__ == '__main__':
    main()

