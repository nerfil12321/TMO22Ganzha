g = (x + 4 for x in [1,2,3])
print(list(g))

def announce(func):
    def wrapper():
        print('Приветствуем')
        return func()
    return wrapper

@announce
def hello():
    print('Привет!')

hello()