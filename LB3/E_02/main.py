# Task: E Обход дерева

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if self.value is None:
            self.value = value
            return
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                return

    def __str__(self):
        result = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            result.append(str(node.value))
            dfs(node.right)

        dfs(self)
        return ' '.join(result)


def solution(arr):
    tree = Node()
    for a in arr:
        tree.add(a)
    return str(tree)


def main():
    print(solution(map(int, input().split()[:-1])))


if __name__ == '__main__':
    main()
