def type_converter(type_of_output):
    def real_decorator(func):
        def wrapper():
            x = func()
            return type_of_output(x)
        return wrapper
    return real_decorator


@type_converter(str)
def return_int():
    return 3


@type_converter(int)
def return_string():
    return "not a number"


y = return_int()
print(type(y).__name__)

try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")
