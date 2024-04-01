def convertTemperature(celsius: float) -> list[float]:
    return [celsius + 273.15, celsius * 1.80 + 32.00]


celsius = 36.50
print(convertTemperature(celsius))

