def solution(n, arr) -> list:
    dist = [row[:] for row in arr]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


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
