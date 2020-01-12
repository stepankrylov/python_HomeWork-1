# 1-е задание
long_phrase = 'Насколько проще было бы писать программы, если бы не заказчики'
short_phrase = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
print(len(long_phrase)>len(short_phrase))

# 2-е задание
x = 100000
y = x/10**6
print('Объем файла равен ', y, ' Mb')

# 3-е задание
Jan = 'январь'
Feb = 'февраль'
Mar = 'март'
Apr = 'апрель'
May = 'май'
Jun = 'июнь'
Jul = 'июль'
Aug = 'август'
Sen = 'сентябрь'
Oct = 'октябрь'
Nov = 'ноябрь'
Dec = 'декабрь'

mounth = str(input('Введите месяц Вашего рождения: '))
day = int(input('Введите день Вашего рождения: '))

if mounth == Dec and day >= 22 and day <= 31 or mounth == Jan and day >= 1 and day <= 19:
  print('Ваш знак зодиака - Козерог')
elif mounth == Jan and day >= 20 and day <= 31 or mounth == Feb and day >= 1 and day <= 19:
  print('Ваш знак зодиака - Водолей')
elif mounth == Feb and day >= 21 and day <= 29 or mounth == Mar and day >= 1 and day <= 21:
  print('Ваш знак зодиака - Рыбы')
elif mounth == Mar and day >= 22 and day <= 31 or mounth == Apr and day >= 1 and day <= 21:
  print('Ваш знак зодиака - Овен')
elif mounth == Apr and day >= 22 and day <= 30 or mounth == May and day >= 1 and day <= 21:
  print('Ваш знак зодиака - Телец')
elif mounth == May and day >= 22 and day <= 31 or mounth == Jun and day >= 1 and day <= 21:
  print('Ваш знак зодиака - Близнецы')
elif mounth == Jun and day >= 22 and day <= 30 or mounth == Jul and day >= 1 and day <= 21:
  print('Ваш знак зодиака - Рак')
elif mounth == Jul and day >= 22 and day <= 31 or mounth == Aug and day >= 1 and day <= 21:
  print('Ваш знак зодиака - Лев')
elif mounth == Aug and day >= 22 and day <= 31 or mounth == Sen and day >= 1 and day <= 21:
  print('Ваш знак зодиака - Дева')
elif mounth == Sen and day >= 22 and day <= 30 or mounth == Oct and day >= 1 and day <= 21:
  print('Ваш знак зодиака - Весы')
elif mounth == Oct and day >= 22 and day <= 31 or mounth == Nov and day >= 1 and day <= 20:
  print('Ваш знак зодиака - Скорпион')
elif mounth == Nov and day >= 21 and day <= 30 or mounth == Dec and day >= 1 and day <= 21:
  print('Ваш знак зодиака - Стрелец')
else:
 raise SystemExit('Некорректная запись месяца или дня рождения. Пожалуйста, начните заново')

# 4-е задание
wages = int(input('Ваша заработная плата '))*12
the_percentage_of_life = int(input('Процент на жизнь '))/100
the_interest_on_the_mortgage = int(input('Процент на ипотеку '))/100
annual_bonus = int(input('Кол-во годовых премий '))
bonus = wages/12
vacation = annual_bonus*bonus/2
the_cost_of_the_mortgage = wages*the_interest_on_the_mortgage
print('Расходы на ипотеку ', the_cost_of_the_mortgage)
the_cost_of_living = wages*the_percentage_of_life
print('Расходы на жизнь ', the_cost_of_living)
capital = wages+annual_bonus*bonus-vacation-the_cost_of_the_mortgage-the_cost_of_living
print('Накопления за год ', capital)

