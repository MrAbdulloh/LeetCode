from fractions import Fraction


def fractionAddition(expression: str):
    fractions = []
    num = ""
    for ch in expression:
        if ch in "+-":
            if num:
                fractions.append(Fraction(num))
            num = ch
        else:
            num += ch
    fractions.append(Fraction(num))
    result = sum(fractions)
    return f"{result.numerator}/{result.denominator}"


# expression = "1/3-1/2"
# expression = "-1/2+1/2+1/3"
expression = "-1/2+1/2"
print(fractionAddition(expression))