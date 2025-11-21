from collections import deque

def is_palindrome(text):
    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    chars = deque(normalized)
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True

def main():
    print("Перевірка рядка на паліндром (deque).")
    user_input = input("Введи рядок: ")
    if is_palindrome(user_input):
        print("Рядок є паліндромом.")
    else:
        print("Рядок не є паліндромом.")

if __name__ == "__main__":
    main()
