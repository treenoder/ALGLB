def evaluate(ex: str) -> int:
    operators = []
    parts = []
    start = 0
    for i, ch in enumerate(ex):
        if ch in ['+', '-']:
            operators.append(ch)
            parts.append(int(ex[start:i]))
            start = i + 1
    parts.append(int(ex[start:]))

    result = parts[0]
    for i, part in enumerate(parts[1:]):
        if operators[i] == '+':
            result += part
        else:
            result -= part

    return result


def solution(ex: str) -> int:
    max_val = float('-inf')
    for i in range(len(ex)):
        new_ex = ex[:i] + ex[i + 1:]
        if not new_ex:
            continue
        evl = evaluate(new_ex)
        max_val = max(max_val, evl)
    return int(max_val)


def main():
    ex = input()
    result = solution(ex.replace(' ', ''))
    print(result)


if __name__ == "__main__":
    main()
