# Задача2
# Для заданного пользователем натурального n вывести значение числа Пи, вычисленное по формуле Лейбница:
# 4 * (1/1 - 1/3 + 1/5 - 1/7 +...) = Pi

# todo: проверка входных данных
n = int(input("Введите количество членов ряда: "))
sign = 1
pi = 0
for i in range(1, n + 1, 2):
   pi += sign * 1 / i
   sign = -sign
pi *= 4
print("Pi =", pi)