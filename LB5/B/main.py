def solution(n, arr) -> list:
    ...


def main():
    import sys
    input = sys.stdin.read
    ...
    result = solution(n, arr)
    for i in range(n):
        print(' '.join(map(str, result[i])))


if __name__ == '__main__':
    main()
