def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорійність/вартість в порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, properties in sorted_items:
        if total_cost + properties['cost'] <= budget:
            total_cost += properties['cost']
            total_calories += properties['calories']
            selected_items.append(item)
    
    return selected_items, total_calories


def dynamic_programming(items, budget):
    # Створюємо матрицю для зберігання результатів
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    
    for i, (item, properties) in enumerate(items.items(), start=1):
        cost = properties['cost']
        calories = properties['calories']
        for j in range(1, budget + 1):
            if cost > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + calories)
    
    # Відновлюємо набір страв
    selected_items = []
    j = budget
    for i in range(len(items), 0, -1):
        if dp[i][j] != dp[i-1][j]:
            selected_items.append(list(items.keys())[i-1])
            j -= items[selected_items[-1]]['cost']
    
    return selected_items, dp[-1][-1]


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    budget = 100
    
    greedy_items, greedy_calories = greedy_algorithm(items, budget)
    dynamic_items, dynamic_calories = dynamic_programming(items, budget)
    
    print("Greedy Algorithm:")
    print("Selected items:", greedy_items)
    print("Total calories:", greedy_calories)
    
    print("\nDynamic Programming:")
    print("Selected items:", dynamic_items)
    print("Total calories:", dynamic_calories)
