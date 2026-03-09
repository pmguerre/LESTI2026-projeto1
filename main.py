from get_float import *
from get_int import *

if __name__ == "__main__":
    x = get_float("x: ")
    i = get_int("y: ")
    z = x * i
    print(f"{x}*{i} = {z}")
