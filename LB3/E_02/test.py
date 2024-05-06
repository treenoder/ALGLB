from LB3.E_02.main import solution


def test_solution():
    table = [
        ([7, 3, 2, 1, 9, 5, 4, 6, 8], '1 2 3 4 5 6 7 8 9'),
        ([1, 2, 1], '1 2'),
        ([5, 5, 1, 4, 3, 1, 2, 1, 6, 1], '1 2 3 4 5 6'),
    ]

    for a, expected in table:
        assert solution(a) == expected
