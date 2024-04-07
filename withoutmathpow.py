def calculate_power(base, exponent):
    result = 1

    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    for i in range(exponent):
        result *= base

    return result

if __name__ == "__main__":
    base = float(input("Enter base number: "))
    exponent = int(input("Enter exponent: "))

    result = calculate_power(base, exponent)

    print(base, "raised to the power of", exponent, "is:", result)