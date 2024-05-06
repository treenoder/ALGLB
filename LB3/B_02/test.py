from LB3.B_02.main import solution, Queue


def test_solution():
    table = [
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 0], 'Igor 5'),
        ([2, 4, 6, 8, 0], [1, 3, 5, 7, 9], 'Artur 5'),
    ]

    for a1, a2, expected in table:
        p1, p2 = Queue(a1), Queue(a2)
        assert solution(p1, p2) == expected
