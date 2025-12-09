import logging

logger = logging.getLogger("simple_logger")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("assignment3/decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info("function: " + func.__name__)

        if len(args) == 0:
            logger.info("positional parameters: none")
        else:
            logger.info("positional parameters: " + str(list(args)))

        if len(kwargs) == 0:
            logger.info("keyword parameters: none")
        else:
            logger.info("keyword parameters: " + str(kwargs))

        result = func(*args, **kwargs)

        logger.info("return: " + str(result))
        logger.info("--------------------")

        return result
    return wrapper


@logger_decorator
def hello():
    print("Hello World")


@logger_decorator
def many_args(*args):
    return True


@logger_decorator
def many_kwargs(**kwargs):
    return logger_decorator


hello()
many_args(1, 2, 3)
many_kwargs(name="Bob", age=20)
