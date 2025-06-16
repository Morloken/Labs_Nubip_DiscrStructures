import numpy as np

def print_binary_array(array, highlight_bits=[]):# Вивід бінарного масиву
    """Вивести масив бітів, виділяючи червоним задані біти."""
    # Створити масив з кольоровими бітами
    colored_bits = [
        f"\033[91m{bit}\033[0m" if i in highlight_bits else str(bit)
        for i, bit in enumerate(array, start=1)
    ]
    # Вивести масив з кольоровими бітами
    print(" ".join(colored_bits))

def cyclic_shift_right(arr, fixed_bits):
    """Виконати циклічний зсув вправо, зберігаючи нерухомі біти."""
    
    # Отримуємо копію початкового масиву
    new_arr = arr.copy()
    
    # Створюємо новий масив для результату, починаємо з усіх нулів
    result = [0] * 8#  [0] * 8 - створюємо масив з 8 нулями
    
    # Зсув бітів вправо, зберігаючи нерухомі біти
    for i in range(8):
        if (i + 1) in fixed_bits:  # якщо біт нерухомий, залишаємо його без змін
            result[i] = arr[i]
        else:
            prev_index = (i - 1) % 8  # зсув вправо: беремо попередній біт
            while (prev_index + 1) in fixed_bits:  # пропускаємо нерухомі біти
                prev_index = (prev_index - 1) % 8  # зсув вправо, а %8 забезпечує, що індекс не виходить за межі масиву
            result[i] = arr[prev_index]  # записуємо біт у новий масив
    
    return np.array(result, dtype=int)

# --- Перевірка коректності вводу ---
while True:
    try:
        num = int(input("Введіть додатне ціле число: "))  # Користувач вводить число
        if num < 0:  # Перевіряємо, чи воно додатне
            print("Помилка: Число повинно бути додатним. Спробуйте ще раз.")
            continue
        break  # Якщо введення коректне, виходимо з циклу
    except ValueError:  # Якщо введене значення не ціле число
        print("Помилка: Будь ласка, введіть ціле число.")

# Отримуємо число, обмежене 8 бітами
remainder = num % 256  # Відкидаємо зайві біти (якщо число більше 255)
binary_num = bin(remainder)[2:]  # Перетворюємо в бінарний рядок (без префікса "0b")

# Додаємо нулі, щоб отримати рівно 8 біт
binary_num = binary_num.zfill(8)  # Заповнюємо зліва нулями
binary_array = np.array(list(map(int, binary_num)), dtype=int)  # Перетворюємо рядок у масив чисел

# Вивід початкового числа, остачі та масиву
print(f"\nВведене число: {num}")
print(f"Остача (число в межах 8 біт): {remainder}")
print("Початковий бінарний масив (B8):")
print_binary_array(binary_array, highlight_bits=[6, 8])

# Виконуємо циклічний зсув вправо на 1 біт, зберігаючи біти 6 і 8
shifted_binary = cyclic_shift_right(binary_array, fixed_bits=[6, 8])

# Перетворюємо бітовий масив назад у десяткове число
shifted_binary_str = "".join(map(str, shifted_binary))  # Об’єднуємо бітовий масив у рядок
new_number = int(shifted_binary_str, 2)  # Перетворюємо з двійкової системи в десяткову

# Вивід результату після зсуву
print("\nБінарний масив після зсуву:")
print_binary_array(shifted_binary, highlight_bits=[6, 8])
print(f"Число після зсуву: {new_number}")

# Додаємо 200 і перевіряємо, чи число влізе в 8 біт
final_number = new_number + 200

# Визначаємо, який масив потрібен: 8-бітний чи 16-бітний
if final_number > 255:
    binary_final = bin(final_number)[2:].zfill(16)  # Перетворюємо в 16-бітне число,
    # синтаксис: bin(число)[2:].zfill(16) це заповнення нулями зліва до 16 біт

    bit_size = "B16"
else:
    binary_final = bin(final_number)[2:].zfill(8)  # Перетворюємо в 8-бітне число
    bit_size = "B8"

# Перетворюємо рядок у масив чисел
binary_final_array = np.array(list(map(int, binary_final)), dtype=int)

# Вивід фінального числа та бінарного масиву
print(f"\nФінальне число після додавання 200: {final_number}")
print(f"Бінарний масив ({bit_size}):")
print_binary_array(binary_final_array)
