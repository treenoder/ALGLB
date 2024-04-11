from LB2.D_02.main import solution


def test_solution():
    records = [
        [10, 20, 30],
        [11, 19, 50],
        [13, 15, 40]
    ]
    queries = [
        (2, 2),
        (1, 1),
        (1, 3)
    ]
    expected_results = [
        [11, 19, 50],
        [13, 15, 40],
        [11, 19, 50]
    ]

    assert solution(records, queries) == expected_results

