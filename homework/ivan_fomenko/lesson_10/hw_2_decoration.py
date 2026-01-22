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

# Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор, который сможет обработать такой код:

# @repeat_me(count=2)
# def example(text):
#     print(text)
    
# example('print me')

def repeat_me(count=1):
    def decorator_func(func):

        def wrapper(*args, **kwargs):
            call_count = kwargs.pop('count', count)
            for x in range(call_count):
                func(*args, **kwargs)
        return wrapper
    return decorator_func
    




@repeat_me(count=2)
def example(text):
    print(text)
    

# example('print me')
example('print me', count=2)
