def get_card_type(number):
    if number.startswith("4"):
        return "Visa"
    elif number.startswith("5"):
        return "MasterCard"
    elif number.startswith("37"):
        return "American Express"
    elif number.startswith("6"):
        return "Discover"
    else:
        return "Invalid Card Type"

def is_luhn_valid(number):
    sum = 0
    is_even = False

    for digit_char in reversed(number):
        if digit_char.isdigit():
            digit = int(digit_char)
            if is_even:
                digit *= 2
                if digit >= 10:
                    digit = digit % 10 + digit // 10
            sum += digit
            is_even = not is_even

    return sum % 10 == 0

def validate_card(number):
    card_type = get_card_type(number)
    if card_type == "Invalid Card Type":
        return f"Invalid Card Type: {number}"

    if is_luhn_valid(number):
        return f"{card_type} card - Valid: {number}"
    else:
        return f"{card_type} card - Invalid: {number}"


if __name__ == "__main__":
    card_number = input("Enter your credit card number: ")
    validation_result = validate_card(card_number)
    print(validation_result)