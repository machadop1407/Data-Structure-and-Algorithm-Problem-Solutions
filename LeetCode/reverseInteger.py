
# Given a 32-bit signed integer, reverse digits of an integer.

def reverse(self, x: int) -> int:

    reversedInt = 0
    number = 0

    if x > 0:
        while math.floor(x) is not 0:
            number = int(x % 10)
            x /= 10
            reversedInt = (reversedInt * 10) + number
    else:
        x *= -1
        while math.floor(x) is not 0:
            number = int(x % 10)
            x /= 10
            reversedInt = (reversedInt * 10) + number
        if (reversedInt * -1) < (-2 ** 31):
            return 0
        return reversedInt * -1

    if reversedInt > (2 ** 31 - 1):
        return 0

    return reversedInt
