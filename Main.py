#3.Створити список з 12 елементів
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(lst)
#4.Добавити в середину списку новий елемент зі значенням 56 ( середина має обчислюватися автоматично )
l = len(lst)
middle = l//2
lst.insert(middle, 56)
print(lst)
#5.Обновити 2й елемент до 25
lst[1] = 25
print(lst)
#6.Додати в кінець списку 88
lst.append(88)
print(lst)
#7.Видалити перший елемент списку
del lst[0]
print(lst)
#8.Видалити остатній елемент списку і вивести в консоль його значення ( для будь якої довжини списка )
tmp = lst.pop(12)
lst[0], lst[1] = lst[1], lst[0]
print(tmp)
#9. Знайти довжину кола і його площу якщо у вас відомий радіус кола. с = 2 * pi * r, s = pi * r ^ 2. Радіус задаєте в коді r = <something>, r - це змінна
import math
r = 7
print('c =', "{0:.2f}".format(math.pi *2 *r))
print('s=', "{0:.2f}".format(math.pi *r**2))


