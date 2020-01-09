def first_recursion(a, b):
    if b == a:
        return a
    else:
        return (str(first_recursion(a, b-1)) + " " + str(b))

def second_recursion(a, b):
    if a == b:
        return b
    else:
        return (str(a) + " " + str(second_recursion(a-1, b)))

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a < b:
    print(first_recursion(a, b))
elif b < a:
    print(second_recursion(a, b))