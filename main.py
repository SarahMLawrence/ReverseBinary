def csReverseIntegerBits(n):
    return int(bin(n)[:1:-1], 2)