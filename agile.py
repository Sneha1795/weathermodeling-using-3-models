import math
import matplotlib.pyplot as plt

def quadratic_solver(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        return (-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a)
    else:
        return None

def plot_weather_model(a, b, c, sprint):
    x = range(-4, 5)
    y = [a*i*i + b*i + c for i in x]
    plt.plot(x, y, label=sprint)

# Sprint 1 – basic model
plot_weather_model(1, -4, 2, "Sprint 1")

# Sprint 2 – feedback based update
plot_weather_model(2, -6, 3, "Sprint 2")

# Sprint 3 – optimized model
plot_weather_model(3, -8, 4, "Sprint 3")

plt.axhline(0)
plt.axvline(0)
plt.xlabel("Time")
plt.ylabel("Weather Value")
plt.title("Agile Model - Sprint-wise Weather Prediction")
plt.legend()
plt.grid(True)
plt.show()
