import sys
from dataclasses import dataclass


@dataclass
class Stack:
    data: list

    def push(self, value):
        self.data.append(value)
        return 'ok'

    def pop(self):
        if not self.data:
            return 'error'
        return self.data.pop()

    def back(self):
        if not self.data:
            return 'error'
        return self.data[-1]

    def clear(self):
        self.data.clear()
        return 'ok'

    def size(self):
        return len(self.data)


def solution(stack, cmd, args):
    return getattr(stack, cmd)(*args)


def main():
    stack = Stack([])
    for line in sys.stdin:
        cmd, *args = line.split()
        if cmd == 'exit':
            print('bye')
            break
        print(solution(stack, cmd, args))


if __name__ == '__main__':
    main()
