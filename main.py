def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """

    number = -1
    while not (0 < number < 100):
        user_input = input("Enter a number greater than 0 and less than 100: ")
        if user_input.isdigit():
            number = int(user_input)
            if not (0 < number < 100):
                print("Invalid input. Please enter a number greater than 0 and less than 100.")
        else:
            print("Invalid input. Please enter a valid integer.")

    print(number)

    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
