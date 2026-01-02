import random
import matplotlib.pyplot as plt

# Кількість кидків
NUM_ROLLS = 1_000_000

# Словник для підрахунку кожної суми
sum_counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

# Симуляція кидків
for i in range(NUM_ROLLS):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    sum_counts[total] = sum_counts[total] + 1

# Обчислення ймовірностей Монте-Карло
monte_carlo_probs = {}
for sum_value in sum_counts:
    monte_carlo_probs[sum_value] = (sum_counts[sum_value] / NUM_ROLLS) * 100

# Аналітичні ймовірності
analytical_probs = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Виведення таблиці
print("=" * 60)
print(f"{'Сума':<10}{'Монте-Карло':<15}{'Аналітична':<15}{'Різниця':<15}")
print("=" * 60)

for sum_value in range(2, 13):
    mc = monte_carlo_probs[sum_value]
    an = analytical_probs[sum_value]
    diff = mc - an
    print(f"{sum_value:<10}{mc:<15.2f}{an:<15.2f}{diff:<+15.2f}")

print("=" * 60)

# Побудова графіка
sums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

mc_values = []
for s in sums:
    mc_values.append(monte_carlo_probs[s])

an_values = []
for s in sums:
    an_values.append(analytical_probs[s])

plt.figure(figsize=(10, 6))

x_positions = range(len(sums))
width = 0.35

plt.bar([x - width/2 for x in x_positions], mc_values, width, label='Монте-Карло', color='#FFC876')
plt.bar([x + width/2 for x in x_positions], an_values, width, label='Аналітична', color='#C0CCFE')

plt.xlabel('Сума')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.xticks(x_positions, sums)
plt.legend()
plt.grid(True)

plt.savefig('result.png')
print("\nГрафік збережено: result.png")

plt.show()
