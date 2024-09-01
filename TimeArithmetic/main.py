import time


def sum(*args):     
    start = time.time()
    for arg in args:
        time.sleep(arg)

    return int(round(time.time() - start))


def sub(num2, num1):
    start = time.time()
    time.sleep(num1)
    sub_time = time.time()
    time.sleep(num2)

    return int(round(time.time() + start - 2 * sub_time))


print(sum(3, 7, 5), sub(8, 3))
