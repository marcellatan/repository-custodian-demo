def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_temperature(value, unit):
    if value is None:
        raise ValueError("Temperature value cannot be empty.")

    if unit.lower() == "c":
        return celsius_to_fahrenheit(value)

    if unit.lower() == "f":
        return fahrenheit_to_celsius(value)

    raise ValueError("Unit must be either 'C' or 'F'.")