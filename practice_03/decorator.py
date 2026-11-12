def announce(func):
    def wrapper():
        print('Приветствуем')
        return func()
    return wrapper

@announce
def hello():
    print('Привет!')

hello()