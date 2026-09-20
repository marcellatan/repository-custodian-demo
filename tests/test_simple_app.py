from src.simple_app import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    convert_temperature,
)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0


def test_convert_temperature_celsius():
    assert convert_temperature(100, "C") == 212


def test_convert_temperature_fahrenheit():
    assert convert_temperature(32, "F") == 0