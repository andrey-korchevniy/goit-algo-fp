import random
import matplotlib.pyplot as plt

# Функція для симуляції кидків двох кубиків
def simulate_dice_throws(num_throws):
    results = [0] * 13  # Індекси від 0 до 12 (використовуватимемо тільки 2-12)

    for _ in range(num_throws):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum_dice = dice1 + dice2
        results[sum_dice] += 1

    probabilities = [result / num_throws for result in results[2:]]  # Ймовірності для сум від 2 до 12
    return probabilities

# Симуляція кидків
num_throws = 1000000
probabilities = simulate_dice_throws(num_throws)

# Відображення результатів
sums = list(range(2, 13))
plt.bar(sums, probabilities, tick_label=sums)
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум чисел на двох кубиках (Метод Монте-Карло)')
plt.grid(True)
plt.show()

# Виведення результатів у вигляді таблиці
print("Сума\tЙмовірність")
for sum_, prob in zip(sums, probabilities):
    print(f"{sum_}\t{prob:.4f}")