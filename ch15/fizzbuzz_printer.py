import logging


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    filename="fizzbuzz.log",
                    datefmt="%Y-%m-%d %H:%M:%S")


logger = logging.getLogger(__name__)



FIZZBUZZ_COUNTER = 0


def log_function_args(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Function {func.__name__} called with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)

    return wrapper


def increment_counter(func):
    def wrapper(*args, **kwargs):
        global FIZZBUZZ_COUNTER
        FIZZBUZZ_COUNTER += 1
        logger.info(f"Function {func.__name__} called {FIZZBUZZ_COUNTER} times")
        return func(*args, **kwargs)

    return wrapper


def validate_args_types_and_limits(min_limit: int, max_limit: int):
    def decorator(func):
        def wrapper(limit: int):
            if not isinstance(limit, int):
                raise TypeError(f"Argument 'limit' must be of type int, got {type(limit)}")
            if limit < min_limit or limit > max_limit:
                raise ValueError(f"Argument 'limit' must be between {min_limit} and {max_limit}, got {limit}")
            return func(limit)

        return wrapper

    return decorator


@log_function_args
@increment_counter
@validate_args_types_and_limits(0, 500)
def print_fizzbuzz(limit: int) -> None:
    for i in range(1, limit + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


print_fizzbuzz(5)
print_fizzbuzz(50)
