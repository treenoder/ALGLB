from LB4.E_02.main import solution


def test_solution():
    table = [
        ([
             [0, 2, 0, 5, 5],
             [2, 0, 3, 0, 0],
             [0, 3, 0, 2, 2],
             [5, 0, 2, 0, 4],
             [5, 0, 2, 4, 0]
         ], [
             [1, 4],
             [1, 5],
             [3, 5],
             [3, 4],
             [1, 2]
         ])
    ]

    for m, expected in table:
        assert solution(m) == expected
