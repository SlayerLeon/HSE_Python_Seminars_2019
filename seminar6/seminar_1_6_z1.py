# Задача1
# Проверьте, для целых чиcел в пределах [0, 100] является ли пара (x, y) корнями уравнения:
# x * x - x * y - 4 = 0

for i in range(0, 101):
   for j in range(0, 101):
       if i * i - i * j - 4 == 0:
           print("Найден корень (", i, ",", j, ")", sep='')
