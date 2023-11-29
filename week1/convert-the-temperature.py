class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = [0,0]
        fahrenheit = float(celsius) * 1.80 + 32.00
        kelvin = celsius + 273.15
        ans[0] = kelvin
        ans[1] = fahrenheit

        return ans
        