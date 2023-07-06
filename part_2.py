import time
from multiprocessing import Pool, cpu_count


def factorize(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result


def factorize_parallel(*numbers):
    pool = Pool(cpu_count())
    result = pool.map(get_factors, numbers)
    pool.close()
    pool.join()
    return result


def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


# Приклад використання та перевірка правильності роботи

def test_factorize(factorize_func):
    a, b, c, d = factorize_func(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    print("Test passed.")


if __name__ == "__main__":
    numbers = (128, 255, 99999, 10651060)

    start_time = time.time()
    factorize_sync_result = factorize(*numbers)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Synchronous execution time: {execution_time} seconds")
    test_factorize(factorize)

    start_time = time.time()
    factorize_parallel_result = factorize_parallel(*numbers)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Parallel execution time: {execution_time} seconds")
    test_factorize(factorize_parallel)
