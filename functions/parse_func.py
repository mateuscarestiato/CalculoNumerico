import math

def parse_func(func_str):
    """
    Converte uma expressão em string para uma função f(x) segura.
    """
    allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
    def f(x):
        local_dict = allowed_names.copy()
        local_dict['x'] = x
        return eval(func_str, {"__builtins__": {}}, local_dict)
    return f