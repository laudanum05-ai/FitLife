# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = str(input('Добро пожаловать в FitLife! Назовите свое имя: '))
user_age = int(input('Назовите свой возраст (полных лет): '))


# 2. Сбор данных
user_weight = float(input('Введите свой вес (в кг), например 55.5: '))
user_height = float(input('Введите свой рост (в м), например 1.75: '))


# 3. Логика расчетов
# Расчет ИМТ
bmi = round((user_weight / (user_height ** 2)), 1)


# Расчет нормы воды в литрах
# Норма воды 30 мл на кг или 0.03 л/кг
WATER_NORM = 0.03
water_needed = user_weight * WATER_NORM


# 4. Вывод красивого результата
print(f"Привет, {user_name.title()}!")
print(f"Отчет для пользователя: {user_name.title()}, ({user_age} г.)")
print(f"Ваш Индекс Массы Тела (ИМТ): {bmi}")
print(f"Ваша рекомендуемая норма воды: {water_needed:.1f} л в день")
print("Расчет окончен. Будьте здоровы!")
