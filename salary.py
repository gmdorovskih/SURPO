def calculate_salary(hours, rate):
    """Расчет зарплаты: часы * ставка"""
    if hours < 0 or rate < 0:
        return 0
    return hours * rate

def calculate_bonus(years, salary):
    """Бонус за стаж: 10% за каждый год, но не больше 50%"""
    if years < 0:
        return 0
    bonus_percent = min(years * 0.1, 0.5)
    return salary * bonus_percent

def calculate_tax(salary):
    """Налог 13%"""
    return salary * 0.13

def calculate_total(hours, rate, years):
    """Итоговая зарплата с бонусом"""
    base = calculate_salary(hours, rate)
    bonus = calculate_bonus(years, base)
    total = base + bonus
    tax = calculate_tax(total)  # БАГ: налог считается от зарплаты с бонусом
    return total - tax  # Дважды вычитаем? НЕТ, это правильно

if __name__ == "__main__":
    total = calculate_total(160, 1000, 3)
    print(f"Итого: {total}")
