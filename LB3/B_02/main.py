from dataclasses import dataclass


@dataclass
class Queue:
    data: list

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.data:
            return None
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)


def solution(player1: Queue, player2: Queue):
    """
    Реалізує гру "П'яниця" між двома гравцями, використовуючи черги для представлення колод карт кожного гравця.

    Параметри:
    player1 Черга, яка представляє колоду карт першого гравця (Артура).
    player2 Черга, яка представляє колоду карт другого гравця (Ігоря).

    Повертає:
    Результат гри - ім'я переможця ("Artur" або "Igor") та кількість ходів до перемоги,
         або "Botva", якщо гра не закінчується протягом 10^6 ходів.
    """
    moves = 0
    while len(player1) and len(player2):
        moves += 1
        if moves > 10E6:
            return 'Botva'
        card1 = player1.dequeue()
        card2 = player2.dequeue()
        if card2 - card1 == 9 or (card1 > card2 and card1 - card2 != 9):
            player1.enqueue(card1)
            player1.enqueue(card2)
        else:
            player2.enqueue(card1)
            player2.enqueue(card2)
    if len(player1):
        return f'Artur {moves}'
    return f'Igor {moves}'


def main():
    player1 = Queue(list(map(int, input().split())))
    player2 = Queue(list(map(int, input().split())))
    print(solution(player1, player2))


if __name__ == '__main__':
    main()
