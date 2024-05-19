def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості у спадаючому порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if info['cost'] <= budget:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)

    return total_calories, selected_items

def dynamic_programming(items, budget):
    n = len(items)
    items_list = list(items.items())

    # Створюємо таблицю dp, де dp[i][w] - максимальна кількість калорій з використанням перших i страв та бюджету w
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        name, info = items_list[i - 1]
        cost = info['cost']
        calories = info['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Визначаємо набір вибраних страв
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items_list[i - 1][0])
            w -= items_list[i - 1][1]['cost']

    return dp[n][budget], selected_items

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Жадібний алгоритм
greedy_calories, greedy_items = greedy_algorithm(items, budget)
print(f"\nЖадібний алгоритм: \nВсього калорій = {greedy_calories}, \nОбрано: {greedy_items}")

# Динамічне програмування
dp_calories, dp_items = dynamic_programming(items, budget)
print(f"\nДинамічне програмування: \nВсього калорій = {dp_calories}, \nОбрано: {dp_items}")