# Decorators are going to be explained in this file;

# How can you calculate the time of execution of a function;

# import time


# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Time of execution for {func.__name__} >>> {end_time - start_time}")
#         return result

#     return wrapper


# @timer
# def example_function(n):
#     time.sleep(n)


# example_function(2)

# Correct way!
# fn = timer(example_function)
# fn(2)


# Question 2: Make a decorator debug to print fuction name and all of its arguments


# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f"Funtion name is {func.__name__}")
#         print(f"Args are >> {args}")
#         print(f"KWArgs are >> {kwargs}")
#         result = func(*args, **kwargs)
#         return result

#     return wrapper


# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f"Funtion name is {func.__name__}")
#         print(f"Args are >> {', '.join(str(arg) for arg in args)}")
#         print(f"KWArgs are >> {', '.join(f"{k} : {v}" for k,v in kwargs.items())}")
#         result = func(*args, **kwargs)
#         return result

#     return wrapper


# @debug
# def print_name_age(name, age):
#     print(f"{name} is {age} years old !")


# print_name_age(name="Faraz Ahmad", age=34)


# Questions 3: Make a caching decorator

# import time


# def cache(func):
#     cache_value = {}
#     print(cache_value)

#     def wrapper(*args):
#         print(cache_value)
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args] = result
#         return result

#     return wrapper


# @cache
# def long_running_fun(a, b):
#     time.sleep(4)
#     print(f"Adding {a} and {b}")
#     return a + b


# print(long_running_fun(2, 3))
# print(long_running_fun(3, 5))
# print(long_running_fun(1, 2))
# print(long_running_fun(2, 3))
# print(long_running_fun(5, 3))
