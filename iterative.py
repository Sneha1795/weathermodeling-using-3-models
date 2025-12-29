
import math
import matplotlib.pyplot as plt

def quadratic_solver(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        return (-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a)
    else:
        return None

def plot_weather_model(a, b, c, label):
    x = range(-4, 5)
    y = [a*i*i + b*i + c for i in x]
    plt.plot(x, y, label=label)

# Iteration 1
plot_weather_model(1, -5, 4, "Iteration 1")

# Iteration 2 (improved coefficients)
plot_weather_model(2, -7, 3, "Iteration 2")

# Iteration 3 (more refined)
plot_weather_model(3, -9, 5, "Iteration 3")

plt.axhline(0)
plt.axvline(0)
plt.xlabel("Time")
plt.ylabel("Weather Value")
plt.title("Iterative Model - Weather Improvement")
plt.legend()
plt.grid(True)
plt.show()
