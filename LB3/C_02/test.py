from LB3.C_02.main import solution


def test_solution():
    table = [
        (3, [
            ['Hello', 'Hi'],
            ['Bye', 'Goodbye'],
            ['List', 'Array'],
        ], 'Goodbye', 'Bye'),
        (3, [
            ['Hello', 'Hi'],
            ['Bye', 'Goodbye'],
            ['List', 'Array'],
        ], 'List', 'Array'),
        (3, [
            ['Hello', 'Hi'],
            ['Bye', 'Goodbye'],
            ['List', 'Array'],
        ], 'Hi', 'Hello'),
    ]

    for n, words, query, expected in table:
        assert solution(n, words, query) == expected
