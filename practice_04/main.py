print('Задание 1')
x = 14

def show():
    x = 4
    print(x)

show()
print(x)

# В функции show() используется локальная переменная х = 4, которая создается в момент вызова функции
# К глобальной переменной х = 14, которую мы создали до функции, локальная не имеет никакого отношения
# В функции манипуляции происходят именно с созданной переменной х = 4, поэтому глобальная переменная х = 14 остается неизменной


print('Задание 2')

def total(*args):
    return sum(args)

print(total(4, 5, 6))


print('Задание 3')

def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name = "Ира", age = 20))


print('Задание 4')

def increase(x):
    return x + 4

def apply(func, value):
    return func(value)

print(apply(increase, 5))


print('Задание 5')

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)