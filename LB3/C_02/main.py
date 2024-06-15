class Synonyms:
    def __init__(self, size: int):
        self.size = size
        self.left_map = [None] * self.size
        self.right_map = [None] * self.size

    def _get_hash(self, key):
        return hash(key) % self.size

    def add(self, w1, w2):
        self._add(self.left_map, w1, w2)
        self._add(self.right_map, w2, w1)

    def _add(self, m: list, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if m[key_hash] is None:
            m[key_hash] = [key_value]
        else:
            for pair in m[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return
            m[key_hash].append(key_value)

    def get(self, key):
        return self._get(self.left_map, key) or self._get(self.right_map, key)

    def _get(self, m: list, key):
        key_hash = self._get_hash(key)
        if m[key_hash] is not None:
            for pair in m[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


def solution(n, words, query):
    synonyms = Synonyms(n)
    for word, syn in words:
        synonyms.add(word, syn)
    return synonyms.get(query)


def main():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().split())
    query = input()
    print(solution(n, words, query))


if __name__ == '__main__':
    main()
