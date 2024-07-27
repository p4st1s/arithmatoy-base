# Aucun n'import ne doit être fait dans ce fichier


def nombre_entier(n: int) -> str:
    """retourne la représentation d'un nombre avec des S

    Args:
        n (int): entier positif à représenter

    Returns:
        str: représentation du nombre
    Exemple:
        0 (int): '0'
        1 (int): 'S0'
        2 (int): 'SS0'
        7 (int): 'SSSSSSS0'
    """
    return n * "S" + "0"
    return f"{S * n}0"


def S(n: str) -> str:
    """retourne le successeur d'un nombre

    Args:
        n (str): nombre à incrémenter

    Returns:
        str: nombre incrémenté

    Exemple:
        0 (str): 'S0'
        S0 (str): 'SS0'
        SS0 (str): 'SSS0'
        SSSSSSS0 (str): 'SSSSSSSS0'
    """
    return "S" + n
    return f"S{n}"


def addition(a: str, b: str) -> str:
    """retourne la somme de deux nombres

    Args:
        a (str): nombre a sous fourme S0
        b (str): nombre b sous forme S0

    Returns:
        str: somme des deux nombres

    Exemple:
        addition('0', 'SS0') -> 'SS0'
        addition('SS0', 'SS0') -> 'SSSS0'
    """
    if a == "0":
        return b
    return S(addition(a[1:], b))


def multiplication(a: str, b: str) -> str:
    """
    Multiply two numbers represented as strings.

    Args:
        a (str): The first number.
        b (str): The second number.

    Returns:
        str: The product of the two numbers.
    """
    if a == "0" or b == "0":
        return "0"
    return addition(b, multiplication(a[1:], b))


def facto_ite(n: int) -> int:
    """
    Calculate the factorial of a given number using an iterative approach.

    Parameters:
    n (int): The number for which the factorial needs to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def facto_rec(n: int) -> int:
    """
    Recursive function to calculate the factorial of a number.

    Parameters:
    n (int): The number for which factorial needs to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    return n * facto_rec(n - 1)


def fibo_rec(n: int) -> int:
    """
    Calculate the nth Fibonacci number recursively.

    Parameters:
    n (int): The index of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.

    """
    if n < 2:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)


def fibo_ite(n: int) -> int:
    """
    Calculate the nth Fibonacci number iteratively.

    Parameters:
    n (int): The index of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.

    """
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def golden_phi(n: int) -> float:
    """
    Calculates the golden ratio (phi) for a given number.

    Parameters:
    n (int): The number for which to calculate the golden ratio.

    Returns:
    float: The golden ratio for the given number.
    """
    if n == 0:
        return 1
    return fibo_ite(n + 1) / fibo_ite(n)


def sqrt5(n: int) -> float:
    """
    Calculates the square root of 5 times the given number.

    Args:
        n (int): The number to calculate the square root of 5 times.

    Returns:
        float: The square root of 5 times the given number.
    """
    phi = golden_phi(n + 1)
    return 2 * phi - 1


def pow(a: float, n: int) -> float:
    """
    Calculates the power of a number.

    Args:
        a (float): The base number.
        n (int): The exponent.

    Returns:
        float: The result of raising `a` to the power of `n`.
    """
    return a**n
