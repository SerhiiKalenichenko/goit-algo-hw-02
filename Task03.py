def is_brackets_sequence_valid(sequence):
    stack = []
    opening = "([{"
    closing = ")]}"
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in sequence:
        if ch in opening:
            stack.append(ch)
        elif ch in closing:
            if not stack:
                return False
            if pairs[ch] != stack.pop():
                return False
    return len(stack) == 0

def main():
    print("Перевірка симетрії дужок (стек).")
    examples = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }"
    ]
    for expr in examples:
        result = "Симетрично" if is_brackets_sequence_valid(expr) else "Несиметрично"
        print(f"{expr}: {result}")

    user_input = input("Введи власний вираз для перевірки: ")
    result = "Симетрично" if is_brackets_sequence_valid(user_input) else "Несиметрично"
    print(f"{user_input}: {result}")

if __name__ == "__main__":
    main()
