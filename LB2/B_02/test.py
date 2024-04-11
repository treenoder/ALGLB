from LB2.B_02.main import solution


def test_solution():
    table = [
        ((2, 3, 10), 9),
        ((1, 1, 1), 1),
    ]

    for (w, h, n), r in table:
        assert solution(w, h, n) == r
