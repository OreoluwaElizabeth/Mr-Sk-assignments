def main():
    num = int(input("Enter a non-negative integer: "))

    if num < 0:
        print("Error message: can't calculate negative value")
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print("The factorial of", num, "is:", factorial)

if __name__ == "__main__":
    main()