import logging
import time
from functools import wraps
from typing import Any

logger: logging.Logger = logging.getLogger(__name__)


def time_it(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time: float = time.time()
        res: Any = func(*args, **kwargs)
        end_time: float = time.time()
        logger.info(
            "Function called.",
            extra={
                "function": func.__name__,
                "args": args,
                "kwargs": kwargs,
                "error": "",
                "timing": f"{end_time - start_time} seconds"})
        return res

    return wrapper


@time_it
def my_func(a: int, b: int) -> int:
    return a + b
