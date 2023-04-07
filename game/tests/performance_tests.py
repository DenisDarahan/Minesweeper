import math
import time
import typing


def timeit(function: typing.Callable) -> typing.Callable:
    def decorator(*args, **kwargs):
        summary_time, repeats = 0, 10_000

        for _ in range(repeats):
            start = time.perf_counter()

            function(*args, **kwargs)

            stop = time.perf_counter()
            summary_time += stop - start

        print(f'Average {function.__name__} time is: {(summary_time / repeats):.10f}')
    return decorator


@timeit
def single_cycle(size: int):
    _divider = int(math.sqrt(size))

    for i in range(size):
        _ = sum(divmod(i, _divider))


@timeit
def double_cycle(size: int):
    _size = int(math.sqrt(size))

    for i in range(_size):
        for j in range(_size):
            _ = sum((i, j))


def test_cycles():
    # double_cycle is faster
    # Average single_cycle time is: 0.0013202717
    # Average double_cycle time is: 0.0008829882

    _size = 10_000
    single_cycle(_size)
    double_cycle(_size)


if __name__ == '__main__':
    test_cycles()
