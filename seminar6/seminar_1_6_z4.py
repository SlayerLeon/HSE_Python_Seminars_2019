# Задача 4
# Товары и стоимость представлены кортежами данных, например, (‘хлеб’, 23) и т.д.
# Окончание ввода “0” в товаре или стоимости. Необходимо рассчитать общую стоимость товара “молоко”.

goods = tuple() # объявление пустого кортежа
sum = 0
while not ('0' in goods):
   goods = (input("Введите название товара: "), input("Введите сумму:"))
   if (not goods[1].isdigit()):
       print ("Надо ввести сумму цифрами, повторите.")
       continue
   print(goods)
   name, val = goods
   if (name == "молоко"):
      sum += int(val)
print("Всего товара 'молоко': ", sum)