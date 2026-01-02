items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items: dict, budget: int) -> tuple[list, int]:
    """
    Жадібний підхід: для кожного товару сортуємо відношення калорій/вартості. Найвигідніші стають першими.
    Потім по черзі додаємо вибрані страви до списку, поки хватає бюджету.
    """
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )
    
    selected = []
    total_calories = 0
    
    for name, info in sorted_items:
        if info["cost"] <= budget:
            selected.append(name)
            total_calories += info["calories"]
            budget -= info["cost"]
    
    return selected, total_calories


def dynamic_programming(items: dict, budget: int) -> tuple[list, int]:
    """Динамічне програмування: знаходить оптимальний набір."""
    names = list(items.keys())
    n = len(names)
    
    # Ствоюємо масив колорійності який заповнений нулями
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповлюємо масив значеннями
    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]
        
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if cost <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - cost] + calories)
    
    # Відновлення вибраних страв
    selected = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(names[i - 1])
            w -= items[names[i - 1]]["cost"]
    
    return selected, dp[n][budget]


if __name__ == "__main__":
    budget = 100

    print("Жадібний алгоритм:")
    selected, calories = greedy_algorithm(items, budget)
    print(f"Страви: {selected}")
    print(f"Калорії: {calories}")

    print("\nДинамічне програмування:")
    selected, calories = dynamic_programming(items, budget)
    print(f"Страви: {selected}")
    print(f"Калорії: {calories}")

