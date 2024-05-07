from LB4.A_02.main import solution


def test_solution():
    table = [
        ([
             [0, 1, 0, 1],
             [1, 0, 0, 1],
             [0, 1, 0, 0],
             [1, 0, 1, 1],
         ], 8),
    ]

    for g, expected in table:
        assert solution(g) == expected
