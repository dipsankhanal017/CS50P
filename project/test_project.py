from project import getCityData, getTemperature, getPressure, getHumidity

def test_getTemperature():
    data = getCityData("kathmandu")
    temperature = getTemperature(data)
    assert 0 < temperature < 50

def test_getPressure():
    data = getCityData("new york")
    pressure = getPressure(data)
    assert 0 < pressure < 100

def test_getHumidity():
    data = getCityData("pokhara")
    humidity = getHumidity(data)
    assert humidity > 0
