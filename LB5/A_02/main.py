import heapq


def solution(n, costs, roads):
    """
    Знаходить мінімальну вартість маршруту з першого міста в N-й місто, враховуючи витрати на бензин і можливість заправки з каністри.

    Аргументи:
    n (int): Кількість міст.
    costs (list[int]): Вартість заправки одного бака бензину в кожному місті.
    roads (list[tuple[int, int]]): Список доріг, де кожна дорога задається парою міст (a, b).

    Повертає:
    int: Мінімальна вартість маршруту або -1, якщо добратися неможливо.
    """
    # Створення графу у вигляді списку суміжності
    graph = [[] for _ in range(n)]
    for a, b in roads:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # Пріоритетна черга для зберігання поточної мінімальної вартості маршруту
    pq = [(costs[0], 0, 1, 0)]
    dist = {}

    while pq:
        # Витягуємо елемент з мінімальною вартістю
        total_cost, u, fuel_in_tank, fuel_in_jerry_can = heapq.heappop(pq)

        # Якщо досягли останнього міста, повертаємо загальну вартість
        if u == n - 1:
            return total_cost

        # Перевірка, чи вже відвідували цей стан з меншою вартістю
        if (u, fuel_in_tank, fuel_in_jerry_can) in dist and dist[(u, fuel_in_tank, fuel_in_jerry_can)] <= total_cost:
            continue

        dist[(u, fuel_in_tank, fuel_in_jerry_can)] = total_cost

        # Обробка всіх сусідів поточного міста
        for v in graph[u]:
            if fuel_in_tank > 0:
                # Перехід до сусіднього міста з витратою одного бака бензину
                new_total_cost = total_cost
                new_fuel_in_tank = fuel_in_tank - 1
                new_fuel_in_jerry_can = fuel_in_jerry_can
                if (v, new_fuel_in_tank, new_fuel_in_jerry_can) not in dist or new_total_cost < dist[
                    (v, new_fuel_in_tank, new_fuel_in_jerry_can)]:
                    heapq.heappush(pq, (new_total_cost, v, new_fuel_in_tank, new_fuel_in_jerry_can))

            if fuel_in_jerry_can > 0:
                # Перехід до сусіднього міста з витратою одного бака з каністри
                new_total_cost = total_cost
                new_fuel_in_tank = 0
                new_fuel_in_jerry_can = fuel_in_jerry_can - 1
                if (v, new_fuel_in_tank, new_fuel_in_jerry_can) not in dist or new_total_cost < dist[
                    (v, new_fuel_in_tank, new_fuel_in_jerry_can)]:
                    heapq.heappush(pq, (new_total_cost, v, new_fuel_in_tank, new_fuel_in_jerry_can))

            # Заправка одного бака бензину в поточному місті
            new_total_cost = total_cost + costs[u]
            new_fuel_in_tank = 1
            new_fuel_in_jerry_can = fuel_in_jerry_can
            if (u, new_fuel_in_tank, new_fuel_in_jerry_can) not in dist or new_total_cost < dist[
                (u, new_fuel_in_tank, new_fuel_in_jerry_can)]:
                heapq.heappush(pq, (new_total_cost, u, new_fuel_in_tank, new_fuel_in_jerry_can))

            # Заправка одного бака бензину в каністру в поточному місті
            new_total_cost = total_cost + costs[u]
            new_fuel_in_tank = fuel_in_tank
            new_fuel_in_jerry_can = 1
            if (u, new_fuel_in_tank, new_fuel_in_jerry_can) not in dist or new_total_cost < dist[
                (u, new_fuel_in_tank, new_fuel_in_jerry_can)]:
                heapq.heappush(pq, (new_total_cost, u, new_fuel_in_tank, new_fuel_in_jerry_can))

    # Якщо не вдалося дістатися останнього міста, повертаємо -1
    return -1


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0

    n = int(data[idx])
    idx += 1
    costs = list(map(int, data[idx:idx + n]))
    idx += n

    m = int(data[idx])
    idx += 1
    roads = []
    for _ in range(m):
        a = int(data[idx])
        b = int(data[idx + 1])
        roads.append((a, b))
        idx += 2

    result = solution(n, costs, roads)
    print(result)


if __name__ == '__main__':
    main()

"""
1. Створення графу: Ініціюється граф як список суміжності, де кожен список відповідає місту та містить індекси сусідніх міст.

2. Ініціалізація: 
   - Встановлюється пріоритетна черга, де перший елемент – це початкове місто з вартістю заправки в цьому місті, із заправленим баком та порожньою каністрою.
   - Визначається словник `dist` для зберігання мінімальних вартостей досягнення станів (місто, паливо в баку, паливо в каністрі).

3. Основний цикл обробки черги:
   - Доки черга не порожня, обробляється кожен стан (вузол міста).
   - Якщо поточний місто є кінцевим містом, алгоритм повертає загальну вартість досягнення цього міста.
   - Якщо поточний стан вже відвідувався з меншою або рівною вартістю, пропускаємо його.
   - Записується вартість стану в словник `dist`.

4. Обробка сусідніх міст:
   - Переміщення з витратою палива з баку: Якщо в баку є паливо, переходимо в сусіднє місто з витратою однієї одиниці палива.
   - Переміщення з витратою палива з каністри: Якщо в каністрі є паливо, переходимо в сусіднє місто, витрачаючи паливо з каністри, і бак стає порожнім.
   - Заправка баку в поточному місті: Збільшуємо вартість на ціну палива в цьому місті та збільшуємо запас палива в баку.
   - Заправка каністри в поточному місті: Збільшуємо вартість на ціну палива, але збільшуємо запас палива в каністрі.

5. Кінець: Якщо після обробки всіх можливих станів алгоритм не знайшов шляху до останнього міста, повертається `-1`.
"""
