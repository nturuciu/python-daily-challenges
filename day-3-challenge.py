def currency_converter(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount


if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount: "))
        exchange_rate = float(input("Enter the exchange rate: "))
        converted_amount = currency_converter(amount, exchange_rate)
        print(f"Converted amount: {converted_amount}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for amount and exchange rate.")
