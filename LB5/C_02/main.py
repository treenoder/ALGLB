def solution(n, arr) -> tuple[int, list[int]]:
    ...


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    arr = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        arr.append(row)
        index += n

    count, verts = solution(n, arr)
    if not count:
        print('NO')
        return
    print('YES')
    print(count)
    print(' '.join(map(str, verts)))


if __name__ == '__main__':
    main()
