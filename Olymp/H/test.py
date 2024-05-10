from Olymp.H.main import solution


def test_solution():
    table = [
        (5, [1, 2, 3, 5, 9], 1),
        (5, [4, 8, 9, 7, 10], 0)
    ]

    for n, arr, expected in table:
        assert solution(n, arr) == expected
