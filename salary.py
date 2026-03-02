def calculate_salary(hours, rate):
    """Расчет зарплаты: часы * ставка"""
<<<<<<< HEAD
    if hours < 0 or rate < 0:
        return 0
=======
>>>>>>> a8bddda (init: базовая зарплата)
    return hours * rate

def calculate_bonus(years, salary):
    """Бонус за стаж: 10% за каждый год, но не больше 50%"""
<<<<<<< HEAD
    if years < 0:
        return 0
    bonus_percent = min(years * 0.1, 0.5)
    return salary * bonus_percent

def calculate_tax(salary):
    """Налог 13%"""
    return salary * 0.13

def calculate_premium(projects):
    """Премия за проекты: 50000 за каждый проект"""
    return projects * 50000

def calculate_total(hours, rate, years, projects):
    """Итоговая зарплата с бонусом и премией"""
    base = calculate_salary(hours, rate)
    bonus = calculate_bonus(years, base)
    premium = calculate_premium(projects)
    total = base + bonus + premium
    tax = calculate_tax(total)
    return total - tax

if __name__ == "__main__":
    total = calculate_total(160, 1000, 3, 2)
    print(f"Итого: {total}")
=======
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
>>>>>>> a8bddda (init: базовая зарплата)
