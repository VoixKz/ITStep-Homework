import time

def calc_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec = end - start
        print(f"Время выполнения: {exec} секунд")
        return result
    return wrapper

@calc_time
def some_func():
    time.sleep(4)
    return "Hello, World!"

print(some_func())