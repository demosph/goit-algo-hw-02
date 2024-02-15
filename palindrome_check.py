from collections import deque

def is_palindrome(input_str):
    input_str = input_str.lower().replace(" ", "")
    char_queue = deque(input_str)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True


try:
    while True:
        # Введення рядка з клавіатури
        user_input = input("Enter a string: ")

        if is_palindrome(user_input):
            print("This is a palindrome!")
        else:
            print("This is not a palindrome.")

except KeyboardInterrupt:
    print("Program terminated by user.")