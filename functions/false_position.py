from .parse_func import parse_func

def false_position(func_str, x_lower, x_upper, tol=1e-6, max_iter=100):
    f = parse_func(func_str)
    f_lower = f(x_lower)
    f_upper = f(x_upper)
    if f_lower * f_upper >= 0:
        raise ValueError("O intervalo inicial não contém raiz (f(a) e f(b) devem ter sinais opostos).")

    for i in range(1, max_iter + 1):
        x_r = x_upper - (f_upper * (x_lower - x_upper)) / (f_lower - f_upper)
        f_r = f(x_r)
        error = abs(x_r - x_upper)

        if f_lower * f_r < 0:
            x_upper = x_r
            f_upper = f_r
        else:
            x_lower = x_r
            f_lower = f_r

        if error < tol:
            return x_r, i, error

    return x_r, max_iter, error