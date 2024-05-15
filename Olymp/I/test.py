from Olymp.I.main import solution


def test_solution():
    table = [
        (
            (3, 5, 3),
            [
                ['#', '.', '.', '.', '.'],
                ['#', '#', '#', '#', '.'],
                ['F', 'S', '.', '.', '.'],
            ],
            [
                (1, 1),
                (2, 3),
                (2, 2),
            ],
            17
        ),
    ]

    for (n, m, k), arr, xy, expected in table:
        assert solution(n, m, k, xy, arr) == expected
