# Проект FitLife - MVP версия 1.0

# Константы
WATER_NORM = 0.03

user_name = str(input('Добро пожаловать в FitLife! Назовите свое имя: '))
while True:
    try:
        user_age = int(input('Назовите свой возраст (полных лет): '))
        break
    except ValueError:
        print('Попробуйте еще раз. Введите целое число')


while True:
    try:
        user_weight = float(input('Введите свой вес (в кг): '))
        break
    except ValueError:
        print('Попробуйте еще раз. При вводе используйте точку, например 55.5')
while True:
    try:
        user_height = float(input('Введите свой рост (в м): '))
        break
    except ValueError:
        print('Попробуйте еще раз. При вводе используйте точку, например 1.75')


# Расчет ИМТ и суточной нормы воды
bmi = round((user_weight / (user_height ** 2)), 1)
water_needed = user_weight * WATER_NORM


print(f"Привет, {user_name}!")
print(f"Отчет для пользователя: {user_name}, ({user_age} г.)")
print(f"Ваш Индекс Массы Тела (ИМТ): {bmi}")
print(f"Ваша рекомендуемая норма воды: {water_needed:.1f} л в день")
print("Расчет окончен. Будьте здоровы!")
