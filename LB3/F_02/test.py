from LB3.F_02.main import solution


def test_solution():
    table = [
        ([7, 3, 2, 1, 9, 5, 4, 6, 8], '3 5 7'),
        ([2, 1, 3], '2'),
    ]

    for a, expected in table:
        assert solution(a) == expected
