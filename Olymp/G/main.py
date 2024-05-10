def solution(ex: str) -> int:
    max_val = float('-inf')
    for i in range(len(ex)):
        new_ex = ex[:i] + ex[i + 1:]
        if not new_ex:
            continue
        try:
            evl = compile(new_ex, '<string>', 'eval')
            evl = eval(evl)
            max_val = max(max_val, evl)
        except Exception:
            continue
    return int(max_val)


def main():
    ex = input()
    result = solution(ex.replace(' ', ''))
    print(result)


if __name__ == "__main__":
    main()
