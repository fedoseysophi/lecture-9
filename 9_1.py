import time

def time_of_function(function):
    def wrapper(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(time.perf_counter() - start_time)
        return res
    return wrapper

@time_of_function
def func(first, second):
    return bin(int(first, 2) + int(second, 2))

print(func("111", "1100111001011"))