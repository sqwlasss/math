from scipy.integrate import quad
import numpy as np

import matplotlib.pyplot as plt


def quadratic_function(x, a, b, c):
    return a * x ** 2 + b * x + c


def area_below_x_axis(a, b, c):
    f = lambda x: quadratic_function(x, a, b, c)

    area, error = quad(lambda x: abs(f(x)) if f(x) < 0 else 0, -np.inf, np.inf)
    # -np.inf, np.inf границы

    return area, error


def plot_quadratic_with_shading(a, b, c):
    x = np.linspace(-10, 10, 400)
    #a b c указаны снизу
    # ПРИМЕР КВАДРАТНОГО УРАВНЕНИЯ
    y = a * x ** 2 + b * x + c

    plt.fill_between(x, y, where=(y < 0), color='gray', alpha=0.5, label='Площадь под Ox')

    plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Квадратное уравнение с заштрихованной областью под осью x')


    plt.legend()


    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()


a, b, c = 1, -1, -72
area, error = area_below_x_axis(a, b, c)
plot_quadratic_with_shading(a, b, c)
print(f"Area below x-axis: {area:.2f}")
print(f"Error estimate: {error:.2e}")
