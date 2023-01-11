# Rashelle Ward
# CIS261
# Temperature Conversion

def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

if __name__ == "__main__":
    for temp in range(0, 212, 40):
        print(temp, "Degrees Fahrenheit =", round(to_celsius(temp), 2), "Degrees Celsius")

#    for temp in range(0, 100, 20):
#        print(temp, "Degrees Celsius =", round(to_fahrenheit(temp), 2), "Degrees Fahrenheit")
