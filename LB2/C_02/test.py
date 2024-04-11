from LB2.C_02.main import solution


def test_solution():
    table = [
        ((4, 10.0, 6.0, 1.0, 1, 2, 3), '30.0000'),
    ]

    for (a, b, c, d, e, f, g), r in table:
        assert solution(a, b, c, d, e, f, g) == r
