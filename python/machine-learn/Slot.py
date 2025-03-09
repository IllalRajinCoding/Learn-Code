MAX_LINES = 3

def deposit():
    while True:
        amount = input("Apa kamu ingin deposit? Rp.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit harus lebih dari 0")
        else:
            print("Deposit harus berupa angka")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            alines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Harus berupa angka")
    return lines

def main():
    balance = deposit()
    lines = get_number_of_lines()

main()

