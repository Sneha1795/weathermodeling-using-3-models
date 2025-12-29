import math
import matplotlib.pyplot as plt

def quadratic_solver(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        return r1, r2
    else:
        return None

def plot_weather_model(a, b, c):
    x = range(-4, 5)
    y = [a*i*i + b*i + c for i in x]

    plt.plot(x, y)
    plt.axhline(0)
    plt.axvline(0)
    plt.title("Waterfall Model - Weather Prediction")
    plt.xlabel("Time")
    plt.ylabel("Weather Value")
    plt.grid(True)
    plt.show()

# Fixed requirements
a, b, c = 2, -7, 3
print("Roots:", quadratic_solver(a, b, c))
plot_weather_model(a, b, c)
