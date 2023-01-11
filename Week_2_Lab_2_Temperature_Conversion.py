# Rashelle Ward
# CIS261
# Temperature Conversion

def toCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def toFahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

if __name__ == "__main__":
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(toCelsius(temp), 2), "Celsius")

    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(toFahrenheit(temp), 2), "Fahrenheit")
