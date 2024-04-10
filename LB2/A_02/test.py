from LB2.A_02.main import solution


def test_solution():
    table = [
        (3, [1,2,3,100,1000], 99),
    ]

    for k, arr, expected in table:
        assert solution(arr, k) == expected
