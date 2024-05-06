from LB3.D_02.main import solution


def test_solution():
    table = [
        ([1, 2, 3, 4, 3], 3, '1 2 4'),
    ]

    for a, n, expected in table:
        assert solution(a, n) == expected
