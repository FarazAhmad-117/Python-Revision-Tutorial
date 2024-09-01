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
#         print(f"KWArgs are >> {kwargs}")
#         result = func(*args, **kwargs)
#         return result

#     return wrapper


# @debug
# def print_name_age(name, age):
#     print(f"{name} is {age} years old !")


# print_name_age("Faraz Ahmad", 34)


# Questions 3:
