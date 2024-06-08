import random
from collections import Counter
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_rolls):
    rolls_counter = Counter()
    for _ in range(num_rolls):
        roll_sum = roll_dice() + roll_dice()
        rolls_counter[roll_sum] += 1
    return rolls_counter

def calculate_probabilities(rolls_counter, num_rolls):
    probabilities = {i: rolls_counter[i] / num_rolls * 100 for i in range(2, 13)}
    return probabilities

def print_probabilities(probabilities):
    print("Сума\t Імовірність")
    for sum_val, prob in probabilities.items():
        print(f"{sum_val}\t{prob:.2f}% ({prob/100*num_rolls}/{num_rolls})")

def print_comparison(probabilities, analytical_probabilities):
    print("Сума\t Монте-Карло\t Аналітично")
    for sum_val in range(2, 13):
        print(f"{sum_val}\t{probabilities[sum_val]:.2f}%\t\t{analytical_probabilities[sum_val]:.2f}%")

def plot_probabilities(probabilities, analytical_probabilities):
    plt.bar(probabilities.keys(), probabilities.values(), color='dodgerblue', alpha=0.8, label='Монте-Карло')
    plt.bar(analytical_probabilities.keys(), analytical_probabilities.values(), color='salmon', alpha=0.5, label='Аналітично')
    plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність (%)')
    plt.xticks(range(2, 13))
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main(num_rolls):
    rolls_counter = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probabilities(rolls_counter, num_rolls)
    print_probabilities(probabilities)
    
    # Аналітичні значення ймовірностей
    analytical_probabilities = {
        2: 1/36 * 100, 3: 2/36 * 100, 4: 3/36 * 100, 5: 4/36 * 100,
        6: 5/36 * 100, 7: 6/36 * 100, 8: 5/36 * 100, 9: 4/36 * 100,
        10: 3/36 * 100, 11: 2/36 * 100, 12: 1/36 * 100
    }
    
    print("\n Порівняння з аналітичними значеннями:")
    print_comparison(probabilities, analytical_probabilities)
    
    plot_probabilities(probabilities, analytical_probabilities)

if __name__ == "__main__":
    num_rolls = 1000000  # Задайте кількість кидків кубиків тут
    main(num_rolls)
