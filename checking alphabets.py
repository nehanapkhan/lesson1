def is_all_alphabets(text):
    """
    Check if the input string contains only alphabets.

    Args:
        text (str): The string to check.

    Returns:
        bool: True if the string contains only alphabets, False otherwise.
    """
    return text.isalpha()

if __name__ == "__main__":
    user_input = input("Enter a string: ")

    if is_all_alphabets(user_input):
        print("The string contains only alphabets.")
    else:
        print("The string contains characters other than alphabets.")
