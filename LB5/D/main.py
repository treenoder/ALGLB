def solution(n, m, arr) -> tuple[int, list[int]]:
    ...


def main():
    import sys
    input = sys.stdin.read
    ...

    count, edges = solution(n, m, arr)
    if not count:
        print('-1')
        return
    print(count)
    for edge in edges:
        print(edge)


if __name__ == '__main__':
    main()
