from math import sqrt, isinf, isnan

eps = 1e-14


def solve(a: float, b: float, c: float) -> list:
    if any(map(isinf, [a, b, c])):
        raise ValueError("Коэффициенты должны отличаться от бесконечности.")

    if any(map(isnan, [a, b, c])):
        raise ValueError("Коэффициенты должны отличаться от nan.")

    if -eps < a < eps:
        raise ValueError("Коэффициент 'а' должен отличаться от нуля.")

    d: float = b * b - 4 * a * c

    if -eps < d < eps:
        return [-b / 2 / a, ]
        
    elif d < eps:
        return []
    else:
        return [
            (-b + sqrt(d)) / 2 / a,
            (-b - sqrt(d)) / 2 / a
        ]
        