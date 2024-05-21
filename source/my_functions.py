
def add(num_one, num_two):
    return num_one + num_two


def divide(num_one, num_two):
    if num_two == 0:
        raise ZeroDivisionError

    return num_one / num_two

