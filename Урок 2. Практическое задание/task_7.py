"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def prof(n=input('Введите число для проверки: '), result=1, step='1'):
    try:
        n = int(n)
        if n == 0:
            print('Введите натуральное число')
            return prof(n=input('Введите число для проверки: '), result=1, step='1')
        if result == n*(n+1)/2:
            return print(f'Проверка выполнена для {step} = {n}({n}+1)/2 \n {result} = {result}')
        result = result + 1
        if result <= n:
            step += f'+{result}'
        return prof(result=result, step=step)
    except ValueError:
        print('Введите натуральное число')
        return prof(n=input('Введите число для проверки: '), result=1, step='1')


prof()
