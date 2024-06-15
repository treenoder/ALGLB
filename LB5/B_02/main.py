def solution(n, arr):
    closure = [[arr[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])

    return closure


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

    result = solution(n, arr)
    for i in range(n):
        print(' '.join(map(str, result[i])))


if __name__ == '__main__':
    main()
