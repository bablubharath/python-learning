import math

def mathmodule():
    a = float(input('Enter a number: '))

    square_root = math.sqrt(a)
    log = math.log(a)
    sine = math.sin(a)

    print(f"Square root: {square_root}")
    print(f"Logarithm: {log}")
    print(f"Sine: {sine}")

mathmodule()