def solution(ex: str) -> int:
    max_val = float('-inf')
    for i in range(len(ex)):
        if ex[i + 1:].startswith(ex[i]):
            continue
        new_ex = ex[:i] + ex[i + 1:]
        if not new_ex:
            continue
        try:
            evl = eval(new_ex)
        except Exception:
            continue
        max_val = max(max_val, evl)
    return int(max_val)


def main():
    ex = input()
    result = solution(ex.replace(' ', ''))
    print(result)


if __name__ == "__main__":
    main()
