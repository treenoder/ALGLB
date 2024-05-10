def solution(ex: str) -> int:
    ex_evals = []
    for i in range(len(ex) - 2):
        new_ex = ex[:i + 1] + ex[i + 2:]
        evl = eval(new_ex.replace(' ', ''))
        ex_evals.append(evl)
    return max(ex_evals)


def main():
    ex = input()
    result = solution(ex)
    print(result)


if __name__ == "__main__":
    main()
