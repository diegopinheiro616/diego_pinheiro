# Python Decorator Function
"""
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")


# say_hello()
# Hello
# Hello

decorated_function = delay_decorator(say_greeting)
decorated_function()
# How are you?
# How are you?
"""
# ### EXERCISE #####

import time
current_time = time.time()
print(current_time)  # 1643812087.1270638


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed:{end_time - start_time}s")
    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()  # fast_function run speed:0.6645872592926025s

slow_function()  # slow_function run speed:6.628876209259033s
