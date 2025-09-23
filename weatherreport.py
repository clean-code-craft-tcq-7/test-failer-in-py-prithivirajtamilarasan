

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def sensorStubHighPrecipLowWind():
    return {
        'temperatureInC': 30,
        'precipitation': 70,
        'humidity': 80,
        'windSpeedKMPH': 40
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if readings['temperatureInC'] > 25:
        if readings['precipitation'] >= 60:
            weather = "Rainy Day"
        elif 20 <= readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testRainy():
    weather = report(sensorStub)
    print("Weather reported:", weather)
    assert("rain" in weather.lower())

def testHighPrecipitation():
    weather = report(sensorStubHighPrecipLowWind)
    print("Weather reported:", weather)
    assert("rain" in weather.lower())


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
