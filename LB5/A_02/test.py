from LB5.A_02.main import solution


def test_solution():
    table = [
        ([1, 10, 2, 15], [
            [1, 2],
            [1, 3],
            [4, 2],
            [4, 2],
        ], 2)
    ]

    for costs, roads, expected in table:
        assert solution(costs, roads) == expected
