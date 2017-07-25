import math
import matplotlib.pyplot as plt

if __name__ == "__main__":
    base = 1 + 9.8 / 100

    l_x = [x for x in range(1, 20, 1)]
    l_y = [base**x for x in l_x]
    ly2 = [math.log10(y) for y in l_y]
    ly3 = [x * math.log10(base) for x in l_x]

    plt.plot(l_x, l_y, label="power(base, x)", color='red', linewidth=1)
    plt.plot(l_x, ly2, "-", label='log10(base^x)', color="g", lw=1)
    plt.plot(l_x, ly3, ".", label='x*log10(base)', color='b', lw=4)
    plt.legend()
    plt.show()