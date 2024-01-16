import functools, time


class time_limit_warning:
    def __init__(self, max_time):
        self.max_time = max_time

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            val = func(*args, **kwargs)
            end = time.perf_counter()
            work_time = end - start
            if work_time > self.max_time:
                print(f'Работа функции {func.__name__} занимает более {self.max_time} секунд!')
            return val
        return wrapper 


@time_limit_warning(5)
def to_zero(num):
    if not num:
        print('END')
    else:
        time.sleep(1)
        to_zero(num-1)


to_zero(10)