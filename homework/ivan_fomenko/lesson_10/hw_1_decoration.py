# Декоратор должен делать следующее:
# распечатывать слово "finished"после выполнения декорированной функции.


def finish_decor(func):
    def wrapper(*args):
        result = func(*args)
        print('Finished')
        return result
    return wrapper


@finish_decor
def simple():
    print('print me')


simple()
