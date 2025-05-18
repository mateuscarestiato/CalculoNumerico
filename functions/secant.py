from .parse_func import parse_func

def secant(func_str, x0, x1, tol=1e-6, max_iter=100):
    f = parse_func(func_str)
    f_x0 = f(x0)
    f_x1 = f(x1)

    for i in range(1, max_iter + 1):
        denom = (f_x1 - f_x0)
        if denom == 0:
            raise ZeroDivisionError("Divisão por zero no denominador do método da secante.")

        x2 = x1 - f_x1 * (x1 - x0) / denom
        error = abs(x2 - x1)

        x0, f_x0 = x1, f_x1
        x1, f_x1 = x2, f(x2)

        if error < tol:
            return x2, i, error

    return x2, max_iter, error