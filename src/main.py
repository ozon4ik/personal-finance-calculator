from datetime import datetime
import sys

# Глобальный список для хранения операций (в оперативной памяти)
operations = []

def add_operation():
    """Функция для добавления новой операции (доход или расход)."""
    print("\n--- Добавление новой операции ---")
    op_type = input("Введите тип операции (доход/расход): ").strip().lower()
    
    if op_type not in ("доход", "расход"):
        print("❌ Ошибка: тип должен быть 'доход' или 'расход'.")
        return

    try:
        amount = float(input("Введите сумму: "))
        if amount <= 0:
            print("❌ Ошибка: сумма должна быть больше нуля.")
            return
    except ValueError:
        print("❌ Ошибка: сумма должна быть числом.")
        return

    category = input("Введите категорию (например, Зарплата, Еда, Транспорт): ").strip()
    if not category:
        category = "Без категории"

    date_str = input("Введите дату (ГГГГ-ММ-ДД) или нажмите Enter для текущей: ").strip()
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d")
    else:
        # Простая проверка формата даты
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("❌ Ошибка: неверный формат даты. Используйте ГГГГ-ММ-ДД.")
            return

    # Сохраняем операцию в список
    operations.append({
        "type": op_type,
        "amount": amount,
        "category": category,
        "date": date_str
    })
    print("✅ Операция успешно добавлена!")

def show_operations():
    """Функция для вывода списка всех операций."""
    print("\n--- Список всех операций ---")
    if not operations:
        print("Список пуст. Добавьте хотя бы одну операцию.")
        return

    for i, op in enumerate(operations, 1):
        # Определяем знак для красивого вывода
        sign = "+" if op["type"] == "доход" else "-"
        print(f"{i}. [{op['date']}] {sign}{op['amount']:.2f} руб. | Категория: {op['category']}")

def show_balance():
    """Функция для подсчета и вывода текущего баланса."""
    print("\n--- Текущий баланс ---")
    if not operations:
        print("Баланс: 0.00 руб. (Нет операций)")
        return

    total_income = sum(op["amount"] for op in operations if op["type"] == "доход")
    total_expense = sum(op["amount"] for op in operations if op["type"] == "расход")
    balance = total_income - total_expense

    print(f"Общий доход:  +{total_income:.2f} руб.")
    print(f"Общий расход: -{total_expense:.2f} руб.")
    print(f"-----------------------------")
    print(f"Текущий баланс: {balance:.2f} руб.")

def main_menu():
    """Главное меню приложения (интерактивный режим)."""
    while True:
        print("\n=== Калькулятор личных финансов ===")
        print("1. Добавить операцию")
        print("2. Показать все операции")
        print("3. Показать текущий баланс")
        print("0. Выход")
        
        choice = input("Выберите действие (0-3): ").strip()
        
        if choice == "1":
            add_operation()
        elif choice == "2":
            show_operations()
        elif choice == "3":
            show_balance()
        elif choice == "0":
            print("До свидания! Программа завершена.")
            sys.exit(0)
        else:
            print("❌ Неверный ввод. Пожалуйста, выберите пункт из меню.")

if __name__ == "__main__":
    # Точка входа в программу
    main_menu()
