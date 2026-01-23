# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция

# Код, использующий этот декоратор может выглядеть, например, так:

# @repeat_me
# def example(text):
#     print(text)

# example('print me', count=2)
# В результате работы будет такое:

# print me

# print me

# создать декоратор, который сможет обработать такой код:

# @repeat_me(count=2)
# def example(text):
#     print(text)

# example('print me')


def repeat_me(count=1):
    # сюда приходит count из декоратора
    # если count не передан, то = 1

    def decorator_func(func):
        # фактически декоратор сам
        # func это декорируемая функция

        def wrapper(*args, **kwargs):
            # вызываем wrapper вместо нашей example функции
            # args - позиционные аргументы, типа text
            # kwargs - именнованные аргументы типа count

            # Берём count:
            # 1) если count передали при вызове example(..., count=2), то берём его
            # 2) если не передали, то используем count из декоратора
            # pop нужен, чтобы удалить count из kwargs,
            # иначе func() получит лишний аргумент и упадёт
            call_count = kwargs.pop('count', count)

            # Запускаем функцию нужно кол-во раз
            for x in range(call_count):
                func(*args, **kwargs)
        return wrapper
    return decorator_func


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
example('print me', count=2)
