from LB4.D_02.main import solution


def test_solution():
    table = [
        (3, 3, [
            [1, 2],
            [1, 3],
            [2, 3],
        ], 'YES'),
        (3, 2, [
            [1, 2],
            [2, 3],
        ], 'NO'),
    ]

    for v, e, m, expected in table:
        assert solution(v, e, m) == expected
