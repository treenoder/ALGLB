from LB2.A.main import solution


def test_solution():
    table = [
        ([1, 3, 5], [1, 5, 7], [1, 3, 0]),
        ([1, 1, 3, 3], [1, 3], [2, 4]),
    ]

    for arr, idx, expected in table:
        assert solution(arr, idx) == expected
