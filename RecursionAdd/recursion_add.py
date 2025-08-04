import sys
sys.setrecursionlimit(10000)


def add(a: float, b: float, h: float = 1) -> float:
    if abs(b) > 0.0001: 
        sign = 1
        if b < 0:
            sign *= -1

        if abs(b - sign * h) < abs(b):
            return add(a + sign * h, b - sign * h, h)
        
        return add(a + sign * h, b - sign * h, h / 2)

    else:
        return a


if __name__ == '__main__':
    for a, b in [(3, 4), (-3, 5), (-1, -2), (1.2, -3.7)]:
        print(f'({a}) + ({b}) = {add(a, b)}')




