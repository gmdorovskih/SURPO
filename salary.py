def calculate_salary(hours, rate):
    """Расчет зарплаты: часы * ставка"""
    return hours * rate

def calculate_bonus(years, salary):
    """Бонус за стаж: 10% за каждый год, но не больше 50%"""
    bonus_percent = min(years * 0.1, 0.5)
    return salary * bonus_percent

def calculate_total(hours, rate, years):
    """Итоговая зарплата с бонусом"""
    base = calculate_salary(hours, rate)
    bonus = calculate_bonus(years, base)
    return base + bonus

if __name__ == "__main__":
    # Тест: 160 часов * 1000 = 160000, стаж 3 года = 30% бонус = 48000
    total = calculate_total(160, 1000, 3)
    print(f"Итого: {total}")
    # Должно быть: 160000 + 48000 = 208000
