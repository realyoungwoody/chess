try:
    first = int(input("Введите первое число: "))    #str
    second = int(input("Введите второе число: "))   #stolb
    third = int(input("Введите третье число: "))   #str
    forth = int(input("Введите четвёртое число: "))   #stolb
except ValueError:
    print("Походу кошка по клавиатуре пробежала")
    
num1 = (first % 2)      #нечетное
num2 = (second % 2)     #нечетное
black_1 = num1 + num2      #четное=нечетное+нечетное
num3 = (third % 2)      #нечетное
num4 = (forth % 2)      #нечетное
black_2 = num3 + num4

if (black_1 == black_2) | ((first + second) % 2 == 0) | ((third + forth) % 2 == 0):
        print("Клетки покрашены в один цвет")
else:
        print("Клетки покрашены в разные цвета")
