def emoji_stack_interpreter(file_path):
    # Initialize a stack of 256 cells (all set to 0)
    stack = [0] * 256
    pointer = 0  # Stack pointer
    output = []  # To store the flag characters

    # Read the contents of the input file (emojis)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read().strip()

    i = 0
    while i < len(data):
        command = data[i]

        if command == '👉':
            pointer = (pointer + 1) % 256  # Move right
        elif command == '👈':
            pointer = (pointer - 1) % 256  # Move left
        elif command == '👍':
            stack[pointer] = (stack[pointer] + 1) % 256  # Increment (bounded by 255)
        elif command == '👎':
            stack[pointer] = (stack[pointer] - 1) % 256  # Decrement (bounded by 0)
        elif command == '💬':
            # Print the ASCII value of the current cell
            output.append(chr(stack[pointer]))
        elif command == '🔁':
            # Repeat the previous command
            repeat_count = int(data[i+1:i+3], 16)  # Get the repeat count (hexadecimal)
            last_command = data[i - 1]  # Get the last command

            if last_command == '👍':
                stack[pointer] = (stack[pointer] + repeat_count) % 256
            elif last_command == '👎':
                stack[pointer] = (stack[pointer] - repeat_count) % 256
            elif last_command == '👉':
                pointer = (pointer + repeat_count) % 256
            elif last_command == '👈':
                pointer = (pointer - repeat_count) % 256

            i += 2  # Skip the next two characters (hex value of repeat count)
        
        i += 1

    return ''.join(output)


# Run the interpreter on the provided input file
flag = emoji_stack_interpreter('input.txt')
print("Extracted Flag:", flag)
