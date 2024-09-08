# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        li = list(map(int, re.findall(r'[+-]?\d+',expression)))
        numerator = 0
        denominator = 1

        for i in range(0, len(li), 2):
            n, den = li[i], li[i+1]
            numerator = numerator * den + n *denominator
            denominator *= den

        c_div = gcd(numerator, denominator)
        return f"{numerator// c_div}/{denominator//c_div}"