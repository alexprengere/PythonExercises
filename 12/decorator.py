
from datetime import datetime
from functools import wraps
import time


def measure(N=1):
    def _measure(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            start = datetime.now()
            for _ in range(N):
                res = f(*args, **kwargs)
            end = datetime.now()
            print((end - start) / N)
            return res
        return wrapped
    return _measure


@measure(N=2)
def long_function(e):
    time.sleep(1)
    print(e)


long_function(5)
print long_function.__name__
