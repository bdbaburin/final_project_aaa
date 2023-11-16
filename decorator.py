import functools
import time


def pizza_log(string: str = "Time: {}"):
    def log_inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(string.format(end_time - start_time))
            return result

        return wrapper

    return log_inner


if __name__ == "__main__":
    pass
