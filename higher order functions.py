
import doctest


def fixed_point_iteration(f, x=1.0):
    """
    This function returns the number of iterations required to achieve the
    desired value. The approach is known as fixed point iteration.
    doctest 1:
    >>> from math import sin,cos
    >>> fixed_point_iteration(lambda x: sin(x) + x, 3.0)
    (3.141592653589793, 3)
    >>> fixed_point_iteration(lambda x: cos(x), 1.0)
    (0.7390851332151611, 86)

    """
    step = 0
    while not approx_fixed_point(f, x):
        x = f(x)
        step += 1
    return x, step


def newton_find_zero(f1, f2, x):
    """
    This function returns the number of iterations required to achieve the desired 
    value. This approach is known as Newton's method.
    doctest 2:
    >>> from math import sin,cos
    >>> newton_find_zero(lambda x: sin(x) , lambda x: cos(x), 3.0)
    (3.141592653589793, 3)
    >>> newton_find_zero(lambda x: cos(x) - x , lambda x: -sin(x)-1, 1.0) 
    (0.7390851332151607, 4)
    """
    step = 0

    while not approx_fixed_point(lambda x: x - (f1(x)/f2(x)), x):
        x = x - (f1(x)/f2(x))
        step += 1
    return x, step


def approx_fixed_point(f, x):
    # using absolute to make (a-b)=(b-a)
    if abs(f(x) - x) <= (10 ** (-15)):
        return True
    else:
        return False


if __name__ == "__main__":
    doctest.testmod(verbose=True)
