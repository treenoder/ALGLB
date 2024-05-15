from Olymp.J.main import solution


def test_solution():
    table = [
        (4, [93, 31, 23, 31], 2),
        (4, [93, 31, 23, 12], 3),
        (4, [93, 31, 23, 2], -1),
    ]

    for n, arr, expected in table:
        assert solution(n, arr) == expected
