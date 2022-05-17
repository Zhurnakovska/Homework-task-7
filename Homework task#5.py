# Написати функції:
# 1. Примає радіус кола, повертає довжину кола. Обробити випадки коли в радіус приходить не числом.
import math
while True:
    r = input("Please input radius in number ")
    try:
        val = int(r)
        break;
    except ValueError:
        try:
            float(r)
            break;
        except ValueError:
            print("This is not a number. Please input radius as a number")
def f(r):
    return math.pi * float(r) * 2

print('c =', "{0:.2f}".format(f(r)))

# 2. Примає радіус кола, повертає площу кола. Обробити випадки коли в радіус приходить не числом.
import math
while True:
    r = input("Please input radius in number ")
    try:
        val = int(r)
        break;
    except ValueError:
        try:
            float(r)
            break;
        except ValueError:
            print("This is not a number. Please input radius as a number")
def f(r):
    return math.pi * float(r) ** 2
print('s =', "{0:.2f}".format(f(r)))

# 3. Приймає число, повертає чи є число поліндромом. Тобто з права на ліво і з ліва на право читається однаково. 12321 - це поліндром, 1234 - не поліндром.
num = input("Please enter number")
def f(num):
        if num == num[::-1]:
            return True
        else:
            return False
print(f(num))

# 4. Функція приймає число n яке більше 0. За допомогою рекурсії виводить всі числа що менші n але більші 0.
def f(n):
    if n > 0:
        if n ==1:
            return 1
        print(n)
        return f(n-1)
    else:
        return f"{n} - doesn't catch condition of fuction"
print(f(-2))
print(f(10))
print(f(5))

# 5. Написати функцію lambda що приймає x i y, а повертає x^2 + y^2
f = lambda x, y: x**2+y**2
print(f(10,12))
# 6. Написати функцію lambda що приймає слово і повертає його довжину.
lst=["hometown"]
i=0
a=lst[i]
f=lambda a:len(a)
print(len(a))

# 6. Написати функцію lambda що приймає слово і повертає його довжину.(вариант№2)
a = input("Please enter word: ")
f=lambda a:len(a)
print(len(a))

# 7. Написати map що перетворює всі числа в списку на строку.
a = [34, 89, 67, 56, 10]
b = list(map(str, a))
print(b)

# 8. Написати filter що залишає в списку тільки числа > 10
lst = [3, 89, 90, 56, 4, 10, 45, 93, 2]
def is_even(n):
    if n > 10:
        return n
lst = list(filter(is_even, lst))
print(lst)

# 9. Є список слів, за допомогою map видалити з кожного слова всі букви "а" (abcd -> bcd ) (з lambda ) ( підказка: викорисати метот replace )
lst=["apple", "cat", "homework", "brand", "town", "car"]
i=0
n = str(lst[i])
f=lambda n: n.replace('a','')
lst = list(map(f, lst))
print(lst)

# 9. Є список слів, за допомогою map видалити з кожного слова всі букви "а" (abcd -> bcd ) (без lambda )
lst=["apple", "cat", "homework", "brand", "town", "car"]
i=0
n = str(lst[i])
def f(n):
    return n.replace('a','')
lst = list(map(f, lst))
print(lst)

# 10. Є список слів, за допомогою filter залишити тільки ті слова в яких к-ть букв більша ніж 4.
lst=["apple", "cat", "homework", "brand", "town", "car"]
i = 0
n = lst[i]
def f(n):
    if len(n) > 4:
        return n
lst = list(filter(f, lst))
print(lst)

# 10. Є список слів, за допомогою filter залишити тільки ті слова в яких к-ть букв більша ніж 4. (способ з lambda)
lst=["apple", "cat", "homework", "brand", "town", "car"]
i=0
n= lst[i]
f=lambda n:len(n)>4
lst = list(filter(f, lst))
print(lst)